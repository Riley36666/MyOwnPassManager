import threading
import time
from dotenv import load_dotenv
import os
import sys


from src.store_pass import storepass, returnAllPasses, passes, copyPassword, deletePassFromFile, deleteAll
from src.passwordGenerator import create_pass
from src.System_info import getMACaddress
from src.webcall import webcall
from src.checkPasswordFile import check
from db.connect import get_password_for_website

website_online = None
running = True
load_dotenv()

websiteurl = os.getenv("WEBAPIURL")

def use_mac_check():
    """Return True if MAC-based 2FA is enabled and the MAC matches"""
    allowed_mac = os.getenv("MAC_ADDRESS", "").lower().replace("-", ":")
    current_mac = getMACaddress()
    useMAC = os.getenv("useMACaddress").lower()
    if useMAC == "false":
        return False
    
    if not current_mac:
        print("Could not retrieve MAC address")
        return False

    current_mac = current_mac.lower().replace("-", ":")
    if allowed_mac == current_mac:
        #print("Using MAC Address 2FA")
        return True
    else:
        #print(f"MAC address does not match (current: {current_mac}, allowed: {allowed_mac})")
        return False

def checkPassFile():
    check()

def deleteAllPass():
    deleteAll()
    print("All passwords have been cleared.")


def passwordGen():
    print("What website is the password for?")
    website = input()
    password = create_pass()
    if storepass(website, password):
        print("Password successfully stored!")
    else:
        print("Password failed to store.")
def check_website_background():
    """Update global website_online with actual status"""
    global website_online
    print("Using Website based 2fa")
    website_online = webcall(websiteurl)


def wait_for_website_check():
    """Start background thread and wait until website_online is set"""
    global website_online
    global running
    thread = threading.Thread(target=check_website_background, daemon=True)
    thread.start()
    while website_online is None:
        print("Checking website status... please wait.")
        time.sleep(0.5)
    if website_online is False:
        print("Program failed to find website/website was down")
        thread.join()
        running = False


def storingaPass():
    website = input("What is the website for the pass?\n")
    newpass = input("What is the password for the website?\n")
    
    if storepass(newpass, website):
        print("Pass successfully stored")
    else:
        print("Pass failed to be stored")

def deletePass():
    passes()
    choice = int(input("Write the number for password to be deleted\n"))
    deletePassFromFile(choice)

def getIndvidialPass():
    global running
    passes()
    choice = int(input("Write the number for password to be copied to clipboard\n"))
    copyPassword(choice)
    running = False


def getallPass():
    global running
    returnAllPasses()
    running = False


def main():
    global running

    while running:
        print("\n1. Store new password")
        print("2. Get all passwords")
        print("3. Get indivial passwords by websites")
        print("4. Create a random password")
        print("5. Delete a current saved password")
        print("6. Exit")

        option = int(input())

        if website_online is None:
            wait_for_website_check()

        if website_online:
            if option == 1:
                storingaPass()
            elif option == 2:
                returnAllPasses()
            elif option == 3:
                getIndvidialPass()
            elif option == 4:
                passwordGen()
            elif option == 5:
                deletePass()
            elif option == 6:
                running = False
            else:
                print("Wrong option")
        else:
            print("Website is down therefore 2FA isn't complete")


if __name__ == "__main__":
    # 2FA checks
    if use_mac_check():
        website_online = True
    else:
        wait_for_website_check()

    checkPassFile()

    if len(sys.argv) == 1:
        main()
        sys.exit()

    command = sys.argv[1].lower()

    if command == "add":
        storingaPass()

    elif command == "list":
        getallPass()

    elif command == "copy":
        if len(sys.argv) < 3:
            print("Usage: passman copy <index>")
        else:
            copyPassword(int(sys.argv[2]))

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: passman delete <index>")
        else:
            deletePassFromFile(int(sys.argv[2]))
    elif command == "deleteall":
        if len(sys.argv) < 2:
            print("Usage: passman deleteall")
        else:
            deleteAllPass()
    elif command in ["help", "-h", "--help"]:
        print("""
    PassMan CLI Commands:
    add               Add a new password
    list              Show all saved passwords
    copy <index>      Copy password to clipboard
    delete <index>    Delete a password
    generate          Generate a random password
    help              Show this help message
    """)
    elif command == "generate":
        passwordGen()

    else:
        print(f"Unknown command: {command}")
