import random

try:
    password_length = int(input("Enter the length of the password: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid integer value.")
    exit()

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$*?"

try:
    password = "".join(random.sample(characters, password_length))
except ValueError:
    print("Error: Password length is too long. Please enter a valid length.")
    exit()

print("Your random password is:", password)


