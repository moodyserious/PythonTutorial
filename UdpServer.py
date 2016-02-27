import socket

def Main():
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     host = socket.gethostname()
     port = 5000

     s.bind((host, port))
     print('Waiting for connection')

     while True:
         data, addr = s.recvfrom(1024)
         data = data.decode('utf-8')
         print("Connection from " + str(addr))
         print("Data " + data)
         data = data.upper()
         s.sendto(data.encode('utf-8'), addr)
     s.close()

if __name__ == '__main__':
     Main()