import kubiki.commands as codes
import socket
import select
import atexit
import struct


class Craft:
    def __init__(self):
        host = 'localhost'
        port = 7777
        self.addr = (host,port)
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        atexit.register(self._bye)

    def getBlock(self, x, y, z):
        data = struct.pack('iii', x, y, z)
        result = self._send(codes.GET_BLOCK, data)
        block_type = struct.unpack('I', result)[0]
        return block_type

    def setBlock(self, x, y, z, block):
        data = struct.pack('iiii',  x, y, z, block)
        self._send(codes.SET_BLOCK, data)

    def chat(self, msg):
        self._send(codes.CHAT, msg.encode())

    def getPos(self):
        result = self._send(codes.GET_POS, b'')
        x, y, z = struct.unpack('iii', result)
        return x, y, z

    def setPos(self, x, y, z):
        data = struct.pack('iii',  x, y, z)
        self._send(codes.SET_POS, data)

    def lookAt(self, x, y, z):
        data = struct.pack('iii',  x, y, z)
        self._send(codes.LOOK_AT, data)

    def _bye(self):
        print('bye')
        self.udp_socket.close()

    def _send(self, command_code, data):
        self.udp_socket.sendto(struct.pack('B', command_code) + data, self.addr)
        r = select.select([self.udp_socket], [], [], 1)[0]
        if r:
            data, conn = self.udp_socket.recvfrom(1024)
            return data[1:]
        else:
            raise ConnectionError
