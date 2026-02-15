# 🔐 MyOwnPassManager

A secure, command-line password manager built with Python that keeps your credentials encrypted and safe. Features master password protection, encrypted storage, and a unique remote 2FA availability check.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Security](https://img.shields.io/badge/security-encrypted-brightgreen)]()

## ✨ Features

- **🔒 Master Password Protection** - Single master key to access all your passwords
- **🛡️ AES Encryption** - All passwords stored securely using Fernet (symmetric encryption)
- **🌐 Remote 2FA Status** - Unique feature to check service availability before attempting login
- **💻 Simple CLI Interface** - Easy-to-use command line interface
- **📦 Lightweight** - Minimal dependencies, runs anywhere Python is installed

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   - git clone https://github.com/Riley36666/MyOwnPassManager.git
   - cd MyOwnPassManager
2. **Install dependencies**
    - pip install -r requirements.txt
3. **Run the script**
    - python main.py
4. **Optional built into .exe**
    - python -m PyInstaller --onefile --windowed --icon=images/icon.ico --add-data ".env;." main.py
