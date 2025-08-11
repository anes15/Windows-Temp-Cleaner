import os
import shutil
import getpass
from colorama import Fore,init
import subprocess

init(autoreset=True)

user = getpass.getuser()

files = [r"C:\Windows\Temp",
        fr"C:\Users\{user}\AppData\Local\Temp",
        fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Cache",
        fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Cache",
        fr"C:\Windows\SoftwareDistribution\Download",
        fr"C:\Windows\Prefetch",
        fr"C:\Windows\Minidump",
        fr"C:\ProgramData\Microsoft\Windows\WER",
        r"C:\Windows\Logs",
        r"C:\Windows\Panther",
        r"C:\Windows\System32\LogFiles",
        r"C:\Windows\Memory.dmp",
        fr"C:\Users\{user}\AppData\Local\Mozilla\Firefox\Profiles",
        fr"C:\Users\{user}\AppData\Local\Opera Software\Opera Stable\Cache",
        fr"C:\Users\{user}\AppData\Roaming\Opera Software\Opera Stable\Cache",
        fr"C:\Users\{user}\AppData\Local\Discord\Cache",
        fr"C:\Users\{user}\AppData\Local\Microsoft\Windows\INetCache",
        fr"C:\Users\{user}\AppData\Local\Temp\chocolatey", 
        r"C:\Windows\SoftwareDistribution\DataStore",
        r"C:\Windows\Installer\$PatchCache$",
        fr"C:\Users\{user}\AppData\Local\Microsoft\Office\UnsavedFiles",
        ]




def take_ownership(path):
    try:
        subprocess.run(["takeown", "/F", path, "/A", "/R", "/D", "Y"], capture_output=True)
        subprocess.run(["icacls", path, "/grant", "administrators:F", "/T", "/C"], capture_output=True)
    except Exception as e:
        print(f"[!] Failed to take ownership: {e}")


def remove():
    total = 0

    for path in files:

        if not os.path.exists(path):
                    continue

        try:
            for file in os.listdir(path):
                f = os.path.join(path,file)
                
                try :
                    if os.path.islink(f):
                        os.unlink(f)
                        print(f"Link removed: {file}")
                        total += 1

                    elif os.path.isfile(f):
                        os.remove(f)
                        print(f"File removed: {file}")
                        total += 1

                    elif os.path.isdir(f):
                        shutil.rmtree(f, ignore_errors=True)
                        print(f"Folder removed: {file}")
                        total += 1

                except PermissionError as p:
                    take_ownership(f)
                try:
                    if os.path.islink(f):
                        os.unlink(f)
                        print(f"Link removed: {file}")
                        total += 1

                    elif os.path.isfile(f):
                        os.remove(f)
                        print(f"File removed: {file}")
                        total += 1

                    elif os.path.isdir(f):
                        shutil.rmtree(f, ignore_errors=True)
                        print(f"Folder removed: {file}")
                        total += 1

                except OSError as e:
                    if e.errno == 32:
                        print(Fore.YELLOW + f"[!] the file is useing : {e}")

                    else :
                        print(Fore.YELLOW + f"[!] Error : {e}")


        except PermissionError:
            take_ownership(path)
    
    print(Fore.BLUE + f"[+] {total} file removed")

def file():
    for path in files:
        if not os.path.exists(path):
            continue
        try :
            for file in os.listdir(path):
                print(file)
        except Exception as e:
            print(f"ERROR : {e}")


def banner():
    banner = """
██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗███████╗
██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║██╔════╝
██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║███████╗
██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║╚════██║
╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝███████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝
                                                          
████████╗███████╗███╗   ███╗██████╗ 
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗
   ██║   █████╗  ██╔████╔██║██████╔╝
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ 
   ██║   ███████╗██║ ╚═╝ ██║██║     
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     
                                    
 ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
        
        [?] command : start         --> start removing
        [?] command : show          --> show the file
        [?] command : exit          --> exit
"""
    print(Fore.GREEN + banner)


def run():
    banner()
    global user
    while True:
        
        command = input(Fore.CYAN + f"{user}\>").strip()
        if command.lower() == "start":
            remove()
        elif command.lower() == "show":
            file()
        elif command.lower() == "exit":
            exit()
            
        else : 
            print(Fore.RED + "[!] Unknown command")

if __name__ == "__main__":
    run()
