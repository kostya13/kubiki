#
# Code under the MIT license by Alexander Pruss
#
import mcpi.minecraft as minecraft
from mcpi.minecraft import *
from mcpi.block import *
from math import *
import random
import sys


def getHeightBelow(x, y, z):
    return min(mc.getHeight(x, z), y)


def rectangularPrism(x1, y1, z1, x2, y2, z2, distribution):
    x1 = int(round(x1))
    y1 = int(round(y1))
    z1 = int(round(z1))
    x2 = int(round(x2))
    y2 = int(round(y2))
    z2 = int(round(z2))
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1):
                if isinstance(distribution, Block):
                    mc.setBlock(x, y, z, distribution)
                else:
                    r = random.random()
                    for p, b in distribution:
                        r -= p
                        if r < 0:
                            mc.setBlock(x, y, z, b)
                            break


# Note: the first set of coordinates must be smaller than the second
def wall(x1, y1, z1, x2, y2, z2, baseHeight, altHeight, distribution):
    x = x1
    z = z1

    while True:
        if (x - x1 + z - z1) % 2 == 0:
            height = altHeight
        else:
            height = baseHeight
        y0 = getHeightBelow(x, y1, z)
        rectangularPrism(x, y0, z, x, y1 + height, z, distribution)
        if x >= x2 and z >= z2:
            return
        if x < x2:
            x = x + 1
        if z < z2:
            z = z + 1


# Note: the first set of coordinates must be smaller than the second
def moatSide(x1, y1, z1, x2, y2, z2, depth):
    x = x1
    z = z1

    while True:
        y0 = getHeightBelow(x, y1, z)
        mc.setBlocks(x, y0 - depth + 1, z, x, y0, z, WATER_STATIONARY)
        if x >= x2 and z >= z2:
            return
        if x < x2:
            x = x + 1
        if z < z2:
            z = z + 1


def crenellatedSquare(x1, y1, z1, width, height, altHeight, distribution):
    wall(x1, y1, z1, x1 + width - 1, y1, z1, height, altHeight, distribution)
    wall(x1, y1, z1, x1, y1, z1 + width - 1, height, altHeight, distribution)
    wall(x1 + width - 1, y1, z1, x1 + width - 1, y1, z1 + width - 1, height, altHeight, distribution)
    wall(x1, y1, z1 + width - 1, x1 + width - 1, y1, z1 + width - 1, height, altHeight, distribution)


def square(x, y, z, width, height, distribution):
    crenellatedSquare(x, y, z, width, height, height, distribution)


def moatSquare(x1, y1, z1, width, depth):
    moatSide(x1, y1, z1, x1 + width - 1, y1, z1, depth)
    moatSide(x1, y1, z1, x1, y1, z1 + width - 1, depth)
    moatSide(x1 + width - 1, y1, z1, x1 + width - 1, y1, z1 + width - 1, depth)
    moatSide(x1, y1, z1 + width - 1, x1 + width - 1, y1, z1 + width - 1, depth)


def crenellatedSquareWithInnerWall(x, y, z, width, baseHeight, altHeight, distribution):
    crenellatedSquare(x, y, z, width, baseHeight, altHeight, distribution)
    square(x + 1, y, z + 1, width - 2, baseHeight - 1, distribution)


def tower(x, y, z, width, baseHeight, altHeight, innerHeight, distribution):
    crenellatedSquareWithInnerWall(x, y, z, width, baseHeight, altHeight, distribution)
    rectangularPrism(x + 2, y + innerHeight - 1, z + 2, x + width - 3, y + innerHeight - 1, z + width - 3, distribution)


mc = minecraft.Minecraft.create()
pos = Vec3(1,1,1)
mc.setBlocks(-20,0,-20,80,0,80, GRASS)


distribution = ((.05, MOSS_STONE), (.1, Block(STONE_BRICK.id, 1)), (.2, Block(STONE_BRICK.id, 2)),
                (.651, Block(STONE_BRICK.id, 0)))

wallSize = 51
groundY = 1 + getHeightBelow(pos.x, pos.y, pos.z)

# outer walls
mc.postToChat("Outer walls")
crenellatedSquareWithInnerWall(pos.x, groundY, pos.z, wallSize, 9, 10, distribution)

# towers
mc.postToChat("Towers")
tower(pos.x - 7, groundY, pos.z - 7, 9, 12, 13, 11, distribution)
tower(pos.x + wallSize - 2, groundY, pos.z + wallSize - 2, 9, 12, 13, 11, distribution)
tower(pos.x - 7, groundY, pos.z + wallSize - 2, 9, 12, 13, 11, distribution)
tower(pos.x + wallSize - 1, groundY, pos.z - 7, 9, 12, 13, 11, distribution)

# keep
mc.postToChat("Keep")
keepStartX = pos.x + wallSize / 4
keepStartZ = pos.z + wallSize / 4
keepWidth = wallSize / 6 * 3
tower(keepStartX, groundY, keepStartZ, keepWidth, 16, 17, 15, distribution)


mc.postToChat("Castle done")