letters = {}

# set variable to user input as uppercase
userword = input("What word or phrase do you want to analyze? ").upper()

# for each letter in user input
for lett in userword:
	# if the letter is in key val of our dictionary
    if lett in letters.keys():
    	# count the occurence of each letter
        letters[lett] += 1

    else:

        letters[lett]=1

for key,value in letters.items():

    print (key + " occurs " + str(value) + " times")