# use hashlib library 
import hashlib
def dictionary_password_cracking(password): #intake password from main interface
# user selects desired hash technique
    print("Hash technique: ")
    print("md5")
    print("sha1")
    print("sha256")
    print("sha512")
    hash_technique = input("Enter desired hash technique: ")
    # while hash_technique != "md5" or "sha1" or "sha256" or "sha512":
    #     print("Invalid hash technique. Please try again.")
    #     hash_technique = input("Enter desired hash technique: ")
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
    for line in f:
        line = line.rstrip() # removing new line character
    #encoding the following password
    if hash_technique == "md5":
        hsh_test = hashlib.md5(line.encode('iso-8859-15')).hexdigest()
    elif hash_technique == "sha1":
        hsh_test = hashlib.sha1(line.encode('iso-8859-15')).hexdigest()
    elif hash_technique == "sha256":
        hsh_test = hashlib.sha256(line.encode('iso-8859-15')).hexdigest()
    elif hash_technique == "sha512":
        hsh_test = hashlib.sha512(line.encode('iso-8859-15')).hexdigest()
    # comparing password and test password from dictionary
    if hsh_test == hsh:
        print('Found hash for: ', line)
        print(hsh_test)
