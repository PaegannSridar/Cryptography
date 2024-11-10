from math import gcd

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b, m=26):
    plaintext = ''
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    for char in ciphertext:
        if char.isalpha():
            x = ord(char.upper()) - ord('A')
            plain_char = (a_inv * (x - b)) % m
            plaintext += chr(plain_char + ord('A'))
        else:
            plaintext += char
    return plaintext

def affine_crack(ciphertext, m=26):
    possible_plaintexts = []
    for a in range(1, m):
        if gcd(a, m) == 1:
            for b in range(m):
                plaintext = affine_decrypt(ciphertext, a, b, m)
                if plaintext:
                    possible_plaintexts.append((a, b, plaintext))
    return possible_plaintexts

ciphertext = input("Enter ciphertext: ")

results = affine_crack(ciphertext)

for a, b, plaintext in results:
    print(f"a={a}, b={b}: {plaintext}")


