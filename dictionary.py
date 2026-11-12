# use hashlib library 
import hashlib
# intake password
password = input("Enter password: ")
# beginning of new added section
print("Hash types: ")
print("md5")
print("sha1")
print("sha256")
print("sha512")
hash_technique = input("Enter hash type: ")
#encoding the following password
if hash_technique == "md5":
    hsh = hashlib.md5(password.encode('utf-8')).hexdigest()
elif hash_technique == "sha1":
    hsh = hashlib.sha1(password.encode('utf-8')).hexdigest()
elif hash_technique == "sha256":
    hsh = hashlib.sha256(password.encode('utf-8')).hexdigest()
elif hash_technique == "sha512":
    hsh = hashlib.sha512(password.encode('utf-8')).hexdigest()

#hsh = hashlib.md5("error01$".encode('utf-8')).hexdigest()
# rules are 5 letter word, 2 numbers, and 1 character from the following list: ! $ @
print(hsh)
#fopen dictionary text file of 300 most common 5 letter nouns
f = open("generated_passwords.txt", "r", encoding= 'iso-8859-15') 
## hasing through all the options
for line in f:
    line = line.rstrip() # removing new line character
    #decoding the following password
if hash_technique == "md5":
    hsh_test = hashlib.md5(line.encode('iso-8859-15')).hexdigest()
elif hash_technique == "sha1":
    hsh_test = hashlib.sha1(line.encode('iso-8859-15')).hexdigest()
elif hash_technique == "sha256":
    hsh_test = hashlib.sha256(line.encode('iso-8859-15')).hexdigest()
elif hash_technique == "sha512":
    hsh_test = hashlib.sha512(line.encode('iso-8859-15')).hexdigest()
    if hsh_test == hsh:
        print('Found hash for: ', line)
        print(hsh_test)
        #def hash_password(password, algorithm):

