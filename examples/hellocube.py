import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from minecraftstuff import MinecraftDrawing
mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)

s = time.time()
mc.postToChat("Привет.")
#print(mc.getBlock(0,0,0))
#print(mc.getBlock(0,0,0))
# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             mc.setBlock(i,k,j,block.GRASS)
mc.setBlocks(0,0,0,100,1,100,block.GRASS)
#playerPos = mc.player.getPos()
#print(playerPos)
#mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.DIAMOND_ORE)
#mcDrawing.drawLine(0,0,-10,-10,10,-5,block.STONE.id)
print(time.time() - s)
