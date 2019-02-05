"Рисование плоскости + логические операции"
from kubiki.mc import mc, block, clean
from random import randint


def horizontal(width, depth):
    for x in range(0, width):
        for z in range(0, depth):
            mc.setBlock(x, 0, z, block.GRASS)

def vertical(width, height):
    for x in range(0, width):
        for y in range(0, height):
            mc.setBlock(x, y, 0, block.BRICK_BLOCK)


def horizontal4(width, depth, xpos=0, zpos=0):
    for x in range(0, width):
        for z in range(0, depth):
            mc.setBlock(x + xpos, 0, z + zpos, block.GRASS)

def vertical4(width, height, xpos=0, zpos=0):
    for x in range(0, width):
        for y in range(0, height):
            mc.setBlock(x + xpos, y, zpos, block.BRICK_BLOCK)


def fence():
    horizontal4(10 ,10)
    vertical4(8, 5, 1, 1)
    vertical4(8, 5, 1, 8)


clean()
fence()

