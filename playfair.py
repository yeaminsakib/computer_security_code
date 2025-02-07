import re

def generate_playfair_matrix(key):
    # Convert the key to uppercase and remove any non-alphabetic characters
    key = re.sub(r'[^A-Za-z]', '', key.upper())

    # Initialize the matrix with 'X'
    matrix = [['X' for _ in range(5)] for _ in range(5)]
    seen_letters = set()

    # Fill the matrix with the unique letters from the key
    row, col = 0, 0
    for letter in key:
        if letter not in seen_letters:
            seen_letters.add(letter)
            matrix[row][col] = letter
            col += 1
            if col == 5:
                col = 0
                row += 1

    # Fill the rest of the matrix with remaining letters (excluding 'J')
    for letter in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if letter not in seen_letters:
            matrix[row][col] = letter
            col += 1
            if col == 5:
                col = 0
                row += 1

    return matrix

def find_letter_positions(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def encrypt_playfair(plaintext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = ''

    # Preprocess plaintext by removing non-alphabetic characters and converting to uppercase
    plaintext = re.sub(r'[^A-Za-z]', '', plaintext.upper())

    # Handle consecutive identical letters by inserting 'X' between them
    i = 0
    while i < len(plaintext) - 1:
        if plaintext[i] == plaintext[i + 1]:
            plaintext = plaintext[:i + 1] + 'X' + plaintext[i + 1:]
        i += 2

    # If the plaintext length is odd, add an 'X' at the end
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    # Encrypt pairs of letters
    for i in range(0, len(plaintext), 2):
        letter1, letter2 = plaintext[i], plaintext[i + 1]

        row1, col1 = find_letter_positions(matrix, letter1)
        row2, col2 = find_letter_positions(matrix, letter2)

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        ciphertext += matrix[row1][col1] + matrix[row2][col2]

    return ciphertext

def decrypt_playfair(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ''

    # Preprocess ciphertext by removing non-alphabetic characters and converting to uppercase
    ciphertext = re.sub(r'[^A-Za-z]', '', ciphertext.upper())

    # Decrypt pairs of letters
    for i in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[i], ciphertext[i + 1]

        row1, col1 = find_letter_positions(matrix, letter1)
        row2, col2 = find_letter_positions(matrix, letter2)

        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1

        plaintext += matrix[row1][col1] + matrix[row2][col2]

    return plaintext

print("**Playfair cipher code**")

while True:
    print("\nDo you want to encrypt or decrypt? (e/d)")
    user_input = input().lower()

    if user_input == 'e':
        print("\nEncryption mode selected")
        key = input("Enter the key: ")
        text = input("Enter the text you want to encrypt: ")
        ciphertext = encrypt_playfair(text, key)
        print(f'Ciphertext: {ciphertext}')
    elif user_input == 'd':
        print("\nDecryption mode selected")
        key = input("Enter the key: ")
        text = input("Enter the text you want to decrypt: ")
        plaintext = decrypt_playfair(text, key)
        print(f'Plaintext: {plaintext}')
    else:
        print("Invalid input. Please enter 'e' to encrypt, 'd' to decrypt, or any other key to quit.")
        break
