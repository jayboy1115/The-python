import random
import string


def generate_password(length=16):
    if not isinstance(length, int) or length < 1:
        raise ValueError("Password length must be a positive integer")

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(characters, k=length))

    while not (any(c.isupper() for c in password)
               and any(c.islower() for c in password)
               and any(c.isdigit() for c in password)
               and any(c in string.punctuation for c in password)):
        password = ''.join(random.choices(characters, k=length))

    return password

def main():
    print("Password Generator")
    print("------------------")
    print(f"Generated Password: {generate_password(16)}")

if __name__ == "__main__":
    main()
