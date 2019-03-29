from minecraftstuff import MinecraftShape, ShapeBlock
import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import  Vec3
import time
import threading
from time import sleep


mc = minecraft.Minecraft.create()

def ground():
    mc.setBlocks(-20,0,-20,20,0,20,block.GRASS)

def clean():
    mc.setBlocks(-20,0,-20,20,5,20,block.AIR)

class BackAndForth:
    def __init__(self, shape, xstart, xend):
        self.xstart = xstart
        self.xend = xend
        self.shape = shape
        self.direction = 1
        
    def move(self):
        if self.shape.position.x > self.xend:
            self.direction = -1
        elif self.shape.position.x < self.xstart:
            self.direction = +1
        self.shape.moveBy(self.direction,0,0)
        
shapeBlocks = [ShapeBlock(0,0,0,block.DIAMOND_BLOCK),
               ShapeBlock(1,0,0,block.DIAMOND_BLOCK),
               ShapeBlock(-1,0,0,block.DIAMOND_BLOCK),
               ShapeBlock(0,1,0,block.DIAMOND_BLOCK),
               ShapeBlock(0,-1,0,block.DIAMOND_BLOCK),
               ShapeBlock(0,0,-1,block.DIAMOND_BLOCK),
               ShapeBlock(0,0,1,block.DIAMOND_BLOCK)]


shapes = [BackAndForth(MinecraftShape(mc, Vec3(0, 2, i * 5), shapeBlocks), -10, 10)
          for i in range(3)]

clean()
ground()
while True:
    for s in shapes:
        s.move()
    sleep(0.1)
