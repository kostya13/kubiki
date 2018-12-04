from minecraftstuff import MinecraftTurtle
import mcpi.minecraft as minecraft
import mcpi.block as block
import time


# connect to minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
print(pos)s
# create minecraft turtle
steve = MinecraftTurtle(mc, pos)

steve.forward(5)