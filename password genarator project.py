import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for your password: "))
        if length <= 0:
            print("Please enter a valid positive integer for password length.")
            return

        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
