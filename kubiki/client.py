from socket import *

class Client:
    def __init__(self):
        host = 'localhost'
        port = 7777
        self.addr = (host,port)
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)

    def close(self):
        self.udp_socket.close()


    def send(self, data):
        self.udp_socket.sendto(data, self.addr)
        data = self.udp_socket.recvfrom(1024)
        return data

