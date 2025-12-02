#Write a Python program that generates a password using a random combination of
#words from a dictionary file.

import random

def generate_password(dictionary_file, num_words=3):
    
    with open(dictionary_file, "r") as file:
        words = [word.strip() for word in file.readlines() if word.strip()]
    
    
    selected_words = random.sample(words, num_words)
    
   
    password = "".join(selected_words)  # or "-".join(selected_words)
    return password


dictionary = input("Enter dictionary file name: ")
num = int(input("How many words for the password? "))

password = generate_password(dictionary, num)

print("\nGenerated Password:", password)
