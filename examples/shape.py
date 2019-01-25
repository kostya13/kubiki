from minecraftstuff import MinecraftShape, ShapeBlock
import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import  *
import time

#connect to minecraft
mc = minecraft.Minecraft.create()

#test MinecraftShape
#playerPos = mc.player.getTilePos()

#create the shape object
shapeBlocks = [ShapeBlock(0,0,0,block.DIAMOND_BLOCK.id),
                ShapeBlock(1,0,0,block.DIAMOND_BLOCK.id),
                ShapeBlock(1,0,1,block.DIAMOND_BLOCK.id),
                ShapeBlock(0,0,1,block.DIAMOND_BLOCK.id),
                ShapeBlock(0,1,0,block.DIAMOND_BLOCK.id),
                ShapeBlock(1,1,0,block.DIAMOND_BLOCK.id),
                ShapeBlock(1,1,1,block.DIAMOND_BLOCK.id),
                ShapeBlock(0,1,1,block.DIAMOND_BLOCK.id)]

shapeBlocks = [ ShapeBlock(x,y,z,block.DIAMOND_BLOCK.id)
                for x in range(40)
                for y in range(10)
                for z in range(1)]
#move the shape about
myShape = MinecraftShape(mc, Vec3(0,0,0), shapeBlocks)
print("drawn shape")
for _ in range(3):
    for i in range(30):
        myShape.moveBy(1,0,0)
    for i in range(30):
        myShape.moveBy(-1,0,0)

##myShape.moveBy(10,0,1)
##time.sleep(0.5)
##myShape.moveBy(1,10,0)
##time.sleep(0.5)
###rotate the shape
##myShape.rotate(90,0,0)

#clear the shape
#myShape.clear()
