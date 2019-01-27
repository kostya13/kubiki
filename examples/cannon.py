from kubiki.mc import mc, mcDrawing, block
import math
import time

G = 9.8
PI = 3.14159

def get_coord(u0, alfa, t):
    alfa = alfa * PI/180
    x = u0 * t * math.cos(alfa)
    y = u0 * t * math.sin(alfa) - G * t * t / 2
    return x*100 , y*100

def impact(x):
    mcDrawing.drawSphere(x, 0, 0, 3, block.AIR)
    
    
def throw_block():
    for t in range(1000):
        x, y = get_coord(7.0, 5 , t/1000)
        if y < 0 and x > 10:
            impact(x)
            break
        mc.setBlock(x, y, 0, block.TNT)
        time.sleep(0.001)
        mc.setBlock(x, y, 0, block.AIR)
        
        
def draw_scene():
    mc.setBlocks(-10, 0, -5, 200, 0, 5,  block.GRASS)

#draw_scene()
throw_block()
    