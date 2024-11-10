letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def create_keyword_cipher(keyword):
    keyword = ''.join(dict.fromkeys(keyword.upper()))

    cipher = list(keyword)

    last_letter = keyword[-1]
    start_index = letters.index(last_letter) + 1

    for i in range(start_index, len(letters)):
        if letters[i] not in cipher:
            cipher.append(letters[i])

    for i in range(start_index):
        if letters[i] not in cipher:
            cipher.append(letters[i])

    cipher_dict = {letters[i]: cipher[i] for i in range(len(letters))}

    return cipher_dict


def decrypt(ciphertext, keyword):
    cipher = create_keyword_cipher(keyword)

    reverse_cipher = {v: k for k, v in cipher.items()}

    plaintext = ''.join(reverse_cipher.get(char, char) for char in ciphertext.upper())

    return plaintext


ciphertext = input("Enter the ciphertext: ")
keyword = input("Enter the possible keyword: ")
decrypted_text = decrypt(ciphertext, keyword)
print("Decrypted text:", decrypted_text)
