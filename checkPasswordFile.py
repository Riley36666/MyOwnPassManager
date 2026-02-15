from pathlib import Path

def check():
    path = Path("passwords/password.txt")
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()
