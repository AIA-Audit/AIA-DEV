import __main__
import cmd
import time
from colorama import Fore
from beaupy.spinners import *
from modules.scanner.configure import Configure
from modules.scanner.shodan_scanner import ShodanScanner


class MyPrompt(cmd.Cmd):

    prompt = 'AIAConsole ' + Fore.BLUE + '>' + Fore.RESET + " "
    doc_header = 'Showing AIA Audit console commands. Use help [command]:'
    ruler = Fore.LIGHTBLACK_EX + '-' + Fore.RESET

    def default(self, line):
        return print('Unknown command, use help for more information')

    def do_audit(self, args):
        audit_results = {"data": []}
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
            time.sleep(3)
            spinner.stop()
            for item in items:
                if item == "nmap Scan - Full scan":
                    nmap_data = {"nmap": "empty"}
                    audit_results["data"].append(nmap_data)
                elif item == "Shodan API":
                    shodan_data = {"shodan": ShodanScanner.main()}
                    audit_results["data"].append(shodan_data)
                elif item == "theHarvester":
                    theharvester_data = {"theHarvester": "empty"}
                    audit_results["data"].append(theharvester_data)
                elif item == "Website admin login finder":
                    admin_finder_data = {"admin_finder": "empty"}
                    audit_results["data"].append(admin_finder_data)
                elif item == "SSH-Audit":
                    ssh_audit_data = {"ssh_audit": "empty"}
                    audit_results["data"].append(ssh_audit_data)
            # Export the results to PDF HERE
        else:
            print("Use 'audit [full/custom] to start an audit'")

    def do_quit(self, args):
        "Quit from AIA Audit console."
        raise SystemExit
