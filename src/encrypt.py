from src.master_key import derive_key
cipher = derive_key("my_master_password")

def encrypt_pass(password: str) -> bytes:
    return cipher.encrypt(password.encode())


def decryptPass(token: bytes) -> str:
    return cipher.decrypt(token).decode()