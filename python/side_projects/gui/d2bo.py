#!/usr/bin/python3

#create an empty variable to store decimal input
number = ''

# set the while loop to repeatedly execute until the input is not numeric

while(not(number.isnumeric())):
	# get user input for the decimal they want to convert &
	# set our prev created varaible 'number' to our users input
	number = input('What is the decimal you want to convert? ')

# create temp variable '_num' and set to our converted (to integer) input variable 'number'
_num = int(number)

# create an empty variable to store our converted binary 
bin_conv = ''

# execute the loop repeatedly while our '_num' variable is greater than 0
while(_num > 0):
	# set 'bin_conv' to the (string) sum of our integer (_num % 2) + bin_conv
	bin_conv = str(_num % 2) + bin_conv
	# convert and set _num back to an integer sum of _num / 2
	_num = int(_num / 2)

# print our decimal that has been converted to binary
print(f'Binary of {number} is {bin_conv}')

