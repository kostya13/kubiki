from kubiki.client import Client

class Chat:
    def encode(self, msg):
        pass
    def decode(self, data):
        pass

class Craft:
    def __init__(self):
        self._client = Client()
        self.player = None
        self.builder = None

    def chat(self):
        self._client.send(parser.Chat.encode('Hello'))

    def getPos(self):
        pass

    def setPos(self):
        pass

    def getBlock(self):
        pass

    def setBlock(self):
        pass