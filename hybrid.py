import time
import os # [r1]
import itertools

baseWords = []
foundPassword = False
totalAttempts = 0

# check if password valid
def validatePassword(password):
    if len(password) != 8: # be 12345678 long
        return False

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

# load words.txt
def loadWords():

    filePath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "words.txt" 
    )

    try:
        with open(filePath, "r") as file:
            for word in file:
                word = word.strip().lower() #error checking for no spaces or capitals
                if len(word) == 5 and word.isalpha():
                    if word not in baseWords:
                        baseWords.append(word) #check dictionary word.txt 
        return True

    except FileNotFoundError:
        print("Error: cannot find file")
        return False

    except OSError:
        print("Error: cannot read file")
        return False
# why is opening the fiel the hardest part of htis
#https://runestone.academy/ns/books/published/fopp/Exceptions/standard-exceptions.html

# move character postions test combination
def generateCandidates(word, digits, symbol):
    seen = set()
    extraCharacters = [digits[0], digits[1], symbol]

    #taking discrete structures matter thank you aj munoz
    for positions in itertools.combinations(range(8), 3):

        # PERMUTATIONS AFTER THE COMBINATIONS 
        for arrangement in itertools.permutations(extraCharacters):
            candidate = [None] * 8
            for position, character in zip(positions, arrangement): #tuple
                candidate[position] = character
#https://www.geeksforgeeks.org/python/zip-in-python/
            letterIndex = 0 # fill the remaining spaces with letters from word

            for index in range(8):
                if candidate[index] is None:
                    candidate[index] = word[letterIndex]
                    letterIndex += 1
#find where num and symbols are first, then fill with letters in order of word from dictionry
            password = "".join(candidate)

            # no dups
            if password not in seen: #send password to next function
                seen.add(password)
                yield password #did not know how to do this, claude helped a. lot.
#https://www.geeksforgeeks.org/python/how-to-use-a-variable-from-another-function-in-python/
#https://stackoverflow.com/questions/16043797/how-do-i-pass-variables-across-functions
#https://discuss.python.org/t/how-to-share-variable-value-between-function/21402

# combine w/ dictionary 
def dictionaryAttack(targetPassword):
    global foundPassword
    global totalAttempts #
    symbols = ["!", "@", "$"]
    #every. dictionary. word.
    for word in baseWords:
        #every. possible. two. digit. combination.
        for number in range(100):
            digits = str(number).zfill(2)
            # test symbol
            for symbol in symbols:
                for password in generateCandidates(
                    word, digits, symbol
                ):
                    totalAttempts += 1
                    if password == targetPassword:
                        foundPassword = True
                        print("i found it:", password)
                        return True
    return False

# stats
def displayStatistics(startTime, endTime): #https://docs.python.org/3/library/time.html
    print("unique passwords tested:", totalAttempts) #ask chatgpt how to add complexity to my program, it gave me this idea, i hated it, thank you chat
    print("time spent trying to find password:", round(endTime - startTime, 4),"secs")
    if foundPassword:
        print("success")
    else:
        print("fail")

def hybrid_password_cracking(targetPassword):
    #load dictionary
    if not loadWords():
        return
    if len(baseWords) == 0:
        print("Word not in dictionary.")
        return
    print("Running through potential password combinations.")
    # begin timer
    startTime = time.perf_counter()
    # Running analysis
    dictionaryAttack(targetPassword)
    #end timer
    endTime = time.perf_counter()
    # display run time stat
    displayStatistics(startTime, endTime)
