import random
import string


def password_generator(lengthh, letters, uppercase, lowercase, digits, special_symbols):
    password = ""

    all_uppercase_letters = string.ascii_uppercase
    all_lowercase_letters = string.ascii_lowercase
    all_digits = string.digits
    all_special_symbols = string.punctuation

    index = 1

    while index <= length:
        if letters == "yes":
            if uppercase == "yes":
                password += random.choice(all_uppercase_letters)
                index += 1

            if lowercase == "yes":
                password += random.choice(all_lowercase_letters)
                index += 1

            if index > length:
                break

        if digits == "yes":
            password += random.choice(all_digits)
            index += 1

            if index > length:
                break

        if special_symbols == "yes":
            password += random.choice(all_special_symbols)
            index += 1

            if index > length:
                break

    password = ''.join(random.sample(password, len(password)))
    password = password[::-1]

    return password


username = input("Please type you username: ")
print()  # The purpose of this print is the code to look prettier

print(f"Welcome, {username}! In this app you I will generate a password based on the parameters you give me or \n"
      f"you can pick out the recommended password which will generate a strong password. It is up tp you!\n")

print("Type of passwords: \n1. Recommended \n2. Custom\n")

type_of_password = int(input("Please select one of the two options. (1 or 2): "))

length = 0
letters = ""
uppercase = ""
lowercase = ""
digits = ""
special_symbols = ""

while True:
    if type_of_password == 1:
        length = 16
        letters = "yes"
        uppercase = "yes"
        lowercase = "yes"
        digits = "yes"
        special_symbols = "yes"

    elif type_of_password == 2:
        length = int(input("Please choose the length of your password: "))
        letters = input("Do you wish your password to contain letters? (yes/no): ").lower()

        if letters == "yes":
            uppercase = input("Do you wish your password to contain uppercase letters? (yes/no): ").lower()
            lowercase = input("Do you wish your password to contain lowercase letters? (yes/no): ").lower()

        digits = input("Do you wish your password to contain digits? (yes/no): ").lower()
        special_symbols = input(
            "Do you wish your password to contain special symbols(e.g. %, &, ^,@)? (yes/no): ").lower()

    else:
        type_of_password = int(input("Invalid option! Please choose again: "))
        continue

    break

print()  # The purpose of this print is the code to look prettier
print(f"Password: {password_generator(length, letters, uppercase, lowercase, digits, special_symbols)}")
