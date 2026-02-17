from dotenv import load_dotenv
from src.System_info import getMACaddress
import os
load_dotenv()

def set_env_var(key, value):
    lines = []
    found = False

    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                if line.startswith(f"{key}="):
                    lines.append(f"{key}={value}\n")
                    found = True
                else:
                    lines.append(line)

    if not found:
        lines.append(f"{key}={value}\n")

    with open(".env", "w") as f:
        f.writelines(lines)

def changeConfig():
    print("Do you want 2FA through MAC address? (yes/no)")
    useMAC = input().strip().lower()

    if useMAC in ("true", "yes"):
        mac = getMACaddress()
        set_env_var("useMACaddress", "true")
        set_env_var("MAC_ADDRESS", mac)
        set_env_var("WEBAPIURL", "")
    else:
        print("What is the API URL?")
        weburl = input().strip()
        set_env_var("useMACaddress", "false")
        set_env_var("WEBAPIURL", weburl)
        set_env_var("MAC_ADDRESS", "")

    print("Config updated.")
    
