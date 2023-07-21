import os
import sys
from platform import platform
from getmac import get_mac_address as gma
from colorama import Fore
import socket
import time
import shutil
import platform
#1
logoStandard = (f"""██▓███   ██░ ██  ▒█████   ▄▄▄▄    ▒█████    ██████ 
▓██░  ██▒▓██░ ██▒▒██▒  ██▒▓█████▄ ▒██▒  ██▒▒██    ▒ 
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▒██▒ ▄██▒██░  ██▒░ ▓██▄   
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▒██░█▀  ▒██   ██░  ▒   ██▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░░▓█  ▀█▓░ ████▓▒░▒██████▒▒
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ▒░▒   ░   ░ ▒ ▒░ ░ ░▒  ░ ░
░░        ░  ░░ ░░ ░ ░ ▒   ░    ░ ░ ░ ░ ▒  ░  ░  ░  
          ░  ░  ░    ░ ░   ░          ░ ░        ░  
                                ░                  """)
#2
logoLoading = (f"""██▓███   ██░ ██  ▒█████   ▄▄▄▄    ▒█████    ██████ 
▓██░  ██▒▓██░ ██▒▒██▒  ██▒▓█████▄ ▒██▒  ██▒▒██    ▒ 
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▒██▒ ▄██▒██░  ██▒░ ▓██▄   
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▒██░█▀  ▒██   ██░  ▒   ██▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░░▓█  ▀█▓░ ████▓▒░▒██████▒▒
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ▒░▒   ░   ░ ▒ ▒░ ░ ░▒  ░ ░
░░        ░  ░░ ░░ ░ ░ ▒   ░    ░ ░ ░ ░ ▒  ░  ░  ░  
          ░  ░  ░    ░ ░   ░          ░ ░        ░  
                                ░                  
                    {Fore.RED} Loading...{Fore.RESET}""")
#3
logoOsErr = (f"""██▓███   ██░ ██  ▒█████   ▄▄▄▄    ▒█████    ██████ 
▓██░  ██▒▓██░ ██▒▒██▒  ██▒▓█████▄ ▒██▒  ██▒▒██    ▒ 
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▒██▒ ▄██▒██░  ██▒░ ▓██▄   
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▒██░█▀  ▒██   ██░  ▒   ██▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░░▓█  ▀█▓░ ████▓▒░▒██████▒▒
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ▒░▒   ░   ░ ▒ ▒░ ░ ░▒  ░ ░
░░        ░  ░░ ░░ ░ ░ ▒   ░    ░ ░ ░ ░ ▒  ░  ░  ░  
          ░  ░  ░    ░ ░   ░          ░ ░        ░  
                                ░                  
{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED} You Are Using A Unsupported Operating System!{Fore.RESET}""")
             
logoExit = (f"""██▓███   ██░ ██  ▒█████   ▄▄▄▄    ▒█████    ██████ 
▓██░  ██▒▓██░ ██▒▒██▒  ██▒▓█████▄ ▒██▒  ██▒▒██    ▒ 
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▒██▒ ▄██▒██░  ██▒░ ▓██▄   
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▒██░█▀  ▒██   ██░  ▒   ██▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░░▓█  ▀█▓░ ████▓▒░▒██████▒▒
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ▒░▒   ░   ░ ▒ ▒░ ░ ░▒  ░ ░
░░        ░  ░░ ░░ ░ ░ ▒   ░    ░ ░ ░ ░ ▒  ░  ░  ░  
          ░  ░  ░    ░ ░   ░          ░ ░        ░  
                                ░                  
                    {Fore.RED} Exiting...{Fore.RESET}""")

help = (f"""{Fore.RED}╔══════════╦════════════════════════════════╗
║ Command  ║              info              ║
╠══════════╬════════════════════════════════╣
║ help     ║ Command Overview               ║
║ settings ║ Edit settings                  ║
║ start    ║ Starts the Miner               ║
║ discord  ║ Join our Discord!              ║
║ web      ║ Opens our Website              ║
║ quit     ║ Exits The Program              ║
╚══════════╩════════════════════════════════╝""")

def Help():
    os.system(clear)
    print(Fore.RED,CLogo)
    print(CHelp)
    main()
                
console_size = shutil.get_terminal_size()
logo_lines = logoStandard.split('\n')
logo_width = max(len(line) for line in logo_lines)
logo_height = len(logo_lines)
padding_vertical = (console_size.lines - logo_height) // 2
padding_horizontal = (console_size.columns - logo_width) // 2
CLogo = '\n' * padding_vertical + '\n'.join(' ' * padding_horizontal + line for line in logo_lines)

console_size = shutil.get_terminal_size()
logo_lines = logoLoading.split('\n')
logo_width = max(len(line) for line in logo_lines)
logo_height = len(logo_lines)
padding_vertical = (console_size.lines - logo_height) // 2
padding_horizontal = (console_size.columns - logo_width) // 2
CLogoLoading = '\n' * padding_vertical + '\n'.join(' ' * padding_horizontal + line for line in logo_lines)

console_size = shutil.get_terminal_size()
logo_lines = logoOsErr.split('\n')
logo_width = max(len(line) for line in logo_lines)
logo_height = len(logo_lines)
padding_vertical = (console_size.lines - logo_height) // 2
padding_horizontal = (console_size.columns - logo_width) // 2
CLogoOsErr = '\n' * padding_vertical + '\n'.join(' ' * padding_horizontal + line for line in logo_lines)

console_size = shutil.get_terminal_size()
logo_lines = help.split('\n')
logo_width = max(len(line) for line in logo_lines)
logo_height = len(logo_lines)
padding_vertical = (console_size.lines - logo_height) // 2
padding_horizontal = (console_size.columns - logo_width) // 2
CHelp = '\n' * padding_vertical + '\n'.join(' ' * padding_horizontal + line for line in logo_lines)

console_size = shutil.get_terminal_size()
logo_lines = logoExit.split('\n')
logo_width = max(len(line) for line in logo_lines)
logo_height = len(logo_lines)
padding_vertical = (console_size.lines - logo_height) // 2
padding_horizontal = (console_size.columns - logo_width) // 2
CLogoExit = '\n' * padding_vertical + '\n'.join(' ' * padding_horizontal + line for line in logo_lines)

if platform.system() == 'Windows':
    clear = 'cls'
else:
    print(Fore.RED,CLogoOsErr)
    time.sleep(3)
    os.exit()
 
os.system(clear)
print(Fore.RED,CLogoLoading)
time.sleep(2)
os.system(clear)
print(Fore.RED,CLogo)
def main():
    print(f"{Fore.RED}")
    command = input(f"{socket.gethostname()}:~/Phobos> {Fore.RESET}")
    if command == "help":
        Help()
    elif command == "example":
        os.system(clear)
        print(Fore.RED,CLogo)
        print(Fore.RED,"Please Enter Your Discord Webhook.")
        webhook = input(f"{socket.gethostname()}:~/Phobos/example> {Fore.RESET}")
    elif command == "quit":
        os.system(clear)
        print(Fore.RED,CLogoExit)
        time.sleep(3)
        os.system(clear)
        sys.exit()
    else:
        print(Fore.RED,command,"Is Not A Valid Command, Try Running The 'help' Command.")
        main()

main()
    



