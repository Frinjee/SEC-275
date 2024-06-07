import scapy.all as scapy
import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Addresses')
	opts = parser.parse_args()

	# check for errors, quit if arg is missing, display error message
	if not opts.target:
		parser.error('[-] Specificy address')
	return opts


def scan(ip):
	arp_rq_frame = scapy.ARP(pdst = ip)
	bc_eth_frame = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
	bc_eth_arp_rq_frame = bc_eth_frame / arp_rq_frame

	a_list = scapy.srp(bc_eth_frame, timeout = 1, verbose = False)[0]
	result = []

	for _ in range(0, len(a_list)):
		client_dict = {'ip': a_list[i][1].psrc, 'mac': a_list[i][1].hwsrc}
		result.append(client_dict)
	return result

opts = get_args()
sc_output = scan(opts.target)