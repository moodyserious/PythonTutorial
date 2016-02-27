import socket
import time

host = socket.gethostname()
port = 5000

users = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quit = False
print("Waiting for connection")

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if "Quit" in (data).decode('utf-8'):
            quit = True
        if addr not in users:
            users.append(addr)   # stores address of each user

        print(time.ctime(time.time()) + str(addr) + ": " + data.decode('utf-8'))  # prints the message from users
        for add in users:
            if addr != add:   # dont send the message to the sender
                #print("Sender " + addr + " " + "Storage " + add)
                s.sendto(data, add)   # received data, sending it to all users

    except:
        pass

s.close()

























