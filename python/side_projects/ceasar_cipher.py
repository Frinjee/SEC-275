alphabet = {
	'a': '😀', 'b': '😃', 'c': '😄', 'd': '😁', 'e': '😆', 'f': '😅', 'g': '😂', 'h': '🤣', 'i': '😊', 'j': '😇',
    'k': '🙂', 'l': '🙃', 'm': '😉', 'n': '😌', 'o': '😍', 'p': '😘', 'q': '😗', 'r': '😙', 's': '😚', 't': '😋',
    'u': '😜', 'v': '😝', 'w': '😛', 'x': '🤑', 'y': '😎', 'z': '🤓'
}

def ceasar_cipher(txt, shift):

	enc_txt = ""

	for c in txt.lower():

		if c.isalpha():
			e_char = alphabet[c]
			enc_txt += e_char
		else:
			enc_txt += c

	return enc_txt

usr_input = input('Enter text to encrypt: ')
shift = int(input('Enter the shift value: '))

enc_txt = ceasar_cipher(usr_input, shift)
print('Original Text: ', usr_input)
print('Encrypted: ', enc_txt)

