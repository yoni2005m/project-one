import string
import random

def generate_password(length=12, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''

    all_chars = letters + digits + special
    if not all_chars:
        raise ValueError("No character sets selected.")

    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    print("Welcome to the Password Generator")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        include_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
        include_special = input("Include special characters? (y/n, default y): ").lower() != 'n'

        password = generate_password(length, include_digits, include_special)
        print(f"\nYour password: {password}")
    except ValueError as ve:
        print("Error:", ve)
