# src/buttonFunctions.py

def storeButton(main_window):
    """
    Called when user presses 'Store a New Password'
    """
    if hasattr(main_window, "show_store_screen"):
        main_window.show_store_screen()


def allPassButton(main_window):
    """
    Called when user presses 'Display All Passwords'
    """
    print("Display all passwords not implemented yet")


def genPass(main_window):
    """
    Called when user presses 'Generate New Password'
    """
    print("Generate password not implemented yet")


def deletePass(main_window):
    """
    Called when user presses 'Delete Saved Password'
    """
    print("Delete password not implemented yet")
