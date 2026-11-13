# use hashlib library 
import hashlib
import time
# FIX DISPLAY STATISTICS LATER
def displayStatistics(startTime, endTime): #https://docs.python.org/3/library/time.html
    print("unique passwords tested:", totalAttempts) #ask chatgpt how to add complexity to my program, it gave me this idea, i hated it, thank you chat
    print("time spent trying to find password:", round(endTime - startTime, 4),"secs")
    if foundPassword:
        print("success")
    else:
        print("fail")

def dictionary_password_cracking(password): #intake password from main interface
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
    f = open("dictionary_passwords.txt", "r", encoding= 'iso-8859-15') 
    ## hasing through all the options
    # setting hsh_test value
    hsh_test_md5 = "HelloWorld"
    hsh_test_sha1 = "HelloWorld"
    hsh_test_sha256 = "HelloWorld"
    hsh_test_sha512 = "HelloWorld"
    # begin timer
    startTime = time.perf_counter()
    for line in f:
        line = line.rstrip() # removing new line character
        #encoding the following password
        while hsh not in [hsh_test_md5, hsh_test_sha1, hsh_test_sha256, hsh_test_sha512]:
            hsh_test_md5 = hashlib.md5(line.encode('iso-8859-15')).hexdigest()
            # comparing password and test password from dictionary
            if hsh == hsh_test_md5: 
                #end timer
                endTime = time.perf_counter()
                print("Password cracked using md5 method: ", line)
                #stats
                displayStatistics(startTime, endTime)
                return
            hsh_test_sha1 = hashlib.sha1(line.encode('iso-8859-15')).hexdigest()
            # comparing password and test password from dictionary
            if hsh == hsh_test_sha1: 
                #end timer
                endTime = time.perf_counter()
                print("Password cracked using sha1 method: ", line)
                #stats
                displayStatistics(startTime, endTime)
                return
            hsh_test_sha256 = hashlib.sha256(line.encode('iso-8859-15')).hexdigest()
            # comparing password and test password from dictionary
            if hsh == hsh_test_sha256: 
                #end timer
                endTime = time.perf_counter()
                print("Password cracked using sha256 method: ", line)
                #stats
                displayStatistics(startTime, endTime)
                return
            hsh_test_sha512 = hashlib.sha512(line.encode('iso-8859-15')).hexdigest()
            # comparing password and test password from dictionary
            if hsh == hsh_test_sha512: 
                #end timer
                endTime = time.perf_counter()
                print("Password cracked using sha512 method: ", line)
                #stats
                displayStatistics(startTime, endTime)
                return
