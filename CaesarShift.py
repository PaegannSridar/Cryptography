

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""

    # Loop through each character in the ciphertext
    for char in ciphertext:
        if char.isupper():
            # Perform the shift with wrap-around for uppercase letters
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            # Perform the shift with wrap-around for lowercase letters
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char  # Non-letter characters remain unchanged

    return decrypted_text


def auto_decrypt_caesar_cipher(ciphertext):
    shift = 1
    while True:
        # Decrypt using the current shift (forward)
        decrypted_message_forward = decrypt_caesar_cipher(ciphertext, shift)
        print(f"Forward Shift {shift}: {decrypted_message_forward}")

        # Decrypt using the current shift (backward, which is equivalent to shifting forward by (26 - shift))
        decrypted_message_backward = decrypt_caesar_cipher(ciphertext, 26 - shift)
        print(f"Backward Shift {shift}: {decrypted_message_backward}")

        # Ask the user if either message is readable
        user_input = input("Is either message readable? (yes to stop, no to continue): ").strip().lower()
        if user_input == 'yes':
            print(f"Decryption successful with shift {shift}!")
            break

        # Increment shift and wrap around (shift can only be between 1 and 25)
        shift = (shift + 1) % 26
        if shift == 0:
            shift = 1  # Ensuring the shift never reaches 0 (since a shift of 0 means no change)


# Example usage
ciphertext = 'LYPGFFFOL'
auto_decrypt_caesar_cipher(ciphertext)

