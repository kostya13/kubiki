import select
import socket
from kubiki import blocks


class RemoteCommand:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.cmd_map = {b"world.getBlock":self.world_getBlock,
                        b"world.setBlock": self.world_setBlock,
                        b"world.setBlocks": self.world_setBlocks,
                        b"chat.post": self.chat_post,
                        b"player.getPos": self.player_getPos,
                        b"player.setPos": self.player_setPos,
                        b"player.getTile": self.player_getTile}
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
            #print(data, cmd, payload)
            fun = self.cmd_map.get(cmd)
            if fun:
                return fun(payload)
            else:
                print(f'Unknown command: {cmd}')
        return None

    def world_getBlock(self, payload):
        pos = struct.unpack('iii', payload)
        try:
            block = self.model.world[pos].num
        except KeyError:
            block = blocks.AIR
        return struct.pack('i', block)

    def world_setBlock(self, payload):
        args = [int(i) for i in payload.split(b',')]
        self.model.add_block((args[0], args[1], args[2]), self._find_block(args[3]))

    def world_setBlocks(self, payload):
        args = [int(i) for i in payload.split(b',')]
        begin = args[0:3]
        end = args[3:6]
        block = self._find_block(args[7])
        for x in range(begin[0], end[0] + 1):
            for y in range(begin[1], end[1] + 1):
                for z in range(begin[2], end[2] + 1):
                    self.model.add_block((x, y, z), block)

    def chat_post(self, payload):
        self.window.chat_msg = payload.decode()

    def player_getPos(self, _):
        return ','.join([str(i) for i in self.window.position])

    def player_setPos(self, payload):
        new_pos =  struct.unpack('iii', payload)
        self.window.position = new_pos
        return b''

    def player_getTile(self, _):
        return ','.join([str(int(i)) for i in self.window.position])

class Server:
    def __init__(self, window, model):
        self.command = RemoteCommand(window, model)
        HOST, PORT = "localhost", 4711
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(1)
        self.connection = None
        self.file = None
        self.batch = 1
        #self.server.handle_timeout = lambda _: pass

    def _close(self):
        self.connection.close()
        self.connection = None
        self.file = None

    def _send(self, reply):
        if self.connection:
            self.connection.send(reply.encode() + b"\n")

    def accept(self):
        if self.connection and self.file:
            self._handle()
        else:
            if select.select([self.sock], [], [],0)[0]:
                self.connection, _ = self.sock.accept()
                self.file = self.connection.makefile("b")
                self._handle()
    def _handle(self):
        for _ in range(self.batch):
            data = self.file.readline()
            if data:
                reply = self.command.run(data)
                if reply:
                    self._send(reply)
            else:
                self._close()
                break

