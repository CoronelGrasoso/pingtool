# Import os
import os

# Function for doing ping
def do_ping(ip, packets_size):
    os.system(f"ping -s {packets_size} {ip}")

# Clear function
def clear():
    os.system("clear")

def run():
    # Getting ip and packets size
    ip = input("Select the ip:\n")
    packets_size = input("Select packets size:\n")

    clear()
    
    # Doing the ping
    do_ping(ip, packets_size)

if __name__ == "__main__":
    while True:
        run()
        
        # Try again code
        dec = input("Again? [y/n]\n").lower()

        if dec != "y":
            break
