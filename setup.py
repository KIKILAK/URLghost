import os

system = input("Select your operating system (1.- Windows, 2.- Linux/Termux) $ ")

if system == '1':
    os.system("@echo off")
    os.system("color 0a")
    os.system("cls")
    print("[+] Installing requirements...")
    print("\n")
    os.system("pip install -r requirements.txt")

elif system == '2':
    
    print("[+] Installing requirements...")
    print("\n")
    os.system("pip install -r requirements.txt")

else:
    print("Invalid option, QUITTING!")
    quit()