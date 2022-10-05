import sys
import time
import sqlite3
import threading

from colorama import Fore
from modules.cmd import MyPrompt
from clear_screen import clear
from modules.flask.website import *

is_loading = True
website_thread = None



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def show_loading():
    print(Fore.RESET +
          '      _______ _______________    ' + Fore.BLUE + '   _______         ______________ _____ \n' + Fore.RESET +
          '      ___    |____  _/___    |   ' + Fore.BLUE + '   ___    |____  ________  /___(_)__  /_\n' + Fore.RESET +
          '      __  /| | __  /  __  /| |   ' + Fore.BLUE + '   __  /| |_  / / /_  __  / __  / _  __/\n' + Fore.RESET +
          '      _  ___ |__/ /   _  ___ |   ' + Fore.BLUE + '   _  ___ |/ /_/ / / /_/ /  _  /  / /_  \n' + Fore.RESET +
          '      /_/  |_|/___/   /_/  |_|   ' + Fore.BLUE + '   /_/  |_|\\__,_/  \\__,_/   /_/   \\__/  \n' + Fore.RED)
    loading_status = 0
    loading_tick = 0
    icon_states = ['\\', '|', '/', '-']
    global is_loading
    while is_loading:
        original_str = "\r[*] Starting the AIA Audit framework console ..."
        for i in range(0, len(original_str)):
            new_str = "\r"
            for k in range(0, len(original_str)):
                if k <= 4 or k >= len(original_str) - 4:
                    new_str += original_str[k]
                else:
                    if i == k:
                        if original_str[k] == " ":
                            new_str += " "
                        if original_str[i].isupper():
                            new_str += original_str[k].lower()
                        elif original_str[i].islower():
                            new_str += original_str[k].upper()
                    else:
                        new_str += original_str[k]
            new_str += icon_states[loading_status]
            sys.stdout.write(new_str)
            sys.stdout.flush()
            time.sleep(0.300)
            if loading_status == 3:
                loading_status = 0
            else:
                loading_status += 1
            loading_tick += 1
            if loading_tick > 5:
                sys.stdout.write("\r")
                sys.stdout.flush()
                is_loading = False


def start_loading():
    #Show AIA Audit loading..
    clear()
    show_loading()
    #Prepare SQLite database connection..
    con = sqlite3.connect("database.db")
    #Show welcome and show cmd prompt to the user..
    show_welcome()


def show_welcome():
    print(Fore.RESET +
          "       =[ " + Fore.RED + "AIA Audit Framework v0.1 " + Fore.RESET + "                       ]\n" +
          "+ -- --=[ 2230 exploits - 1177 auxiliary - 398 post       ]\n" +
          "+ -- --=[ 867 payloads - 45 encoders - 11 nops            ]\n" +
          "+ -- --=[ 9 evasion                                       ]\n" +
          "                                                           \n" +
          "If you need help use " + Fore.BLUE + "help" + Fore.RESET + " on the command prompt.\n")
    MyPrompt().cmdloop()

def custom_clear():
    clear()
    print(Fore.RESET +
          '      _______ _______________    ' + Fore.BLUE + '   _______         ______________ _____ \n' + Fore.RESET +
          '      ___    |____  _/___    |   ' + Fore.BLUE + '   ___    |____  ________  /___(_)__  /_\n' + Fore.RESET +
          '      __  /| | __  /  __  /| |   ' + Fore.BLUE + '   __  /| |_  / / /_  __  / __  / _  __/\n' + Fore.RESET +
          '      _  ___ |__/ /   _  ___ |   ' + Fore.BLUE + '   _  ___ |/ /_/ / / /_/ /  _  /  / /_  \n' + Fore.RESET +
          '      /_/  |_|/___/   /_/  |_|   ' + Fore.BLUE + '   /_/  |_|\\__,_/  \\__,_/   /_/   \\__/  \n' + Fore.RED)
    print(Fore.RESET +
          "       =[ " + Fore.RED + "AIA Audit Framework v0.1 " + Fore.RESET + "                       ]\n" +
          "+ -- --=[ 2230 exploits - 1177 auxiliary - 398 post       ]\n" +
          "+ -- --=[ 867 payloads - 45 encoders - 11 nops            ]\n" +
          "+ -- --=[ 9 evasion                                       ]\n" +
          "                                                           \n" +
          "If you need help use " + Fore.BLUE + "help" + Fore.RESET + " on the command prompt.\n")


if __name__ == "__main__":
    # Start Flask webserver
    website_thread = website_start()
    # Start AIA-Audit Framework
    start_loading()

