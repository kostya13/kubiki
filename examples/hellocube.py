import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

#mc.postToChat("Привет.")
#print(mc.getBlock(0,0,0))
#print(mc.getBlock(0,0,0))
for i in range(10):
    for j in range(10):
        mc.setBlock(i,0,j,block.GRASS)
#playerPos = mc.player.getPos()
#mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.DIAMOND_ORE)
