import socketserver

"""
class RemoteCommand:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.cmd_map = {codes.GET_BLOCK:self.getBlock,
                        codes.SET_BLOCK: self.setBlock,
                        codes.CHAT: self.chat,
                        codes.GET_POS: self.getPos,
                        codes.SET_POS: self.setPos,
                        codes.LOOK_AT: self.lookAt}
        self.block_map = {blocks.GRASS: GRASS,
                          blocks.BRICK: BRICK,
                          blocks.SAND: SAND,
                          blocks.STONE: STONE}


    def run(self, data):
        code = data[0]
        return struct.pack('B', code) + self.cmd_map[code](data[1:])

    def getBlock(self, payload):
        pos = struct.unpack('iii', payload)
        try:
            block = self.model.world[pos].num
        except KeyError:
            block = blocks.AIR
        return struct.pack('i', block)

    def setBlock(self, payload):
        x, y, z, block = struct.unpack('iiii', payload)
        self.model.add_block((x, y, z), self.block_map[block])
        return b''

    def chat(self, payload):
        self.window.chat_msg = payload.decode()
        return b''

    def getPos(self, _):
        return struct.pack('iii', *[int(i) for i in self.window.position])

    def setPos(self, payload):
        new_pos =  struct.unpack('iii', payload)
        self.window.position = new_pos
        return b''

    def lookAt(self, payload):
        pos = struct.unpack('iii', payload)
        self.window.rotation = (45, 45)
        return b''


class Connection:
    def __init__(self, window, model):
        host = 'localhost'
        port = 7777
        addr = (host, port)
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(addr)
        self.command = RemoteCommand(window, model)


    def poll(self):
        readable, writable, exceptional = select.select([self.udp_socket], [], [], 0.01)
        if readable:
            data, addr = self.udp_socket.recvfrom(1024)
            reply = self.command.run(data)
            self.udp_socket.sendto(reply, addr)

    def close(self):
        self.udp_socket.close()
"""

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data)


class Server:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        HOST, PORT = "localhost", 4711
        self.server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
        self.server.timeout = 0.1
        #self.server.handle_timeout = lambda _: pass

    def handle(self):
        self.server.handle_request()
