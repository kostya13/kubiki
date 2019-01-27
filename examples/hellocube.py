import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

mc.postToChat("Hello.")
print(mc.getBlock(0, 0, 0))
mc.setBlocks(0,0,0,9,0,9,block.GRASS)
#mc.connection._socket.close()