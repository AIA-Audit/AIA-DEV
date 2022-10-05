import nmap3
from beaupy.spinners import *


class NmapScanner:

    @staticmethod
    def scan_address(ip, range):
        spinner_animation = ['🖥💣    🏢️ ', '🖥 💣   🏢️️ ', '🖥  💣  🏢️️ ', '🖥   💣 🏢️️ ', '🖥    💣🏢️️ ']
        spinner = Spinner(spinner_animation, "Running NMAP scan..")
        spinner.start()
        nmap = nmap3.Nmap()
        data = nmap.scan_top_ports(ip + range, args="-n --open --script vuln")
        spinner.stop()
        print("[✔] NMAP scan done")
        return data

    @staticmethod
    def scan_custom(self):
        print("Null for now")