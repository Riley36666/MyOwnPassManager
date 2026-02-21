# 🔐 MyOwnPassManager

A secure, lightweight command-line password manager built with Python.  
Passwords are encrypted using symmetric encryption and protected by a master authentication system with optional environment-based access verification.
**This project is for educational purposes and not intended for production use. The README was written with the assistance of AI.**

---

## ✨ Features

- 🔒 **Master Password Protection** – Secure access control before vault access  
- 🛡️ **Encrypted Storage (Fernet / AES)** – All credentials are encrypted before storage  
- 🌐 **Environment-Based Access Verification** – Optional MAC address validation or remote API availability check  
- 💻 **Command Line Interface** – Fast, minimal, and efficient workflow  
- 📦 **Lightweight & Portable** – Runs anywhere Python 3.6+ is installed  
- 🗄️ **MongoDB Support** – Secure database-backed storage  

---
## 🏗 Architecture

The project follows a modular architecture:

- **CLI Layer** → Handles user input and command routing  
- **Core Logic Layer** → Encryption, password generation, storage management  
- **Persistence Layer** → Local file storage or MongoDB backend  
- **Security Layer** → Master password validation + environment verification  

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

### Create a `.env` file (or edit `.env.production` for deployment):

```bash 
useMACaddress=true
MAC_ADDRESS=00:00:00:00:00:00
WEBAPIURL=https://your-api-endpoint/api/websitecheck
mongodburl=your-mongodb-connection-string
useDB=true|false
```

> **Note:** `Setup.bat` adds the CLI to PATH (Windows only).

### Example usages

```
passman help
passman list
passman copy <index>
passman add
passman add <website> <password>
passman gen  
```
---
## 🧪 Testing

The project includes unit tests for:
- Encryption/decryption integrity
- Password storage logic
- Deletion behaviour
- Update checks

Run tests with:
```
python -m pytest
```
---

## 🎯 Project Goals

- Learn secure credential handling
- Practice modular Python design
- Explore encryption and environment-based security checks