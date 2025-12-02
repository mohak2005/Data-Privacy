#Write a Python program that simulates a brute-force attack on a password by trying out
#all possible character combinations

import itertools
import string

def brute_force(target_password):
    characters = string.ascii_lowercase  # allowed characters (a–z)
    
    attempt_count = 0
    
    for length in range(1, len(target_password) + 1):
        for combo in itertools.product(characters, repeat=length):
            attempt = ''.join(combo)
            attempt_count += 1
            
            print(f"Trying: {attempt}")  

            if attempt == target_password:
                print("\nPassword FOUND!")
                print("Password:", attempt)
                print("Total attempts:", attempt_count)
                return

    print("Password not found.")


password = input("Enter password to brute-force (lowercase only): ")
brute_force(password)
