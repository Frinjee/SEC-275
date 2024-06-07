
# create and empty variable to store our decimal input
dec = ''

# execute the while loop repeatedly until input is not numeric
while(not(dec.isnumeric())):
	# get user input & and set 'dec' to user input
	dec = input('Enter decimal to convert to octal: ')

# create a temp variable to store our converted user input
_dec = int(dec)
# create an empty variable to store remainder
remainder = ''

# execute the while loop repeatedly until our qoutient is 0
while(_dec > 0):
	# use modulo (and add remainder) to store our final remainder as new variable oct_val
	oct_val = str(_dec % 8) + remainder
	# set _dec equal to an integer value of our temp decimal value by 8
	# this will not store our qoutient when it is equal to 0 
	_dec = int(_dec / 8)

# display users decimal and converted octal
print(f'Octal of {dec} is: {oct_val}')
