"Разбиение кода на функции. Рисование осей"
from kubiki.mc import mc, block, clean


block_X = block.GOLD_BLOCK
block_Y = block.SAND
block_Z = block.BRICK_BLOCK
length = 20

axis = {'x': (1, 0, 0, block_X),
        'y': (0, 1, 0, block_Y),
        'z': (0, 0, 1, block_Z)}

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


def axis_any(name, length):
    mul = axis[name]
    for i in range(1, length):
        mc.setBlock(mul[0] * i, mul[1] * i, mul[2] * i, mul[3])    


def draw_axes2():
    for a in axis:
        axis_any(a, 15)


clean()
#draw_axes()
draw_axes2()



