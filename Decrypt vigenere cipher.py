def vigenere_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper().replace(" ", "")
    keyword = keyword.upper()
    decrypted_text = []

    for i, char in enumerate(ciphertext):
        key_char = keyword[i % len(keyword)]
        shift = ord(key_char) - ord('A')

        decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)

ciphertext = input("Enter ciphertext: ")
keyword = input("Enter keyword: ")
decrypted_text = vigenere_decrypt(ciphertext, keyword)
print("Decrypted Text:", decrypted_text)
