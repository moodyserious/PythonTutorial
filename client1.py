import socket
import threading
import time

tlock = threading.Lock()
exit = False

def receiveOld(name, sock):
    while not exit:
        try:
            tlock.acquire()
            while True:
                data , addr = sock.recvfrom(1024)
                print(data.decode('utf-8'))
        except:
            pass
        finally:
            tlock.release()

host = socket.gethostname()
port = 5002

server = (host, 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receiveOld, args=("ReceiveThread", s))
rT.start()  # get old messages

name = input("Name: ")
message = input(name + ": ")
while message != "q":
    if message != "":
        s.sendto((name + " : " + message).encode('utf-8'), server)
        tlock.acquire()
        message = input(name + ": ")
        tlock.release()
        time.sleep(0.2)

exit = True
rT.join()
s.close()
