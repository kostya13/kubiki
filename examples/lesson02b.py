"""Логические операции
Случайные числа
Введение понятие тип boolean
"""
from kubiki.mc import mc, block, clean
from random import randint


длина = 10
ширина = 10
снег = 5

def нарисовать_землю():
    for x in range(0, длина):
        for z in range(0, ширина):
            mc.setBlock(x, 0, z, block.GRASS)


def нарисовать_снег():
    for i in range(снег):
        x = randint(0, длина - 1)
        z = randint(0, ширина - 1)
        mc.setBlock(x, 0, z, block.SNOW)


def убрать_снег():
    snow = block.SNOW.id
    for x in range(0, длина):
        for z in range(0, ширина):
            b = mc.getBlock(x, 0, z)
            if b == snow:
                mc.setBlock(x, 0, z, block.GRASS)

clean()
нарисовать_землю()
нарисовать_снег()
input('Выпал снег')
print('Уборка снега!')
убрать_снег()
mc.postToChat('Done')