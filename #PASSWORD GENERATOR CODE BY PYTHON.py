#PASSWORD GENERATOR CODE BY PYTHON
import random
import string


def password_generator(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")
    length = int(input("Enter password length (min 8): "))
    
    if length < 8:
        print("Password length must be at least 8 characters.")
    else:
        password = password_generator(length)
        print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()