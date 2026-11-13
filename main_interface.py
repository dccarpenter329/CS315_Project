# File: main_interface.py
# Authors: Corinne Carpenter
# 	 Lauren Chilen
# 	 Sophia Eads
# Version: 1.0 11/7/2026
# Description: Password Cracking Program
# 	     - User enters password to start
# 	     - User may pick either use hashing, dictionary/brute force, or pure brute force

# 	    TO-DO
# 	     - Add "go back" features to try different methods/make alterations
# 	     - Let the user "play again" w/o leaving the program
# 	     - Have a "high score" features that shows the least iterations/fastest time
# Resources:
# [r1]: https://www.geeksforgeeks.org/python/os-module-python-examples/
# [r2]: https://docs.python.org/3/library/time.html



import hashlib
import itertools
import time
import os	#r1
import dictionary
import hybrid
import bruteForce

foundPassword = False
totalAttempts = 0

def validatePassword(password):
	# first checking to see if password is correct length
    if len(password) != 8: # be 12345678 long
        return False
	# initializing variable counts
    letters = 0
    numbers = 0
    symbols = 0

    for character in password:
        if character in "abcdefghijklmnopqrstuvwxyz":
            letters += 1
        elif character in "0123456789":
            numbers += 1
        elif character in "!@$":
            symbols += 1
        else:
            return False

    return letters == 5 and numbers == 2 and symbols == 1

def main():
	targetPassword = input("Please enter password: ")

	if not validatePassword(targetPassword):
		print("Password must contain exactly 5 letters, 2 numbers, and 1 symbol (!, @, $).")
		print("Please try again.")

    print("Password cracking method: ")
    print("1-Brute force")
    print("2-Dictionary method")
    print("3- Dictionary/brute force hybrid")
    method = input("What method would you like to use the crack the password?") # Selecting a method to password crack
    while method not in ["1", "2", "3"]: 
        print("Please select a valid option- 1, 2, or 3 ")
        method = input("What method would you like to use the crack the password?")

    if method=="1":
        # link to brute force code
		bruteForce.ADD_FUNCTION_NAME
    elif method=="2":
        # link to dictionary method
		# dictionary fucntion will intake target password and try to find the correct one
		dictionary.dictionary_password_cracking(targetPassword)
    elif method=="3":
        # link to hybrid method
		hybrid.hybrid_password_cracking(targetPassword)


