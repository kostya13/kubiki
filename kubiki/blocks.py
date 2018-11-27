def tex_coord(x, y, n=4):
    """ Return the bounding vertices of the texture square.

    """
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def tex_coords(top, bottom, side):
    """ Return a list of the texture squares for the top, bottom and side.

    """
    top = tex_coord(*top)
    bottom = tex_coord(*bottom)
    side = tex_coord(*side)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result

class Block:
    def __init__(self, num, tex_coords):
        self.num = num
        self.tex_coords = tex_coords

GRASS = Block(2, tex_coords((1, 0), (0, 1), (0, 0)))
SAND = Block(12, tex_coords((1, 1), (1, 1), (1, 1)))
BRICK = Block(45, tex_coords((2, 0), (2, 0), (2, 0)))
STONE = Block(98, tex_coords((0, 2), (2, 1), (2, 1)))