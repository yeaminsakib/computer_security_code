letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
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
    
# def encrypt_decrypt(text ,mode ,key):
#     result = ''
#     if mode == 'd':
#         key = -key
#     for letter in text:
#         letter =letter.lower()
#         if not letter == " ":
#             index = letter.find(letter)
#             if index == -1:
#                 result += letters
#             else:
#                 new_index = index + key
#                 if new_index >= num_letters:
#                     new_index -= num_letters
#                 elif new_index < 0:
#                     new_index += num_letters 
#                 result += letters[new_index]
#     return result





print()
print("** ceaser cipher program**")
print()

print('Do you want to encrypt or decrypt?')
user_input =input('e/d' ).lower()
print()

if user_input == 'e':
    print("Encryption mode selected")
    print()
    key = int(input('enter the key (1 to 26): '))
    text = input('Enter the text you want to encrypt: ')
    ciphertext =encrypt(text, key)
    print(f'Ciphertext: {ciphertext}')

elif user_input == 'd':
    print("Decryption mode selected")
    print()
    key = int(input('enter the key (1 to 26): '))
    text = input('Enter the text you want to dencrypt: ')
    plaintext =decrypt(text, key)
    print(f'Plaintext: {plaintext}')

