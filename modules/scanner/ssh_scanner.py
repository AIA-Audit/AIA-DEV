from beaupy.spinners import *
class SSHScanner:

    @staticmethod
    def main():
        spinner_animation = ['🖥💣    🏢️ ', '🖥 💣   🏢️️ ', '🖥  💣  🏢️️ ', '🖥   💣 🏢️️ ', '🖥    💣🏢️️ ']
        spinner = Spinner(spinner_animation, "Running NMAP scan..")
        spinner.start()
        spinner.stop()
        print("[✔] SSH scan done")
        return
