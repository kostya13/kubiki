import select
import socket
from kubiki import blocks


class RemoteCommand:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.cmd_map = {b"world.getBlock":self.getBlock,
                        b"world.setBlock": self.setBlock,
                        b"chat.post": self.chat,
                        b"player.getPos": self.getPos,
                        b"player.setPos": self.setPos}
        self.blocks = [blocks.GRASS, blocks.BRICK, blocks.SAND, blocks.STONE]

    def _find_block(self, num):
        for b in self.blocks:
            if num == b.num:
                return b
        return blocks.GRASS

    def run(self, data):

        start = data.find(b'(')
        if start > 0:
            cmd = data[:start]
            end = data.find(b')')
            payload = data[start +1 : end]
            print(data, cmd, payload)
            fun = self.cmd_map.get(cmd)
            if fun:
                return fun(payload)
            else:
                print(f'Unknown command: {cmd}')
        return None

    def getBlock(self, payload):
        pos = struct.unpack('iii', payload)
        try:
            block = self.model.world[pos].num
        except KeyError:
            block = blocks.AIR
        return struct.pack('i', block)

    def setBlock(self, payload):
        args = [int(i) for i in payload.split(b',')]
        self.model.add_block((args[0], args[1], args[2]), self._find_block(args[3]))


    def chat(self, payload):
        self.window.chat_msg = payload.decode()

    def getPos(self, _):
        return struct.pack('iii', *[int(i) for i in self.window.position])

    def setPos(self, payload):
        new_pos =  struct.unpack('iii', payload)
        self.window.position = new_pos
        return b''


class Server:
    def __init__(self, window, model):
        self.command = RemoteCommand(window, model)
        HOST, PORT = "localhost", 4711
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(1)
        self.connection = None

        #self.server.handle_timeout = lambda _: pass

    def _close(self):
        self.connection.close()
        self.connection = None

    def accept(self):
        if self.connection:
            self._handle()
        else:
            if select.select([self.sock], [], [],0)[0]:
                self.connection, _ = self.sock.accept()
                self._handle()

    def _handle(self):
        data = self.connection.recv(1024)
        print('received {!r}'.format(data))
        if data:
            print('sending data back to the client')
            for c in data.split(b'\n'):
                reply = self.command.run(c)
            if reply:
                self.connection.send(reply)
        else:
            self._close()