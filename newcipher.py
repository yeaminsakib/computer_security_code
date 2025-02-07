letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter =letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
                
            else:
                new_index= index + key
                if new_index >= num_letters:
                    new_index -=num_letters
                ciphertext +=letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext +=letters[new_index]
    return plaintext


print("**Caesar cipher code**")

while True:
    print("\nDo you want to encrypt or decrypt? (e/d)")
    user_input = input().lower()

    if user_input == 'e':
        print("\nEncryption mode selected")
        key = int(input("Enter the key (1 to 26): "))
        text = input("Enter the text you want to encrypt: ")
        ciphertext = encrypt(text, key)
        print(f'Ciphertext: {ciphertext}')
    elif user_input == 'd':
        print("\nDecryption mode selected")
        key = int(input("Enter the key (1 to 26): "))
        text = input("Enter the text you want to decrypt: ")
        plaintext = decrypt(text, key)
        print(f'Plaintext: {plaintext}')
    else:
        print("Invalid input. Please enter 'e' to encrypt, 'd' to decrypt, or any other key to quit.")
        break