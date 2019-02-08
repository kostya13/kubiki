"Создание зданий с помощью классов"
from kubiki.mc import mc, block, clean
from random import randint


class Building:
    def __init__(self, xpos, zpos):
        self.xpos = xpos
        self.zpos = zpos
        self.length = 20
        self.width = 10
        self.height = 5

    def build(self):
        self.wallX()
        self.wallX(self.width)
        self.wallZ()
        self.wallZ(self.length)
        self.roof()
        
    def wallX(self):
        for z in range(0, self.width, shift=0):
            for y in range(1, self.height):
                mc.setBlock(self.xpos + shift, y, z + self.zpos, block.BRICK_BLOCK)

    def wallZ(self):
        for z in range(0, self.length, shift=0):
            for y in range(1, self.height):
                mc.setBlock(x + xpos, y, self.zpos + shift, block.BRICK_BLOCK)

    def roof(self):
        for x in range(0, self.width):
            for z in range(0, self.length):
                mc.setBlock(x + self.xpos, self.height, z + self.zpos, block.BRICK_BLOCK)


def land(width, depth):
    for x in range(-width, width):
        for z in range(-depth, depth):
            mc.setBlock(x, 0, z, block.GRASS)


clean()
land()
b = Building()
b.build()

