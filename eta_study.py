#!/usr/bin/env python3
# Eta Team - Linux Study Tutor (Study Mode + Categories Menu)

import os

# ----------------------------------------------
# Command Data
# ----------------------------------------------

commands = [
    "whoami", "cd", "ls", "ls -l", "ls -a", "clear", "man", "locate",
    "whereis", "echo", "find", "cat", "touch", "mkdir", "sudo", "nl",
    "wc", "ps", "top", "history", "grep", "cut", "chmod"
]

descriptions = [
    "Show current logged-in user.",
    "Change directory.",
    "List files and folders.",
    "Long listing format (permissions, owner, size).",
    "Show all files including hidden ones.",
    "Clear the terminal screen.",
    "Show manual help pages.",
    "Search the filesystem database.",
    "Locate binary, man page, and source.",
    "Print text or variables to screen.",
    "Search filesystem by name, type, size, etc.",
    "Display contents of a file.",
    "Create an empty file.",
    "Create a new directory.",
    "Run a command as root (superuser).",
    "Number lines in a file.",
    "Count lines, words, and characters.",
    "Show running processes.",
    "Show real-time system resource usage.",
    "Show command history.",
    "Search for text patterns in files.",
    "Cut text by delimiter and field.",
    "Change file and directory permissions."
]

examples = [
    "$ whoami",
    "$ cd /etc",
    "$ ls",
    "$ ls -l",
    "$ ls -a",
    "$ clear",
    "$ man ls",
    "$ locate passwd",
    "$ whereis python",
    "$ echo Hello World",
    "$ find / -name passwd",
    "$ cat file.txt",
    "$ touch notes.txt",
    "$ mkdir myfolder",
    "$ sudo apt update",
    "$ nl file.txt",
    "$ wc -l file.txt",
    "$ ps -aux",
    "$ top",
    "$ history",
    "$ grep hello file.txt",
    "$ cut -d: -f1 /etc/passwd",
    "$ chmod 755 script.sh"
]

# ----------------------------------------------
# Categories (by command name)
# ----------------------------------------------

categories = {
    "1": {
        "name": "Navigation & Listing",
        "commands": ["cd", "ls", "ls -l", "ls -a", "clear"]
    },
    "2": {
        "name": "Help & Search",
        "commands": ["man", "locate", "whereis", "find", "grep", "history"]
    },
    "3": {
        "name": "Files & Directories",
        "commands": ["echo", "cat", "touch", "mkdir", "nl", "wc", "cut"]
    },
    "4": {
        "name": "Processes & System Info",
        "commands": ["whoami", "ps", "top"]
    },
    "5": {
        "name": "Permissions & Admin",
        "commands": ["chmod", "sudo"]
    }
}

# ----------------------------------------------
# Helper Functions
# ----------------------------------------------

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def pause():
    input("\nPress Enter to return to menu...")

def show_command(idx: int):
    print(f"Command: {commands[idx]}")
    print(f"Description: {descriptions[idx]}")
    print(f"Example: {examples[idx]}")
    print("----------------------------------------")

# ----------------------------------------------
# Study Modes
# ----------------------------------------------

def study_all():
    clear_screen()
    print("===== Study Mode: ALL Linux Commands =====\n")
    for i in range(len(commands)):
        show_command(i)
    pause()

def study_category():
    while True:
        clear_screen()
        print("===== Study by Category =====")
        print("1) Navigation & Listing")
        print("2) Help & Search")
        print("3) Files & Directories")
        print("4) Processes & System Info")
        print("5) Permissions & Admin")
        print("6) Back to Main Menu")
        print("--------------------------------")
        choice = input("Choose a category [1-6]: ").strip()

        if choice == "6":
            break
        elif choice in categories:
            clear_screen()
            cat = categories[choice]
            print(f"===== {cat['name']} =====\n")

            # For each command in the chosen category, find its index and display it
            for cmd_name in cat["commands"]:
                if cmd_name in commands:
                    idx = commands.index(cmd_name)
                    show_command(idx)

            pause()
        else:
            print("\nInvalid choice, try again...")
            pause()

# ----------------------------------------------
# Main Menu
# ----------------------------------------------

def main_menu():
    while True:
        clear_screen()
        print("===========================================")
        print("     Linux Commands Study Tutor (Eta Team)")
        print("===========================================")
        print("1) Study ALL commands")
        print("2) Study by CATEGORY")
        print("3) Exit")
        print("-------------------------------------------")

        choice = input("Choose an option [1-3]: ").strip()

        if choice == "1":
            study_all()
        elif choice == "2":
            study_category()
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice, try again...")
            pause()

# ----------------------------------------------
# Start Program
# ----------------------------------------------

if __name__ == "__main__":
    main_menu()

