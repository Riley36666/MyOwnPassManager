from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from src.store_pass import decryptPass
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("mongodburl"))
db = client["PasswordManager"]
passwords = db["Passwords"]


def add_password(website: str, password: bytes) -> bool:
    try:
        passwords.insert_one({
            "Website": website,
            "Password": password
        })
        return True
    except DuplicateKeyError:
        return False

def get_all_passwords():
    return list(passwords.find({}, {"_id": 0}))  # exclude MongoDB _id


def get_password_for_website(website):
    doc = passwords.find_one({"Website": website}, {"_id": 0})
    if doc:
        return decryptPass(doc["Password"])
    return None


