import socket

def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp
    host = socket.gethostname()
    port = 5001  # client port
    s.bind((host, port))
    server = (host, 5000)   # server port

    message = input("Enter a message ")
    while message!= 'q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received " + data)
        message = input("Enter a message ")
    s.close()

if __name__ == '__main__':
    Main()



