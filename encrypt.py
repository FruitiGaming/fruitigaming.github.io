#!/usr/bin/env python3

'''

The Encryptor:

Welp, it seems you have found my program {user} and please use it (if you wish)
You see, I won't regularly do update but only when neccecarry if thats alright
When encrypting your files, make sure to keep a backup of them, this program (right now) hasn't been trained to do that
Encrypting images, PDFs, disk images might not work as 
Root access may be needed for some actions but please refrain from encrypting any system files.
We WON'T be responcible for any damage towards your system.

- The developer behind it all... :)

'''

# Imports (DO NOT TOUCH BECAUSE REMOVING THEM MIGHT BREAK THE PROGRAM)

from pathlib import Path
from datetime import datetime
import os, sys
import time
import ctypes
import getpass

# Default settings:

path = ""
charecter = "█"
choice = 0
name = ""
extension = ""
replace = ""
correct = False
menus = False
arguments = ""
user = getpass.getuser()
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(SCRIPT_DIR, "LOGS", "Encrypt.log")
boot_path = os.path.join(SCRIPT_DIR, "BOOT", "BOOT.log")
root = False
allowed = True
Restricted = True
logging = True

# Section of functions:

# Other mini functions (above as functions below need it):
def press_any_key():
    if os.name == "nt":
        import msvcrt
        msvcrt.getch()
    else:
        import sys, termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

# Functions needed for startup

def boot():
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    os.system("cls" if os.name == "nt" else "clear")    
    boot_path = os.path.join(SCRIPT_DIR, "BOOT", "BOOT.log")
    try:
        with open(boot_path, "a") as f:
            f.write(" \n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] BOOT.log has started recording boot info...")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Program started\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has logged in\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user}'s operating system is {os.name}\n")
            if os.name == "posix":
                if os.getuid == 0:
                    with open(boot_path, "a") as f:
                        f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has booted with root access\n")
            if os.name == "nt":
                if ctypes.windll.shell32.IsUserAnAdmin():
                    with open(boot_path, "a") as f:
                        f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has booted with root access\n")
            else:
                f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has booted without root access\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Searching for ./Encrypt/LOGS/Encrypt.log\n")
            try:
                with open(log_path, "r") as f:
                    f.read()
                with open(boot_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] BOOT.log has found ./Encrypt/LOGS/Encrypt.log\n")
            except FileNotFoundError:
                with open(boot_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [CRITICAL] Encrypt.log is missing. Create the file or the program won't boot.\n")
        with open(boot_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] BOOT.log has finished gathering boot information. More logs are avalible at ./Encrypt/LOGS\n")
            f.write(" \n")
    except FileNotFoundError:
        os.system("cls" if os.name == "nt" else "clear")
        print("Error loading program, BOOT.log is missing, please create the file.")
        print("Press any key to continue...")
        press_any_key()
        boot()

def logs():
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    log_path = os.path.join(SCRIPT_DIR, "LOGS", "Encrypt.log")
    os.system("cls" if os.name == "nt" else "clear")
    try:
        with open(log_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] BOOT.log has finished gathering boot information. More logs are avalible at ./Encrypt/LOGS\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Program has sucesfully booted up with 0 errors.\n")
    except FileNotFoundError:
        print("Encrypt.log is missing. Please create the file and try again.")
        print("Press any key to continue...")
        press_any_key()
        boot()

def startup():
    boot()
    logs()

startup()

# Overwrite function(s):
def overwrite():
    binary = True
    path = ""
    name = ""
    extension = ""
    correct = False
    while path == "" and name == "" and extension == "" and correct == False:
        os.system("cls" if os.name == "nt" else "clear")
        path = input("Input the path of your file. Copy the FULL path: ").strip()
        name = input("Whats your file's name (without the extension): ").strip()
        extension = input("What is your file's extension (e.g txt): ").strip()
        for i in range(1,len(extension)):
            if extension[i] == ".":
                extension[i] = extension.replace(".", "")
        desicion = input(f"Are you sure you want to format the file: {name}.{extension} to {name}.{extension}.encrypted? This action cannot be undone (Y/N): ")
        if desicion.lower() == "y":
            break
        elif desicion.lower() == "n":
            exit
        else:
            continue

    try:
        file = Path(path)
        with open(path, "r") as f:
            content = f.read()

        new_content = "█" * len(content)
        file.rename(f"{name}.{extension}.encrypted")
        file_name = f"{name}.{extension}.encrypted"
        with open(file_name, "w") as f:
            f.write(new_content)
        with open(log_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has overwritten {path} with {file_name}.\n")
    except UnicodeDecodeError:
        file = Path(path)
        with open(path, "rb") as f:
            content = f.read()

        new_content = b"#" * len(content)
        file.rename(f"{name}.{extension}.encrypted")
        file_name = f"{name}.{extension}.encrypted"
        with open(path, "wb") as f:
            f.write(new_content)
        with open(log_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has overwritten {path} with {file_name}.\n")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Your file is availble at: ./Encrypt/, with the name of: {file_name}. ")
    print("Press any key to continue...")
    press_any_key()
    menu()

def overwrite_v():
    binary = True
    path = ""
    print("path = ''")
    name = ""
    print("name = ''")
    extension = ""
    print("extension = ''")
    correct = False
    print("correct = False")
    print("while path == "" and name == "" and extension == "" and correct == False:")
    while path == "" and name == "" and extension == "" and correct == False:
        os.system("cls" if os.name == "nt" else "clear")
        print("os.system('cls' if os.name == 'nt' else 'clear')")
        print("path = input('Input the path of your file. Copy the FULL path: ')")
        path = input("Input the path of your file. Copy the FULL path: ").strip()
        print("name = input('Whats your file's name (without the extension): ')")
        name = input("Whats your file's name (without the extension): ").strip()
        print("extension = input('What is your file's extension (e.g txt): ')")
        extension = input("What is your file's extension (e.g txt): ").strip()
        print("for i in range(1,len(extension)):")
        for i in range(1,len(extension)):
            print("if extension[i] == '.':")
            if extension[i] == ".":
                print("extension[i] = extension.replace('.', '')")
                extension[i] = extension.replace(".", "")
        print("desicion = input(f'Are you sure you want to format the file: (name).(extension) to (name).(extension).encrypted? This action cannot be undone (Y/N): ')")
        desicion = input(f"Are you sure you want to format the file: {name}.{extension} to {name}.{extension}.encrypted? This action cannot be undone (Y/N): ")
        if desicion.lower() == "y":
            print("if desicion.lower() == 'y':")
            print("break")
            break
        elif desicion.lower() == "n":
            print("elif desicion.lower() == 'n':")
            print("")
            print("press_any_key()")
            press_any_key()
            print("menu()")
            menu()
        else:
            print("continue")
            continue
    try:
        file = Path(path)
        with open(path, "r") as f:
            content = f.read()

        new_content = "█" * len(content)
        file.rename(f"{name}.{extension}.encrypted")
        file_name = f"{name}.{extension}.encrypted"
        with open(file_name, "w") as f:
            f.write(new_content)
        with open(log_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has overwritten {path} with {file_name}.\n")
    except UnicodeDecodeError:
        file = Path(path)
        with open(path, "rb") as f:
            content = f.read()

        new_content = b"#" * len(content)
        file.rename(f"{name}.{extension}.encrypted")
        file_name = f"{name}.{extension}.encrypted"
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Your file is availble at: ./Encrypt/, with the name of: {file_name}. ")
    print("Press any key to continue...")
    press_any_key()
    menu()

def overwrite_t():
    path = ""
    name = ""
    extension = ""
    correct = False
    while path == "" and name == "" and extension == "" and correct == False:
        os.system("cls" if os.name == "nt" else "clear")
        path = input("Input the path of your file. Copy the FULL path: ").strip()
        name = input("Whats your file's name (without the extension): ").strip()
        extension = input("What is your file's extension (e.g txt): ").strip()
        for i in range(1,len(extension)):
            if extension[i] == ".":
                extension[i] = extension.replace(".", "")
        desicion = input(f"Are you sure you want to format the file: {name}.{extension} to {name}.{extension}.encrypted? This action cannot be undone (Y/N): ")
        if desicion.lower() == "y":
            break
        elif desicion.lower() == "n":
            exit
        else:
            continue

    file_name = f"{name}.{extension}.encrypted"
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Your file is availble at: {path}, with the name of: {file_name}. ")
    print("Press any key to continue...")
    press_any_key()
    menu()

# File creation function(s):

def file_creation():
    path = input("Input the path of the folder you want your file to be created: ").strip()
    name = input("Input what you want your file to be called (without extension): ").strip()
    extension = input("What is your file's extension: ").strip()
    text = input("Enter the text you want your file to contain: ")
    file_text = "█" * len(text)
    full_path = os.path.join(path, name + extension + ".encrypted")
    try:
        with open(full_path, "x") as f:
            f.write(file_text)
        print(f"File created at the location: {full_path}")
        print("Press any key to continue...")
        press_any_key()
        menu()
    except FileExistsError:
        desicion = input(f"File already exists at the location: {full_path} (FileExistsError), you can overwrite this file. Continue? (Y/N) ")
        if desicion.lower() == "y":
            with open(full_path, "w") as f:
                f.write(file_text)
            print(f"File overwritten at the location: {full_path}")
            print("Press any key to continue...")
            press_any_key()
            menu()
        print("Press any key to continue...")
        press_any_key()
        menu()



# String coverter function(s):

def string_convert():
    convert = input("Enter a string you want converted: ")
    print("")
    result = "█" * len(convert)
    print(result)
    print("")
    print("String converted, you can copy it")
    print("Press any key to continue...")
    press_any_key()

def string_convert_v():
    convert = input("Enter a string you want converted: ")
    print("convert = input('Enter a string you want converted: ')")
    print("")
    print("print('')")
    result = "█" * len(convert)
    print("result = '█' * len(convert)")
    print("print(result)")
    print(result)
    print("")
    print('')
    print("print('String converted, you can copy it')")
    print("String converted, you can copy it")
    print("print('Press any key to continue...')")
    print("Press any key to continue")
    print("press_any_key()")
    press_any_key()

# When the choice is invalid:

def invalid():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"The choice: {choice}, is invalid. Pick from 1-4")
    print("Press any key to continue...")
    press_any_key()
    os.system("cls" if os.name == "nt" else "clear")
    menu()

def menu():
    menus = True



# End of section

if arguments == "-r":
    arguments = ""
while choice != 1 or choice != 2 or choice !=3 and menus == True:
    if os.geteuid() == 0:
        arguments = "-s"
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to the file encrypter!")
    if arguments == "-v":
        print("for i in range(1,3):")
        print("    print("")")
    for i in range(1,3):
        print("")
    if arguments == "-v":
        print("print('Pick a choice')")
    print("Pick a choice:")
    if arguments == "-v":
        print("print('1: Overwrite a file')")
    print("1: Overwrite a file")
    if arguments == "-v":
        print("print('2: Create a new file (paste text)')")
    print("2: Create a new file (paste text)")
    if arguments == "-v":
        print("print('3: Convert string')")
    print("3: Convert string")
    if arguments == "-v":
        print("print('4: Arguments')")
    print("4: Arguments")
    if arguments == "-v":
        print("print('')")
    if arguments == "-v":
        print("print('5: Admin settings (Requires root access)')")
    print("5: Admin settings (Requires root access)")
    if arguments == "-v":
        print("print('6: Quit')")
    print("6: Quit")
    print("")
    choice = input("")
    if choice == "1":
        menus = False
        with open(log_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} [IMPORTANT] has chosen to overwrite a file\n")
        os.system("cls" if os.name == "nt" else "clear")
        overwrite()
        if arguments == "-v":
            os.system("cls" if os.name == "nt" else "clear")
            print("menus = False")
            with open(log_path, "a") as f:
                f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has chosen to overwrite a file\n")
            menus = False
            os.system("cls" if os.name == "nt" else "clear")
            overwrite_v()
        elif arguments == "-x":
            os.system("cls" if os.name == "nt" else "clear")
            with open(log_path, "a") as f:
                f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has chosen to overwrite a file but couldn't continue because of safe mode\n")
            print("Safe mode is enabled: System cannot trigger this action (0xffffff)")
            os.system("cls" if os.name == "nt" else "clear")
            print("Press any key to continue...")
            press_any_key()
    elif choice == "2":
        with open(log_path, "a") as f:
                f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has chosen create a file\n")
        menus = False
        os.system("cls" if os.name == "nt" else "clear")
        file_creation()
    elif choice == "3":
        with open(log_path, "a") as f:
                f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has chosen to create a string\n")
        menus = False
        os.system("cls" if os.name == "nt" else "clear")
        string_convert()
    elif choice == "4":
        with open(log_path, "a") as f:
                f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has chosen to change arguments\n")
        choice = 0
        os.system("cls" if os.name == "nt" else "clear")
        if allowed == False:
            print("Arguments have been disabled.")
            print("Press any key to continue...")
            press_any_key()
            menu()
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("Availble arguments (used for de-bugging purposes):")
            print("1: -v Verbose mode (Shows advanced output)")
            print("2: -x Safe mode (This disables overwriting files)")
            print("3: -t Testing mode (Shows output but won't do anything)")
            print("4: -s Administrator mode (Program gains full acsess to system. May require password)")
            print("5: -r Reset arguments (Gets rid of any argument and resets the state)")
            print("")
            if arguments == "-v":
                print("Current argument applied: -v (Verbose mode)")
            elif arguments == "-x":
                print("Current argument applied: -x (Safe mode)")
            elif arguments == "-t":
                print("Current argument applied: -t (Testing mode)")
            elif arguments == "-s":
                print("Current argumet applied: -s (Admin mode)")
            elif arguments == "-r":
                print("Current argument applied: -r (Reset arguments)")
            elif arguments == "":
                print("Current argument applied: N/A")
            else:
                print(f"Current argument applied: {arguments} (Unknown argument)")
            print("")
            arguments = input("Enter an argument, only one argument can be added: ")
            if arguments == "-v":
                with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has enabled verbose mode\n")
                with open(boot_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has rebooted the program and enabled verbose mode\n")
                print("Arguments set to -v for verbose mode")
                print("Press any key to continue...")
                press_any_key()
                os.system("cls" if os.name == "nt" else "clear")
                break
            elif arguments == "-x":
                with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has enabled safe mode\n")
                with open(boot_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has rebooted the program and enabled safe mode\n")
                print("Arguments set to -x for safe mode")
                print("Press any key to continue...")
                press_any_key()
                os.system("cls" if os.name == "nt" else "clear")
                break
            elif arguments == "-t":
                with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has enabled testing mode\n")
                with open(boot_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has rebooted the program and enabled testing mode\n")
                print("Arguments set to -t for testing mode")
                print("Press any key to continue...")
                press_any_key()
                os.system("cls" if os.name == "nt" else "clear")
                break
            elif arguments == "-r":
                with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has reseted arguments\n")
                with open(boot_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has rebooted the program and reseted arguments\n")
                print("Arguments set to -r for reseting arguments")
                print("Press any key to continue...")
                press_any_key()
                os.system("cls" if os.name == "nt" else "clear")
                if os.geteuid() == 0:
                    os.execvp("", ["", "python3"] + sys.argv)
                break
            elif arguments == "-s":
                print("Arguments set to -s for admin mode")
                print("Press any key to continue...")
                press_any_key()
                os.system("cls" if os.name == "nt" else "clear")
                try:
                    if os.geteuid() != 0:
                        os.execvp("sudo", ["sudo", "python3"] + sys.argv)
                    with open(boot_path, "a") as f:
                        f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} [IMPORTANT] has rebooted the program but with root access\n")
                except AttributeError:
                    ctypes.windll.shell32.IsUserAnAdmin()
                break
            elif arguments == "":
                with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has set no arguments\n")
                with open(boot_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has rebooted the program but with no arguments\n")
                print("Arguments set to N/A")
                print("Press any key to continue...")
                press_any_key()
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [WARNING] {user} has enabled an invalid argument: {arguments}\n")
                print(f"Arguments set to {arguments} which is invalid. No changes will apply")
                print("Press any key to continue...")
                press_any_key()
                os.system("cls" if os.name == "nt" else "clear")
                break
    elif choice == "5":
        os.system("cls" if os.name == "nt" else "clear")
        try:
            if os.geteuid() != 0:
                with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} [IMPORTANT] has enabled admin mode\n")
                with open(boot_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} [IMPORTANT] has rebooted the program into admin mode\n")
                os.execvp("sudo", ["sudo", "python3"] + sys.argv)
            with open(boot_path, "a") as f:
                f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has rebooted the program but with root access\n")
        except AttributeError:
                ctypes.windll.shell32.IsUserAnAdmin()
        choice = ""
        if os.geteuid() == 0:
            root = True
        elif ctypes.windll.shell32.IsUserAnAdmin() == True:
            root = True
        else:
            root = False
        while choice != "1" or choice != "2" or choice != "3" or choice != "4" or choice != "5" and root == True:
            os.system("cls" if os.name == "nt" else "clear")
            print("Root settings:")
            print("")
            print("1. Change LOG path (may break things)")
            print("2. Change BOOT path (may break things)")
            if allowed == True:
                print("3. Disable arguments")
            else:
                print("3. Enable arguments")
            if logging == True:
                print("4. Disable logs")
            else:
                print("4. Enable logs")
            if Restricted == True:
                print("5. Disable System file protection (may break things)")
            else:
                print("5. Enable System file protection (Recommended)")
            print("")
            choice = input("")
            os.system("cls" if os.name == "nt" else "clear")
            if choice == "1":
                os.system("cls" if os.name == "nt" else "clear")
                log = input("Enter the new path for the log. ")
                log_path = log = os.path.join(SCRIPT_DIR, log)
                print("Path of log sucesfully changed for this session.")
                print("Press any key to continue...")
                press_any_key()
                menu()
                break
            elif choice == "2":
                os.system("cls" if os.name == "nt" else "clear")
                booter = input("Enter the new path for the log. ")
                boot_path = os.path.join(SCRIPT_DIR, booter)
            elif choice == "3":
                os.system("cls" if os.name == "nt" else "clear")
                if allowed == True:
                    allowed = False
                    print(f"Arguments allowed = False by {user}")
                    print("Press any key to continue...")
                    press_any_key()
                    menu()
                    break
                else:
                    allowed = True
                    print(f"Arguments allowed = True by {user}")
                    print("Press any key to continue...")
                    press_any_key()
                    menu()
                    break
            elif choice == "4":
                os.system("cls" if os.name == "nt" else "clear")
                if logging == True:
                    with open(log_path, "a") as f:
                        f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has disabled logs for this session. Goodbye for now...\n")
                    log_path = ""
                    boot_path = ""
                    logging = False
                    print(f"Logs disabled for this session by {user}")
                    print("Press any key to continue...")
                    press_any_key()
                    menu()
                    break
                else:
                    log_path = os.path.join(SCRIPT_DIR, "LOGS", "Encrypt.log")
                    boot_path = os.path.join(SCRIPT_DIR, "BOOT", "BOOT.log")
                    logging = True
                    with open(log_path, "a") as f:
                        f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has enabled logs for this session. Hello again!\n")
                    print(f"Logs enabled for this session by {user}")
                    print("Press any key to continue...")
                    press_any_key()
                    menu()
                    break
            elif choice == "5":
                os.system("cls" if os.name == "nt" else "clear")
                if Restricted == True:
                    with open(log_path, "a") as f:
                            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [WARNING] {user} is trying to disable system file protection\n")
                    desicion = input("Are you sure you want to disable system file protection? This could potentially put your computer at risk of complete loss of data. Continue? (Y/N) ")
                    if desicion.lower() == "y":
                        Restricted = False
                        with open(log_path, "a") as f:
                            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has disabled system file protection. Important files are at risk.\n")
                        print("Action completed")
                        print("Press any key to continue...")
                        press_any_key()
                        menu()
                        break
                    else:
                        with open(log_path, "a") as f:
                            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has decided not to disable system file protection\n")
                        print("Action not completed")
                        print("Press any key to continue...")
                        press_any_key()
                        menu()
                        break
                else:
                    Restricted = True
                    with open(log_path, "a") as f:
                        f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} has enabled system file protection\n")
                    print("Action completed...")
                    print("Press any key to continue")
                    press_any_key()
                    menu()
                    break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [WARNING] {user} has picked an invalid option: {choice}\n")
                print("Invalid choice!")
                print("Press any key to continue...")
                press_any_key()
                menu()
                break
    elif choice == "6":
        os.system("cls" if os.name == "nt" else "clear")
        with open(log_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] {user} is logging off\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Saving logs...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Reseting settings to default\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Cleaning session\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Reseting settings to default\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Logging out...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Finished task... BOOT logs are avalible at ./Encrypt/BOOT/BOOT.log\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Migrating logging to ./Encrypt/BOOT/BOOT.log for shutdown...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] Completed logging for this session. See you next time.\n")
            f.write(f" \n")
        with open(boot_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Stopping services...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Saving preboot orders...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Reseting argument data...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Removing root access if needed...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Clearing cache...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] Closing...\n")
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [IMPORTANT] Completed logging for this session. See you next time.\n")
            f.write(f" \n")
            exit()
    elif choice == "":
        with open(log_path, "a") as f:
                    f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {user} has picked no option\n")
        menus = False
        os.system("cls" if os.name == "nt" else "clear")
        menu()
    else:
        with open(log_path, "a") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] [WARNING] {user} has picked an invalid option: {choice}\n")
        menus = False
        os.system("cls" if os.name == "nt" else "clear")
        invalid()
menu()