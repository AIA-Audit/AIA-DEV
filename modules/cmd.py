import __main__
import cmd
import time
from colorama import Fore
from beaupy.spinners import *
from modules.scanner.configure import Configure


class MyPrompt(cmd.Cmd):

    prompt = 'AIAConsole ' + Fore.BLUE + '>' + Fore.RESET + " "
    doc_header = 'Showing AIA Audit console commands. Use help [command]:'
    ruler = Fore.LIGHTBLACK_EX + '-' + Fore.RESET

    def default(self, line):
        return print('Unknown command, use help for more information')

    def do_audit(self, args):
        "Use 'audit [full/custom] to start an audit'"
        if args == "full":
            print("Full audit here")
        elif args == "custom":
            print(" ")
            print("Select the modules you want to use for the audit")
            items = Configure().main()
            __main__.custom_clear()
            print(" ")
            spinner_animation = ['🖥💣    🏢️ ', '🖥 💣   🏢️️ ', '🖥  💣  🏢️️ ', '🖥   💣 🏢️️ ', '🖥    💣🏢️️ ']
            spinner = Spinner(spinner_animation, "Starting the auditory..")
            spinner.start()

            time.sleep(10)

            spinner.stop()
            for item in items:
                print(item)
            #self.postloop()
        else:
            print("Use 'audit [full/custom] to start an audit'")

    def do_quit(self, args):
        "Quit from AIA Audit console."
        raise SystemExit
