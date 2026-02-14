import threading

from store_pass import storepass 
from store_pass import returnAllPasses
from store_pass import passes
from store_pass import copyPassword
from webcall import webcall

website_online = None
running = True

def webcheck():
    return webcall()


def storingaPass():
    website = input("What is the website for the pass?\n")
    newpass = input("What is the password for the website?\n")
    
    if storepass(newpass, website) == True:
        print("Pass successfully stored")
    else:
        print("Pass failed to be stored")

def check_website_background():
    global website_online
    website_online = webcall()

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
    print("1. Store new password")
    print("2. Get all passwords")
    print("3. Get indivial passwords by websites")
    print("4. Exit")

    option = int(input())

    if website_online is None:
        print("Checking website status... please wait.")
        return

    if website_online:
        if option == 1:
            storingaPass()
        elif option == 2:
            returnAllPasses()
        elif option == 3:
            getIndvidialPass()
        elif option == 4:
            running = False
        else:
            print("Wrong option")
    else:
        print("Website is down therefore 2fa isn't complete")


if __name__ == "__main__":
    threading.Thread(target=check_website_background, daemon=True).start()
    main()
