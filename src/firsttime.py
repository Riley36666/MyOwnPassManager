import os
from dotenv import load_dotenv

from src.config import changeConfig


def first_time_setup(reload_callback=None):
    load_dotenv(override=True)
    first_time = os.getenv("firstTime", "True").lower()

    if first_time == "true":
        print("⚙ First time setup detected")
        print("Running initial configuration...\n")

        # Run your interactive config
        changeConfig()

        # Mark setup complete
        update_env_value("firstTime", "False")

        print("\nSetup complete.\n")

        # Reload config in main if callback provided
        if reload_callback:
            reload_callback()


def update_env_value(key, value):
    with open(".env", "r") as file:
        lines = file.readlines()

    found = False

    with open(".env", "w") as file:
        for line in lines:
            if line.strip().startswith(key):
                file.write(f"{key}={value}\n")
                found = True
            else:
                file.write(line)

        # If key didn't exist, append it
        if not found:
            file.write(f"{key}={value}\n")


def validate_env():
    return True