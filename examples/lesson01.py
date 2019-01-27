"Разбиение кода на функции. Рисование осей"
from kubiki.mc import mc, block

золото = block.GOLD_BLOCK
песок = block.SAND
кирпич = block.BRICK_BLOCK
длина = 20

def ось_X():
    for i in range(1, длина):
        mc.setBlock(i, 0, 0, золото)

def ось_Y():
    for i in range(1, длина):
        mc.setBlock(0, i, 0, песок)

def ось_Z():
    for i in range(1, длина):
        mc.setBlock(0, 0, i, кирпич)

def нарисовать_оси():
    ось_X()
    ось_Y()
    ось_Z()

нарисовать_оси()



