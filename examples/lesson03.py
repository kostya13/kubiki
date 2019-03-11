"Создание зданий с помощью классов"
from kubiki.mc import mc, block, clean
from random import randint

        
def wallZY(xs, ys, zs, lz, ly, bl=block.BRICK_BLOCK):
    for z in range(lz):
        for y in range(ly):
            mc.setBlock(xs, ys + y, zs + z, bl)

def wallXY(xs, ys, zs, lx, ly, bl=block.BRICK_BLOCK):
    for x in range(lx):
        for y in range(ly):
            mc.setBlock(xs + x, ys + y, zs, bl)

def wallXZ(xs, ys, zs, lx, lz, bl=block.BRICK_BLOCK):
    for z in range(lz):
        for x in range(lx):
            mc.setBlock(xs + x, ys, zs + z, bl)


def roof(xs, ys, zs, lx, ly, back=False, bl=block.BRICK_BLOCK):
    for x in range(lx):
        for y in range(ly):
            z = -y if back else y
            mc.setBlock(xs + x, ys + y, zs + z, bl)


def triangle(xs, ys, zs, lz, ly, bl=block.BRICK_BLOCK):
    startz = zs
    lengthz = lz
    for y in range(ly):
        for z in range(lengthz):
            mc.setBlock(xs, ys + y, startz + z, bl)
        startz += 1
        lengthz -= 2
      

def flat_cube():
    wallXZ(0,0,0, 20,20)
    wallXY(0,0,0, 20,20, block.LAPIS_LAZULI_BLOCK)
    wallXY(0,0,20, 20,20, block.LAPIS_LAZULI_BLOCK)
    wallZY(0,0,0, 20,20, block.DIAMOND_BLOCK)
    wallZY(20,0,0, 20,20, block.DIAMOND_BLOCK)
    wallXZ(0,20,0, 21,21)


def roof_house():
    wallXZ(0,0,0, 20,20)
    wallXY(0,0,0, 20,20, block.LAPIS_LAZULI_BLOCK)
    wallXY(0,0,20, 20,20, block.LAPIS_LAZULI_BLOCK)
    wallZY(0,0,0, 20,20, block.DIAMOND_BLOCK)
    wallZY(20,0,0, 20,20, block.DIAMOND_BLOCK)
    roof(0,20,0, 21,11)
    roof(0,20,20, 21,11, True)
    triangle(0,20,0, 21,20, block.DIAMOND_BLOCK)
    triangle(20,20,0, 21,20, block.DIAMOND_BLOCK)    
    

clean()
roof_house()

