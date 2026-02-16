# 🔐 MyOwnPassManager

A secure, lightweight command-line password manager built with Python.  
Passwords are encrypted using symmetric encryption and protected by a master authentication system with environment-based access verification.
**This project is for educational purposes and not intended for production use.**

---

## ✨ Features

- 🔒 **Master Password Protection** – Secure access control before vault access  
- 🛡️ **Encrypted Storage (Fernet / AES)** – All credentials are encrypted before storage  
- 🌐 **Environment-Based Access Verification** – Optional MAC address validation or remote API availability check  
- 💻 **Command Line Interface** – Fast, minimal, and efficient workflow  
- 📦 **Lightweight & Portable** – Runs anywhere Python 3.6+ is installed  
- 🗄️ **MongoDB Support** – Secure database-backed storage  

---

## 🛠 Tech Stack

- Python 3.6+
- cryptography (Fernet encryption)
- python-dotenv
- MongoDB
- threading
- requests (for remote availability check)

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Riley36666/MyOwnPassManager.git
cd MyOwnPassManager
pip install -r requirements.txt
```

### Create a .env / edit the .env.production

```bash 
useMACaddress=true
MAC_ADDRESS=00:00:00:00:00:00
WEBAPIURL=https://your-api-endpoint/api/websitecheck
mongodburl=your-mongodb-connection-string
useDB=true|false
```

Make the CLI work globally run **Setup.bat**