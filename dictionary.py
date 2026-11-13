# use hashlib library 
import hashlib
import time

totalAttempts = 0
foundPassword = False

def displayStatistics(startTime, endTime): # [r2]
    print("unique passwords tested:", totalAttempts) 
    print("time spent trying to find password:", round(endTime - startTime, 4),"secs")
    if foundPassword:
        print("success")
    else:
        print("fail")

def dictionary_password_cracking(password): #intake password from main interface
    global foundPassword, totalAttempts
    # user selects desired hash technique
    print("Hash technique: ")
    print("md5")
    print("sha1")
    print("sha256")
    print("sha512")
    hash_technique = input("Enter desired hash technique: ")
    while hash_technique not in ["md5", "sha1", "sha256", "sha512"]:
        print("Invalid hash technique. Please try again.")
        hash_technique = input("Enter desired hash technique: ")
    # encoding the password using selected hash technique
    if hash_technique == "md5":
        hsh = hashlib.md5(password.encode('utf-8')).hexdigest()
    elif hash_technique == "sha1":
        hsh = hashlib.sha1(password.encode('utf-8')).hexdigest()
    elif hash_technique == "sha256":
        hsh = hashlib.sha256(password.encode('utf-8')).hexdigest()
    elif hash_technique == "sha512":
        hsh = hashlib.sha512(password.encode('utf-8')).hexdigest()
    print(hsh) # printing the generated hash
    #opening file of 300 most common 5 letter nouns and possible password combinations
    f = open("dictionary_passwords.txt", "r", encoding= 'utf-8') 
    # begin timer
    startTime = time.perf_counter()
    # hasing through all the options
    for line in f:
        line = line.rstrip() # removing new line character
        #encoding the following password

        hsh_test_md5 = hashlib.md5(line.encode('utf-8')).hexdigest()
        # comparing password and test password from dictionary
        if hsh == hsh_test_md5: 
            #end timer
            endTime = time.perf_counter()
            print("Password cracked using md5 method: ", line)
            #stats
            foundPassword = True
            totalAttempts = totalAttempts + 1
            displayStatistics(startTime, endTime)
            return
        hsh_test_sha1 = hashlib.sha1(line.encode('utf-8')).hexdigest()
        # comparing password and test password from dictionary
        if hsh == hsh_test_sha1: 
            #end timer
            endTime = time.perf_counter()
            print("Password cracked using sha1 method: ", line)
            #stats
            foundPassword = True
            totalAttempts = totalAttempts + 2
            displayStatistics(startTime, endTime)
            return
        hsh_test_sha256 = hashlib.sha256(line.encode('utf-8')).hexdigest()
        # comparing password and test password from dictionary
        if hsh == hsh_test_sha256: 
            #end timer
            endTime = time.perf_counter()
            print("Password cracked using sha256 method: ", line)
            #stats
            foundPassword = True
            totalAttempts = totalAttempts + 3
            displayStatistics(startTime, endTime)
            return
        hsh_test_sha512 = hashlib.sha512(line.encode('utf-8')).hexdigest()
        # comparing password and test password from dictionary
        if hsh == hsh_test_sha512: 
            #end timer
            endTime = time.perf_counter()
            print("Password cracked using sha512 method: ", line)
            #stats
            foundPassword = True
            totalAttempts = totalAttempts + 4
            displayStatistics(startTime, endTime)
            return
        totalAttempts = totalAttempts + 4
    if foundPassword == True:
        return
    else:
        print("Password not found using dictionary method")
        #end timer
        endTime = time.perf_counter()
        displayStatistics(startTime, endTime)
        return

