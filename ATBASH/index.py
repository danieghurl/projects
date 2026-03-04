import string
import hashlib
import re

# User Data Storage (simulated with a dictionary for simplicity)
users_db = {}
login_attempts = {}

# Registration Function
def register_user():
    print("\n=== User Registration ===")
    while True:
        username = input("Enter a username (at least 6 characters): ")
        if len(username) < 6:
            print("Username must be at least 6 characters long.")
            continue
        if username in users_db:
            print("Username already exists. Choose another.")
            continue
        break

    while True:
        password = input("Enter a strong password (at least 8 characters with letters, numbers, and special characters): ")
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password) or not re.search(r"[!@#$%^&*]", password):
            print("Password must include letters, numbers, and special characters.")
            continue
        break

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users_db[username] = hashed_password
    login_attempts[username] = 0
    print("User registered successfully!\n")

# Login Function
def login_user():
    print("\n=== User Login ===")
    for _ in range(3):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if username in users_db and users_db[username] == hashed_password:
            print("Login successful!\n")
            return username
        else:
            print("Invalid credentials. Try again.")
            if username in login_attempts:
                login_attempts[username] += 1
                if login_attempts[username] >= 3:
                    print(f"User '{username}' is blocked due to multiple failed login attempts.")
                    return None
    return None

# Atbash Cipher
def atbash_cipher(text):
    alphabet = string.ascii_uppercase
    atbash_dict = {alphabet[i]: alphabet[-(i + 1)] for i in range(len(alphabet))}
    return "".join([atbash_dict.get(char.upper(), char) for char in text])

# Caesar Cipher
def caesar_cipher(text, shift, mode="encrypt"):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr((ord(char.upper()) - 65 + shift_amount) % 26 + 65)
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)

# Vigenere Cipher
def vigenere_cipher(text, keyword, mode="encrypt"):
    keyword = keyword.upper()
    result = []
    keyword_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - 65
            if mode == "decrypt":
                shift = -shift
            new_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            result.append(new_char)
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            result.append(char)
    return "".join(result)

# Main Application
def main():
    print("=== Welcome to the Encryption Application ===")
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            username = login_user()
            if username:
                print("\n=== Encryption / Decryption Options ===")
                print("1. Atbash Cipher\n2. Caesar Cipher\n3. Vigenere Cipher\n4. Logout")
                while True:
                    cipher_choice = input("Choose a cipher: ")
                    if cipher_choice == '1':
                        text = input("Enter text for Atbash Cipher: ")
                        print("Atbash Cipher Result:", atbash_cipher(text))
                    elif cipher_choice == '2':
                        text = input("Enter text for Caesar Cipher: ")
                        shift = int(input("Enter shift value: "))
                        print("Caesar Cipher Encrypted:", caesar_cipher(text, shift))
                        print("Caesar Cipher Decrypted:", caesar_cipher(text, shift, mode="decrypt"))
                    elif cipher_choice == '3':
                        text = input("Enter text for Vigenere Cipher: ")
                        keyword = input("Enter keyword: ")
                        print("Vigenere Cipher Encrypted:", vigenere_cipher(text, keyword))
                        print("Vigenere Cipher Decrypted:", vigenere_cipher(text, keyword, mode="decrypt"))
                    elif cipher_choice == '4':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Try again.")
            else:
                print("Returning to main menu.")
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the application
if __name__ == "__main__":
    main()
