import string
import random

charactor=list(string.ascii_letters + string.digits + "!@#$%^&*()?)")

def generate_password():
    password_length = int(input("how long would you like your password to be?\n:-"))
    print("Your password is:- ")

    random.shuffle(charactor)

    password = []

    for x in range(password_length):
        password.append(random.choice(charactor))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password?\n(Yes/No):")

if option == "yes":
    generate_password()
elif option == "No":
    print("Okay program ended:")
else:
    print("Invalid input , please enter Yes or No")
    quit()
