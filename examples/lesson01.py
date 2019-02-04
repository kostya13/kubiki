"Разбиение кода на функции. Рисование осей"
from kubiki.mc import mc, block


block_X = block.GOLD_BLOCK
block_Y = block.SAND
block_Z = block.BRICK_BLOCK
length = 20


def axis_X():
    for i in range(1, length):
        mc.setBlock(i, 0, 0, block_X)


def axis_Y():
    for i in range(1, length):
        mc.setBlock(0, i, 0, block_Y)


def axis_Z():
    for i in range(1, length):
        mc.setBlock(0, 0, i, block_Z)


def draw_axes():
    axis_X()
    axis_Y()
    axis_Z()


draw_axes()



