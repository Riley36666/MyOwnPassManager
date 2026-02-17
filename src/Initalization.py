from pathlib import Path

def checks():
    checkPassword()
    checkConfig()

def checkPassword():
    path = Path("passwords/password.txt")
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()

def checkConfig():
    path = Path(".env")
    path.parent.mkdir(parents=True, exist_ok=True)
    
    if not path.exists():
        path.touch()