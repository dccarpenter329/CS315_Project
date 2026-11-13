
import hashlib
import itertools
import time
import os
import dictionary

foundPassword = False
totalAttempts = 0


def validatePassword(password):
    # First checking to see if password is correct length
    if len(password) != 8:
        return False

    # Initializing variable counts
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

    while not validatePassword(targetPassword):
        print("Password must contain exactly 5 letters, 2 numbers, and 1 symbol (!, @, $).")
        print("Please try again.")
        targetPassword = input("Please enter password: ")

    print("Password cracking method:")
    print("1 - Brute force")
    print("2 - Dictionary method")
    print("3 - Dictionary/brute force hybrid")

    method = input("What method would you like to use? ")

    while method not in ["1", "2", "3"]:
        print("Please select a valid option: 1, 2, or 3.")
        method = input("What method would you like to use? ")

    if method == "2":
        dictionary.dictionary_password_cracking(targetPassword)


if __name__ == "__main__":
    main()
