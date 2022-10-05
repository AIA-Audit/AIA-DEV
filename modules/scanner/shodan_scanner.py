import requests
from shodan import Shodan
from beaupy.spinners import *


class ShodanScanner:
    @staticmethod
    def main():
        spinner_animation = ['🖥💣    🏢️ ', '🖥 💣   🏢️️ ', '🖥  💣  🏢️️ ', '🖥   💣 🏢️️ ', '🖥    💣🏢️️ ']
        spinner = Spinner(spinner_animation, "Running NMAP scan..")
        spinner.start()
        # Extract our public IP
        r = requests.get('https://api.ipify.org?format=json')
        public_ip = r.json()['ip']
        # Set up shodan with our API key
        api = Shodan('D2aJfVtgA7FYJHXe88EqL0urQu42UmFe')
        # Get the information from Shodan based on our Public IP
        try:
            data = api.host(public_ip)
        except:
            print("No information available from Shodan.")
            data = "No information available"
        spinner.stop()
        print("[✔] Shodan Scan done")
        return data
