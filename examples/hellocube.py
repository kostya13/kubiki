from kubiki import show, Craft
from kubiki import blocks

#show()
craft = Craft()

craft.setPos(0, 0, 10)
craft.setBlock(0, 0, 0, blocks.GRASS)
print(craft.getBlock(0, 0, 0))
craft.chat('Привет')
print(craft.getPos())

#craft.lookAt(0, 0, 0)

# craft.chat('Привет')
# for y in range(10):
#     for x in range(10):
#         craft.setBlock(x, y, 10, blocks.GRASS)
# craft.chat('Финиш')
