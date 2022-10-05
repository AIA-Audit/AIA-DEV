from beaupy.spinners import *
class TheHarvesterScanner:

    @staticmethod
    def main():
        spinner_animation = ['🖥💣    🏢️ ', '🖥 💣   🏢️️ ', '🖥  💣  🏢️️ ', '🖥   💣 🏢️️ ', '🖥    💣🏢️️ ']
        spinner = Spinner(spinner_animation, "Running NMAP scan..")
        spinner.start()
        spinner.stop()
        print("[✔] theHarvester scan done")
        return
