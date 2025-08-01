import socket # importing the Socket module here
# Add at the top
from colorama import Fore, init # importing the Module used for New Coloured text output ~!
init(autoreset=True)
 
print_banner = ("""

  ____            _   ____            _                       ____  
 |  _ \ ___  _ __| |_|  _ \ ___  __ _| | _____ _ __    __   _|___ \ 
 | |_) / _ \| '__| __| |_) / _ \/ _` | |/ / _ \ '__|___\ \ / / __) |
 |  __/ (_) | |  | |_|  __/  __/ (_| |   <  __/ | |_____\ V / / __/ 
 |_|   \___/|_|   \__|_|   \___|\__,_|_|\_\___|_|        \_/ |_____|
    A Banner Grabber made using python's Socket Module 
    AUTHOR - Vinay Jangam 
    GITHUB - https://github.com/Vinayjango101/PortPeaker 
           
""")
print(print_banner)


ip = input(Fore.CYAN + "Enter IP Address/Host To Grab Banner for--> ")   #we can supply our own ip/host by this line

print(Fore.GREEN + f"\nScanning {ip}...\n")    #Prints "Scanning 192.168.0.X OR https://test.com"

common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]  #Defining Ports to scan in a LIST data type

for port in common_ports:  #for Loop Here to iterate through each individual port number in the port list
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Making a Socket Object here, socket.AF_INET is for IPv4 Address type and socket.SOCK_STREAM is for TCP protocol, and  for making a IPv6 address type and UDP protocol type we use socket.AF_INET6 and socket.SOCKET_DGRAM
             s.settimeout(10) # setting the timeout for each port scan to 5 seconds, after that move to next port
             s.connect((ip, port)) # connecting to the ip and port

             try:
                 banner = s.recv(1024).decode(errors="ignore").strip()
             except socket.timeout:
                 banner = "<NO BANNER RECEIVED ! (Timeout)>"
             except Exception as e:
                 banner = f"<ERROR READING BANNER! ({e})>"
             print(Fore.GREEN + f"[+] Port {port} open - Banner: {banner or '<Empty Response>'}")

    except socket.timeout:
        print(Fore.RED + f"[-] Port Number {port} timed out")
    except ConnectionRefusedError:
        print(Fore.RED + f"[-] Port Number {port} closed Connection refused !")
    except Exception as e:
        print(Fore.RED + f"[!] Port {port} Error {e}")
    # Removed finally block with s.close() because with-statement handles socket closing
