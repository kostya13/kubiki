import mcpi.minecraft as minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing

mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)

clean = lambda: mc.setBlocks(-25, 0, -25, 25, 25, 25, block.AIR)