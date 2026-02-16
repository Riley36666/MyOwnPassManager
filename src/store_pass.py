from cryptography.fernet import Fernet
from src.encrypt import encrypt_pass, decryptPass
import pyperclip
import time

filepath = "passwords/password.txt"





def writePasstoFile(encryptedPass: bytes, website: str):
    from db.connect import add_password
    add_password(encryptedPass, website)
    with open("passwords/password.txt", "ab") as file:
        file.write(website.encode() + b":" + encryptedPass + b"\n")


def storepass(website: str, password: str) -> bool:
    if not isinstance(password, str) or not password:
        return False
    encrypted = encrypt_pass(password)
    writePasstoFile(encrypted, website)
    return True


def returnAllPasses():
    print("---------------------------------")
    print("Websites saved")
    print("---------------------------------")
    try:
        with open("passwords/password.txt", "rb") as file:
            for index, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    website, encrypted = line.split(b":", 1)
                    print(f"{index}. {website.decode()}")
                except ValueError:
                    print("Invalid line format")
    except FileNotFoundError:
        print("No passwords stored yet.")


def passes():
    try:
        with open("passwords/password.txt", "rb") as file:
            for i, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    website, _ = line.split(b":", 1)
                    print(f"{i}. {website.decode()}")
                except ValueError:
                    print(f"{i}. Invalid line format")
    except FileNotFoundError:
        print("No passwords stored yet.")


def copyPassword(index: int, clear_after: int = 10):
    try:
        entries = []
        with open("passwords/password.txt", "rb") as file:
            for line in file:
                if line.strip():
                    website, encrypted = line.strip().split(b":", 1)
                    entries.append((website.decode(), encrypted))

        website, encrypted = entries[index - 1]
        password = decryptPass(encrypted)
        pyperclip.copy(password)
        print(f"Password for {website} copied to clipboard")

        if clear_after:
            time.sleep(clear_after)
            pyperclip.copy("")  
            print("Clipboard cleared")

    except IndexError:
        print("Invalid index.")
    except FileNotFoundError:
        print("No passwords stored yet.")



