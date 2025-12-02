#Write a Python program that reads a file containing a list of usernames and passwords,
#one pair per line (separated by a comma). It checks each password to see if it has been
#leaked in a data breach. You can use the "Have I Been Pwned" API
#(https://haveibeenpwned.com/API/v3) to check if a password has been leaked.

import hashlib
import requests


def check_password_pwned(password):
    """
    Checks if a password has been leaked using the Have I Been Pwned API (k-anonymity model)
    Returns: number of times leaked (int)
    """
   
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()

    
    prefix = sha1[:5]
    suffix = sha1[5:]

    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from HIBP API")
        return -1

   
    hashes = response.text.splitlines()
    for line in hashes:
        h, count = line.split(":")
        if h == suffix:
            return int(count)

    return 0  

filename = input("Enter filename containing username-password pairs: ")

try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            username, password = line.split(",")

            leaked_count = check_password_pwned(password)

            if leaked_count > 0:
                print(f"[LEAKED] User: {username} | Password leaked {leaked_count} times!")
            else:
                print(f"[SAFE]   User: {username} | Password NOT found in breaches.")

except FileNotFoundError:
    print("Error: File not found!")
