from kubiki.client import Client

class Craft:
    def __init__(self):
        self._client = Client()
        self.player = None
        self.builder = None

    def chat(self):
        self._client.send(b'\x00\x00')
        pass
    def getPos(self):
        pass

    def setPos(self):
        pass

    def getBlock(self):
        pass

    def setBlock(self):
        pass