import __main__
import cmd
import time
from colorama import Fore
from beaupy import *
from beaupy.spinners import *
from modules.scanner.host_discovery_scanner import HostDiscovery
from modules.scanner.admin_finder_scanner import AdminFinderScanner
from modules.scanner.configure import Configure
from modules.scanner.nmap_scanner import NmapScanner
from modules.scanner.shodan_scanner import ShodanScanner
from modules.scanner.ssh_scanner import SSHScanner
from modules.scanner.theHarvester_scanner import TheHarvesterScanner


class MyPrompt(cmd.Cmd):
    prompt = 'AIAConsole ' + Fore.BLUE + '>' + Fore.RESET + " "
    doc_header = 'Showing AIA Audit console commands. Use help [command]:'
    ruler = Fore.LIGHTBLACK_EX + '-' + Fore.RESET

    def default(self, line):
        return print('Unknown command, use help for more information')

    def do_audit(self, args):
        """Use 'audit [full/custom] to start an audit'"""
        audit_results = {"data": []}
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
                    print(" ")
                    nmap_scan_type_options = [
                        "Scan my local network [24]",
                        "Scan only my device",
                        "Custom Network IP and range",
                    ]
                    nmap_scan_type = select(nmap_scan_type_options, cursor='🖥  ', cursor_style='red')
                    if nmap_scan_type == "Scan my local network [24]":
                        nmap_data = {"nmap": NmapScanner.scan_address("192.168.202.0", "/24")}
                        audit_results["data"].append(nmap_data)
                    elif nmap_scan_type == "Scan only my device":
                        nmap_data = {"nmap": NmapScanner.scan_address("192.168.202.116", "")}
                        audit_results["data"].append(nmap_data)
                    elif nmap_scan_type == "Custom Network IP and range":
                        hosts_data = {"hosts": HostDiscovery.main("192.168.202.0", "/24")}
                        audit_results["data"].append(hosts_data)
                        # Demanem que seleccioni els dispositius i posteriorment escanejem
                elif item == "Shodan API":
                    shodan_data = {"shodan": ShodanScanner.main()}
                    audit_results["data"].append(shodan_data)
                elif item == "theHarvester":
                    theharvester_data = {"theHarvester": TheHarvesterScanner.main()}
                    audit_results["data"].append(theharvester_data)
                elif item == "Website admin login finder":
                    admin_finder_data = {"admin_finder": AdminFinderScanner.main()}
                    audit_results["data"].append(admin_finder_data)
                elif item == "SSH-Audit":
                    ssh_audit_data = {"ssh_audit": SSHScanner.main()}
                    audit_results["data"].append(ssh_audit_data)
            print(" ")
            print("Results exported in the following path: ")
            print(" ")
            print(" ")
            print(audit_results)
            # Export the results to PDF HERE
        else:
            print("Use 'audit [full/custom] to start an audit'")

    def do_clear(self, args):
        """Use 'audit [full/custom] to start an audit'"""
        __main__.custom_clear()

    def do_quit(self, args):
        """Quit from AIA Audit console."""
        raise SystemExit
