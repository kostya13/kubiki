"Одномерный клеточный автомат"
from kubiki.mc import mc, block

rules = {
    (1, 1, 1): 0,
    (1, 1, 0): 1,
    (1, 0, 1): 1,
    (1, 0, 0): 1,
    (0, 1, 1): 0,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0
 }

length = 200
steps = 100

draw = {0: block.SAND,
        1: block.GRASS}

cells = [0] * length
buffer = [0] * length


def draw_line(z):
    for i, c in enumerate(cells):
        mc.setBlock(i, 0, z, draw[c])


def init_state():
    cells[length//2] = 1
    draw_line(0)
      
    
def neighbours(i):
    if i == 0:
        return length-1, i, 1
    elif i == length - 1:
        return i-1, i, 0
    else:
        return i - 1, i, i + 1


def next_step(left, middle, right):
    key = (cells[left], cells[middle], cells[right])
    return rules[key]

    
def generate():
    init_state()
    for g in range(1, steps):
        for i in range(length):
            (left, middle, right) = neighbours(i)
            buffer[i] = next_step(left, middle, right)
        for i in range(length):
            cells[i] = buffer[i]
        draw_line(g)
            
    
generate()
print('complete')

        