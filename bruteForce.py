"""
File: bruteForce.py
Author: Sophia Eads
Date: 11/5/2026
Description: password cracking using brute force
Resources:
"""

characters = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
	'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '$'
]


def cycleCombo(combo):
	#convert initial string into list to be able to modify individual characters
	combo = list(combo)

	position = len(combo) - 1

	while position >= 0:
		index = characters.index(combo[position])

		if index < (len(characters) - 1):
			combo[position] = characters[index + 1]
			break
		else:
			combo[position] = characters[0]
			position -= 1
	return ''.join(combo)

def testCombo(combo, password):
	return combo == password

def bruteForce(password): #POST MERGE: change to bruteForce(password)
	count = 0
	nFound = 0
	passwordFound = False
	quit = 1	#1 means keep cycling, 2 means quit

	while nFound != 1:

		n = int(input("How many characters would you like to try? "))

		if n < 1 or n > 5:
			print("Invalid number of characters... Please try again")
			continue
		else:
			nFound = 1

		combo = characters[0] * n

		while (passwordFound != True) and (quit == 1):
			count += 1
			if testCombo(combo, password):
				passwordFound = True
				break
			elif combo == characters[-1] * n:
				print(f"Password not found with {n} character(s). Try a different amount?")
				again = int(input("1 for yes, 2 for no: "))
				if again == 1:
					nFound = 0
					break
				elif again == 2:
					quit = 2
			else:
				combo = cycleCombo(combo)
				continue

		if passwordFound == True:
			print(f"Password was {combo} after {count} iterations.")
		elif quit == 2:
			print("Password was not found.")

bruteForce("test")
