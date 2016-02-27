import socket

def Main():
    s = socket.socket()   # by default its TCP
    host = socket.gethostname()
    port = 5000
    s.bind((host, port))
    s.listen(1)     # allow only one client to connect at a time

    print("Waiting for connection ")
    c, addr = s.accept()
    print("Connection from : " + str(addr))

    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print('Data : ' + data)
        data = data.upper()
        c.send(data.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    Main()








