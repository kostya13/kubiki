import mcpi.minecraft as minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)

mc.postToChat("Привет.")
#print(mc.getBlock(0,0,0))
#print(mc.getBlock(0,0,0))
for i in range(100):
    for j in range(100):
        mc.setBlock(i,0,j,block.GRASS)
#playerPos = mc.player.getPos()
#print(playerPos)
#mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.DIAMOND_ORE)
#mcDrawing.drawLine(0,0,-10,-10,10,-5,block.STONE.id)

