import hashlib
import itertools
import time
import os
import dictionary
import hybrid

foundPassword = False
totalAttempts = 0

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

def bruteForce(password):
    count = 0
    nFound = 0
    passwordFound = False
    quit = 1        #1 means keep cycling, 2 means quit

    while nFound != 1:
        print("You may select between 5 and 10 characters.") # Added this since the determined password WILL be exactly 8 characters long
        n = int(input("How many characters would you like to try? "))

        if n < 5 or n > 10:
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
        print("Password must contain exactly 5 letters (lowercase), 2 numbers, and 1 symbol (!, @, $).")
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

    if method == "1":
        bruteForce(targetPassword)

    if method == "2":
        dictionary.dictionary_password_cracking(targetPassword)

    if method == "3":
        hybrid.hybrid_password_cracking(targetPassword)

if __name__ == "__main__":
    main()
