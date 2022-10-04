from beaupy import *
from beaupy.spinners import *


class Configure:

    @staticmethod
    def main():

        item_options = [
            "nmap Scan - Full scan",
            "Shodan API",
            "theHarvester",
            "Website admin login finder",
            "SSH-Audit"
        ]
        # Choose multiple options from a list
        items = select_multiple(item_options, tick_character='💀', ticked_indices=[0], cursor_style='red')
        return items
