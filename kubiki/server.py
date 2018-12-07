import select
import socket
from kubiki import blocks
from collections import deque
import time
from itertools import product

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
                        b"player.getTile": self.player_getTile,
                        b"player.setTile": self.player_setTile,
                        b"world.getHeight": self.world_getHeight,
                        b"world.checkpoint.save": self.world_checkpoint_save,
                        b"world.checkpoint.restore": self.world_checkpoint_restore,
                        b"world.setting": self.world_setting,
                        b"camera.mode.setNormal": self.camera_mode_setNormal,
                        b"camera.mode.setThirdPerson": self.camera_mode_setThirdPerson,
                        b"camera.mode.setFixed": self.camera_mode_setFixed,
                        b"camera.mode.setPos": self.camera_mode_setPos,
                        b"events.block.hits": self.events_block_hits,
                        b"events.clear": self.events_clear}
        self.blocks = [blocks.GRASS, blocks.BRICK, blocks.SAND, blocks.STONE, blocks.AIR]


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
            fun = self.cmd_map.get(cmd)
            if fun:
                return fun(payload)
            else:
                print(f'Unknown command: {cmd}')
        return None

    def world_checkpoint_save(self, _):
        print("world.checkpoint.save", 'not implemented')

    def world_checkpoint_restore(self, _):
        print("world.checkpoint.restore", 'not implemented')

    def world_setting(self, _):
        print("world.setting", 'not implemented')

    def world_getBlock(self, payload):
        pos = [int(i) for i in payload.split(b',')]
        try:
            block = self.model.world[tuple(pos)]
        except KeyError:
            block = blocks.AIR
        return str(block.num)

    def world_setBlock(self, payload):
        args = [int(i) for i in payload.split(b',')]
        block = self._find_block(args[3])
        if block == blocks.AIR:
            self.model.remove_block((args[0], args[1], args[2]))
        else:
            self.model.add_block((args[0], args[1], args[2]), block)

    def world_setBlocks(self, payload):
        print(payload)
        args = [int(i) for i in payload.split(b',')]
        begin = args[0:3]
        end = args[3:6]
        block = self._find_block(args[6])
        for x,y,z in product(range(begin[0], end[0] + 1),
                             range(begin[1], end[1] + 1),
                             range(begin[2], end[2] + 1)):
                    if block == blocks.AIR:
                        self.model.remove_block((x, y, z))
                    else:
                        self.model.add_block((x, y, z), block)

    def chat_post(self, payload):
        self.window.chat_msg = payload.decode()

    def player_getPos(self, _):
        return ','.join([str(float(i)) for i in self.window.position])

    def player_setPos(self, payload):
        new_pos = [int(i) for i in payload.split(b',')]
        self.window.position = new_pos

    def player_getTile(self, _):
        return ','.join([str(int(i)) for i in self.window.position])

    def player_setTile(self, payload):
        self.player_setPos(payload)


    def world_getHeight(self, payload):
        args = [int(i) for i in payload.split(b',')]
        points =[i for i in self.model.world.keys() if i[0]==args[0] and i[2]==args[1]]
        if points:
            top = max(points, key=lambda x: x[1])
            return str(top[1])
        else:
            return '0'

    def camera_mode_setNormal(self, _):
        print("camera.mode.setNormal", 'not implemented')

    def camera_mode_setThirdPerson(self, _):
        print("camera.mode.setThirdPerson", 'not implemented')

    def camera_mode_setFixed(self, _):
        print("camera.mode.setFixed", 'not implemented')

    def camera_mode_setPos(self, _):
        print("camera.mode.setPos", 'not implemented')

    def events_block_hits(self, _):
        if self.window.event:
            event = self.window.event
            block = event[1]
            pos = ','.join([str(int(i)) for i in event[0]])
            self.window.event = None
            return f'{pos},0,{block}'
        return '|'
        
    def events_clear(self, _):
        print("events.clear", 'not implemented')


class Server:
    def __init__(self, window, model):
        self.command = RemoteCommand(window, model)
        HOST, PORT = "localhost", 4711
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(1)
        self.connection = None
        self.batch = 300
        self.commands = deque()

    def _close(self):
        self.connection.close()
        self.connection = None

    def _send(self, reply):
        if self.connection:
            self.connection.send(reply.encode() + b"\n")

    def accept(self):
        if self.connection:
            self._handle()
        else:
            if select.select([self.sock], [], [],0)[0]:
                self.connection, _ = self.sock.accept()
                self._handle()
        self._apply()

    def _handle(self):
        if select.select([self.connection], [], [], 0)[0]:
            try:
                data = self.connection.recv(65536)
                if data:
                    self.commands.extend([l for l in data.split(b'\n')])
                else:
                    self._close()
            except ConnectionError:
                print('Connection error')
                self._close()

    def _apply(self):
        for _ in range(self.batch):
            if self.commands:
                cmd = self.commands.popleft()
                reply = self.command.run(cmd)
                if reply:
                    self._send(reply)
            else:
                break
