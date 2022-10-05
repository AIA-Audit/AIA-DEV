import requests
from shodan import Shodan


class ShodanScanner:

    @staticmethod
    def main():
        # Extract our public IP
        r = requests.get('https://api.ipify.org?format=json')
        public_ip = r.json()['ip']
        # Set up shodan with our API key
        api = Shodan('D2aJfVtgA7FYJHXe88EqL0urQu42UmFe')
        # Get the information from Shodan based on the our Public IP
        data = api.host(public_ip)
        return data
