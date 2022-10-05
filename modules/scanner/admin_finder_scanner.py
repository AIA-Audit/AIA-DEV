from beaupy.spinners import *

class AdminFinderScanner:
    @staticmethod
    def main():
        spinner_animation = ['🖥💣    🏢️ ', '🖥 💣   🏢️️ ', '🖥  💣  🏢️️ ', '🖥   💣 🏢️️ ', '🖥    💣🏢️️ ']
        spinner = Spinner(spinner_animation, "Running NMAP scan..")
        spinner.start()
        spinner.stop()
        print("[✔] AdminFinder scan done")
        return
