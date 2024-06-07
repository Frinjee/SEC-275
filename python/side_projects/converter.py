menu_opts = 'Select Conversion Method \n1: dec to bin, 2: bin to dec, 3: dec to octal, 4: dec to hex, 5: hex to dec - '

def decimal_to_binary(d):

	_d = int(d)
	print(f'Binary of {d} is:', bin(_d)[2:])

def binary_to_decimal(b):

	_s = str(b)
	i_val = int(_s,2)
	
	print(f'Decimal of {_s} is: {i_val}'.format())

def decimal_to_octal(o):

	_o = int(o)
	print(f'Octal of {o} is:', oct(_o)[2:])

def decimal_to_hex(h):

	print(f'Hex of {h} is:', hex(h))

def hex_to_decimal(hex):
	
	_h = int(hex, 16)
	str(_h)
	print(f'Decimal of {hex} is:', +_h)

select = int(input(menu_opts))

if select == 1:
	try:
		d = input('Enter decimal to convert: ')	
		decimal_to_binary(d)
	except ValueError:
		print(f'{d} is not a valid input')
elif select == 2:
	try:
		b = int(input('Enter binary to convert: '))
		binary_to_decimal(b)
	except ValueError:
		print(f'{b} is not a valid input')
elif select == 3:
	try:
		o = int(input('Enter decimal to convert: '))
		decimal_to_octal(o)
	except ValueError:
		print(f'{o} is not a valid input')
elif select == 4:
	try:
		h = int(input('Enter decimal to convert: '))
		decimal_to_hex(h)
	except ValueError:
		print(f'{h} is not a valid input')
elif select == 5:
	try:
		hx = input('Enter hex to convert: ')
		hex_to_decimal(hx)
	except ValueError:
		print(f'{hx} is not a valid input')