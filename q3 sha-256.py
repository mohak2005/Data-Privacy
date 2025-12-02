#Write a Python program that defines a function and takes a password string as input and
#returns its SHA-256 hashed representation as a hexadecimal string.


import hashlib

def sha256_hash(password):
    
    hash_object = hashlib.sha256(password.encode())
    
    return hash_object.hexdigest()


password = input("Enter a password: ")
hashed_value = sha256_hash(password)

print("SHA-256 Hashed Password:", hashed_value)
