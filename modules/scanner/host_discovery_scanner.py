import nmap3
from beaupy.spinners import *


class HostDiscovery:

    @staticmethod
    def main(ip="127.0.0.1", range="/24"):
        spinner_animation = ['🖥💣    🏢️ ', '🖥 💣   🏢️️ ', '🖥  💣  🏢️️ ', '🖥   💣 🏢️️ ', '🖥    💣🏢️️ ']
        spinner = Spinner(spinner_animation, "Running Hosts discovery (Network)")
        spinner.start()
        nmap = nmap3.nmap3.NmapHostDiscovery()
        data = nmap.nmap_no_portscan(ip + range)
        spinner.stop()
        print("[✔] Hosts discovery scan done")
        return data
