import mcpi.minecraft as minecraft
from mcpi.minecraft import Vec3
import mcpi.block as block
from minecraftstuff import MinecraftDrawing

mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)


def simple():
    mcDrawing.drawLine(-10, -10, -10, 10,10, 10,block.STONE.id)
    mcDrawing.drawCircle(0, 0, 0 ,10,block.WOOD.id)
    mcDrawing.drawSphere(0, 0, 0, 5,block.DIAMOND_BLOCK.id)
    

def sign():
    faceVertices = [
        Vec3(0,10,0),
        Vec3(0,30,0),
        Vec3(20,30,0),
        Vec3(20,40,0),
        Vec3(50,20,0),
        Vec3(20, 0,0),
        Vec3(20,10,0)]
    mcDrawing.drawFace(faceVertices, True, block.GOLD_BLOCK.id)
        

class Sign:
    def __init__(self):
        self.verticles = [
            Vec3(0,1,0),
            Vec3(0,3,0),
            Vec3(2,3,0),
            Vec3(2,4,0),
            Vec3(5,2,0),
            Vec3(2, 0,0),
            Vec3(2,1,0)]
        
    def points(self):
        for v in self.verticles:
            mc.setBlock(v.x, v.y, v.z, block.GOLD_BLOCK.id)
    
    def scale(self, scale):
        for i, v in enumerate(self.verticles):
            self.verticles[i] = v * scale

    def move(self, x, y, z):
        vec = Vec3(x, y, z)
        self.verticles = [v + vec for v in self.verticles]

    def draw(self):
        mcDrawing.drawFace(self.verticles, True, block.GOLD_BLOCK.id)                          

    def hide(self):
        mcDrawing.drawFace(self.verticles, True, block.AIR.id)                          


s = Sign()
s.scale(10)
s.points()
#s.move(5, 5, 5)
#s.draw()