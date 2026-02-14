import os
import base64
import hashlib
from cryptography.fernet import Fernet

SALT_FILE = "salt.bin"
ITERATIONS = 200_000


def load_or_create_salt() -> bytes:
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()

    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)
    return salt


def derive_key(master_password: str) -> Fernet:
    salt = load_or_create_salt()

    raw_key = hashlib.pbkdf2_hmac(
        "sha256",
        master_password.encode(),
        salt,
        ITERATIONS,
        dklen=32
    )

    key = base64.urlsafe_b64encode(raw_key)
    return Fernet(key)
