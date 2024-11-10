def substitution_decrypt(text, cipher_pattern):
    text = text.upper()

    decrypted_text = []

    for char in text:
        if char in cipher_pattern:
            decrypted_text.append(cipher_pattern[char])
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


print("Please input your cipher pattern as letter pairs (e.g., 'A:P'). Type 'done' when finished.")

cipher_pattern = {}

while True:
    pair = input("Enter letter pair: ").strip().upper()

    if pair == 'DONE':
        break
    key, value = pair.split(':')
    cipher_pattern[key] = value

print("Cipher pattern:", cipher_pattern)

ciphertext = input("Enter ciphertext: ")

decrypted_text = substitution_decrypt(ciphertext, cipher_pattern)

print("Decrypted text:", decrypted_text)
