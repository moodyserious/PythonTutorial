import socket

def Main():
    s = socket.socket()
    host = socket.gethostname()  # ip address of client
    port = 5000

    s.connect((host, port))

    message = input('Enter a message')

    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("Data : " + data)
        message = input('Enter a message')

    s.close()

if __name__ == '__main__':
    Main()

