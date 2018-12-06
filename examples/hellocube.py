import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from minecraftstuff import MinecraftDrawing
mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)


#mc.postToChat("Привет.")
print(mc.getBlock(0, 0, 0))
s = time.time()
# time.sleep(1)
# print(mc.getBlock(0,0,0))
# for i in range(100):
#     for j in range(1):
#         for k in range(100):
#             mc.setBlock(i,j,k,block.GRASS)
mc.setBlocks(0,0,0,100,0,100,block.GRASS)

#mc.setBlocks(0,0,0,100,1,0,block.GRASS)
#mc.setBlocks(0,0,0,0,1,100,block.GRASS)

#mc.setBlocks(0,0,100,100,1,100,block.GRASS)
#mc.setBlocks(100,0,0,100,1,100,block.GRASS)


#while True:
#     playerPos = mc.player.getTilePos()
#     print(playerPos)
#    hit = mc.events.pollBlockHits()
#    if hit:
#        mc.setBlock(*hit[0].pos,block.GRASS)
#    time.sleep(0.1)

#mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.DIAMOND_ORE)
#mcDrawing.drawLine(0,0,-10,-10,10,-5,block.STONE.id)
print(time.time() - s)
