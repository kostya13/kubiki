import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Vec3
from minecraftstuff import MinecraftDrawing
from random import randint
from time import sleep
mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)


class Boom:
    def __init__(self, x, z):
        y = mc.getHeight(x, z) + 1
        mc.setBlock(x, y, z, block.TNT)
        self.pos = Vec3(x, y, z)

    def boom(self):
       mcDrawing.drawSphere(self.pos.x, self.pos.y, self.pos.z, 5 ,block.AIR)

    def getPos(self):
        return self.pos
    

def prepare(size):
    mc.setBlocks(-size, -5, -size, size, 0, size, block.GRASS)


def set_tnt(count, size):
    tnt = []
    for c in range(count):
        tnt.append(Boom(randint(-size, size), randint(-size, size)))
    return tnt


def get_hit():
    ev = mc.events.pollBlockHits()
    if ev:
        return ev[0]
    return None    


def check_tnt(hit, tnt):
    for t in tnt:
        if hit.pos == t.getPos():
            t.boom()
            
            
def main_loop(tnt):
    while True:
        hit = get_hit()
        if hit:
              check_tnt(hit, tnt)


size = 10
prepare(size)

#tnt = Boom(0,0)
#sleep(1)
#tnt.boom()

tnt = set_tnt(20, size)
main_loop(tnt)