"Рисование осей"
from kubiki.mc import mc, block

трава = block.GRASS
песок = block.SAND
кирпич = block.BRICK_BLOCK
длинна = 20

def ось_X():
    for i in range(1, длинна):
        mc.setBlock(i, 0, 0, трава)

def ось_Y():
    for i in range(1, длинна):
        mc.setBlock(0, i, 0, песок)

def ось_Z():
    for i in range(1, длинна):
        mc.setBlock(0, 0, i, кирпич)

def нарисовать_оси():
    ось_X()
    ось_Y()
    ось_Z()

нарисовать_оси()



