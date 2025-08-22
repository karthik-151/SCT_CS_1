def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # check if character is alphabet
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # keep spaces/symbols unchanged
    return result


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


# Main program
if __name__ == "__main__":
    print("===== Caesar Cipher Program =====")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    encrypted = caesar_cipher_encrypt(message, shift)
    decrypted = caesar_cipher_decrypt(encrypted, shift)

    print(f"\n🔐 Encrypted Message: {encrypted}")
    print(f"🔓 Decrypted Message: {decrypted}")
