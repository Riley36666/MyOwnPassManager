import secrets
import string

letters = string.ascii_lowercase
caps = string.ascii_uppercase
numbers = string.digits
symbols = "!@#$%^&*"

def create_pass():
    password = []

    password += [secrets.choice(letters) for _ in range(5)]
    password += [secrets.choice(caps)]
    password += [secrets.choice(numbers)]
    password += [secrets.choice(symbols)]

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


