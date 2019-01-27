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
move = 10
steve.speed(10)
steve.up(45)
steve.forward(move)
steve.penblock(block.STONE.id, 1)
steve.down(90)
steve.forward(move)
steve.penblock(block.GOLD_BLOCK.id, 1)
steve.up(45)
steve.left(90)
steve.forward(move)
exit()
steve.right(45)


steve.forward(move)
steve.right(90)
steve.forward(move)
steve.penblock(block.STONE.id, 1)
steve.up(90)
steve.forward(move)
steve.right(45)
steve.forward(move)
steve.down(45)



# change pen
#steve.penblock(block.SAND.id, 0)

# backward
#steve.backward(10)

# change pen
#steve.penblock(block.STONE.id, 1)

# pen up/down
#steve.penup()
#steve.forward(20)
#steve.pendown()

#steve.down(30)
steve.left(72)
steve.forward(5)

# change pen
steve.penblock(block.COBBLESTONE.id, 3)