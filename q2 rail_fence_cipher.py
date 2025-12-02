#Write a program to perform encryption and decryption using Rail Fence Cipher
#(transpositional cipher)

def encrypt_rail_fence(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    
    direction_down = False
    row, col = 0, 0

    for ch in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        
        rail[row][col] = ch
        col += 1

        row = row + 1 if direction_down else row - 1

    result = ""
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]
    return result



def decrypt_rail_fence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]

    direction_down = None
    row, col = 0, 0

    # Mark the zig-zag positions
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        
        rail[row][col] = '*'
        col += 1

        row = row + 1 if direction_down else row - 1

    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    
    result = ""
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        
        result += rail[row][col]
        col += 1

        row = row + 1 if direction_down else row - 1

    return result



print("=== Rail Fence Cipher Encryption & Decryption ===")
text = input("Enter text: ")
key = int(input("Enter key (number of rails): "))

encrypted = encrypt_rail_fence(text, key)
print("\nEncrypted Text:", encrypted)

decrypted = decrypt_rail_fence(encrypted, key)
print("Decrypted Text:", decrypted)
