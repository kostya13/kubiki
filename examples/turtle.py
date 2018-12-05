from minecraftstuff import MinecraftTurtle
import mcpi.minecraft as minecraft
from mcpi.vec3 import  *

import mcpi.block as block
import time


# connect to minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
print(pos)
# create minecraft turtle
steve = MinecraftTurtle(mc, Vec3(0,0,0))

steve.right(72)
steve.speed(8)
steve.forward(5)
steve.right(72)
steve.speed(10)
steve.forward(5)
steve.right(72)
steve.speed(0)
steve.forward(5)
steve.right(72)
steve.forward(5)

# change pen
steve.penblock(block.SAND.id, 0)

# backward
steve.speed(6)
steve.backward(10)

# change pen
steve.penblock(block.STONE.id, 1)

# pen up/down
steve.penup()
steve.forward(20)
steve.pendown()

# change pen
steve.penblock(block.WOOL.id, 2)

# up, down, left
steve.up(30)
steve.forward(5)
steve.right(72)
steve.forward(5)
steve.down(30)
steve.left(72)
steve.forward(5)

# change pen
steve.penblock(block.COBBLESTONE.id, 3)

# walking
steve.walk()
steve.forward(10)