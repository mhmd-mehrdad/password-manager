# 🔐 Password Manager

A desktop password manager built with Python and Tkinter. The application allows users to generate strong passwords, save login credentials, and retrieve stored account information through a simple graphical interface.

## Features

- **Password Generation:** Generate random passwords containing letters, numbers, and symbols.
- **Credential Storage:** Save website names, email addresses, and passwords in a JSON file.
- **Password Search:** Retrieve previously saved credentials by website name.
- **Clipboard Integration:** Automatically copy generated passwords to the clipboard.
- **Input Validation:** Prevent saving incomplete entries.
- **Error Handling:** Handle missing files and unsuccessful searches.

## Technologies Used

- **Python** — Core application logic
- **Tkinter** — Graphical user interface (GUI)
- **JSON** — Local credential storage
- **Pyperclip** — Clipboard functionality
- **Random** — Password generation

## Installation and Usage

**1. Clone the repository:**

```bash
git clone https://github.com/mhmd-mehrdad/password-manager.git
cd password-manager
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

**3. Run the application:**

```bash
python main.py
```

## Project Structure

```text
password-manager/
├── main.py
├── logo.png
├── requirements.txt
├── .gitignore
└── README.md
```

The application creates a local `data.json` file to store credentials. This file is excluded from version control.

## What I Learned

Through this project, I practiced:

- Building desktop applications with Tkinter.
- Working with JSON files for persistent data storage.
- Implementing exception handling using `try`, `except`, and `else`.
- Using external Python libraries.
- Organizing application logic into reusable functions.
- Handling user input and displaying feedback through a GUI.

## Security Notice

**This project is intended for educational purposes only.**

Passwords are stored locally in plain text within a JSON file without encryption. Therefore, this application should not be used to store real or sensitive credentials.
