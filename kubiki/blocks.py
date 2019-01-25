def tex_coord(x, y, n=16):
    """
    Return the bounding vertices of the texture square.
    """
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def tex_coords(top, bottom, side):
    """
    Return a list of the texture squares for the top, bottom and side.
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
        

# Первый параметр - это идентификатор блока в Minecraft
AIR = Block(0, tex_coords((0, 0), (0, 0), (0, 0)))
STONE = Block(1, tex_coords((1, 15), (1, 15), (1, 15))) 
GRASS = Block(2, tex_coords((12, 3), (2, 15), (3, 15)))
DIRT = Block(3, tex_coords((2, 15), (2, 15), (2, 15)))
COBBLESTONE = Block(4, tex_coords((0, 14), (0, 14), (0, 14)))
WOOD_PLANKS = Block(5, tex_coords((4, 15), (4, 15), (4, 15)))
BEDROCK = Block(7, tex_coords((1, 14), (1, 14), (1, 14)))
WATER = Block(8, tex_coords((15, 2), (15, 2), (15, 2)))
WATER_FLOWING = WATER
WATER_STATIONARY = WATER
LAVA = Block(10, tex_coords((15, 0), (15, 0), (15, 0)))
LAVA_FLOWING = LAVA
SAND = Block(12, tex_coords((2, 14), (2, 14), (2, 14)))
GRAVEL = Block(13, tex_coords((0, 15), (0, 15), (0, 15)))
GOLD_ORE = Block(14, tex_coords((0, 13), (0, 13), (0, 13)))
IRON_ORE = Block(15, tex_coords((1, 13), (1, 13), (1, 13)))
COAL_ORE = Block(16, tex_coords((2, 13), (2, 13), (2, 13)))
WOOD = Block(17, tex_coords((5, 14), (5, 14), (4, 14)))
LEAVES = Block(18, tex_coords((4, 12), (4, 12), (4, 12)))
GLASS = Block(20, tex_coords((1, 12), (1, 12), (1, 12)))
LAPIS_LAZULI_ORE = Block(21, tex_coords((0, 5), (0, 5), (0, 5)))
LAPIS_LAZULI_BLOCK = Block(22, tex_coords((0, 6), (0, 6), (0, 6)))
SANDSTONE = Block(24, tex_coords((0, 3), (0, 3), (0, 3)))
WOOL = Block(35, tex_coords((0, 11), (0, 11), (0, 11)))
GOLD_BLOCK = Block(41, tex_coords((7, 14), (7, 14), (7, 14)))
IRON_BLOCK = Block(42, tex_coords((6, 14), (6, 14), (6, 14)))
STONE_SLAB_DOUBLE = Block(43, tex_coords((6, 15), (6, 15), (5, 15)))
BRICK_BLOCK = Block(45, tex_coords((7, 15), (7, 15), (7, 15)))
TNT = Block(46, tex_coords((8, 15), (8, 15), (8, 15)))
BOOKSHELF = Block(47, tex_coords((4, 15), (4, 15), (3, 13)))
MOSS_STONE  = Block(48, tex_coords((4, 13), (4, 13), (4, 13)))
OBSIDIAN = Block(49, tex_coords((7, 5), (7, 5), (7, 5)))
CHEST  = Block(54, tex_coords((9, 14), (9, 14), (10, 14)))
DIAMOND_ORE = Block(56, tex_coords((2, 12), (2, 12), (2, 12)))
DIAMOND_BLOCK = Block(57, tex_coords((8, 14), (8, 14), (8, 14)))
CRAFTING_TABLE= Block(58, tex_coords((11, 13), (11, 13), (12, 12)))
FARMLAND = Block(60, tex_coords((7, 10), (7, 10), (7, 10)))
FURNACE_INACTIVE = Block(61, tex_coords((14, 12), (13, 12), (12, 13)))
FURNACE_ACTIVE = Block(62, tex_coords((14, 12), (14, 12), (13, 12)))
REDSTONE_ORE = Block(73, tex_coords((3, 12), (3, 12), (3, 12)))
SNOW = Block(78, tex_coords((2, 11), (2, 15), (4, 11)))
ICE = Block(79, tex_coords((3, 11), (3, 11), (3, 11)))
SNOW_BLOCK = Block(80, tex_coords((2, 11), (2, 11), (2, 11)))
CACTUS  = Block(81, tex_coords((5, 11), (5, 11), (6, 11)))
CLAY = Block(82, tex_coords((8, 11), (8, 11), (8, 11)))
GLOWSTONE_BLOCK = Block(89, tex_coords((9, 9), (9, 9), (9, 9)))
STONE_BRICK = Block(98, tex_coords((6, 12), (6, 12), (6, 12)))
MELON  = Block(103, tex_coords((9, 7), (9, 7), (8, 7)))
GLOWING_OBSIDIAN = Block(246, tex_coords((10, 2), (10, 2), (10, 2)))
NETHER_REACTOR_CORE = Block(247, tex_coords((10, 1), (10, 1), (10, 1)))

_UNKNOWN = Block(248, tex_coords((11, 15), (11, 15), (11, 15)))

num_to_name = {obj.num: key for key, obj in globals().items() if isinstance(obj, Block)}
"""
Неподдерживаемые блоки
Вместо них рисуется блок _UNKNOWN
SAPLING             = Block(6)
BED                 = Block(26)
COBWEB              = Block(30)
GRASS_TALL          = Block(31)
FLOWER_YELLOW       = Block(37)
FLOWER_CYAN         = Block(38)
MUSHROOM_BROWN      = Block(39)
MUSHROOM_RED        = Block(40)
STONE_SLAB          = Block(44)
TORCH               = Block(50)
FIRE                = Block(51)
STAIRS_WOOD         = Block(53)
DOOR_WOOD           = Block(64)
LADDER              = Block(65)
STAIRS_COBBLESTONE  = Block(67)
DOOR_IRON           = Block(71)
SUGAR_CANE          = Block(83)
FENCE               = Block(85)
BEDROCK_INVISIBLE   = Block(95)
GLASS_PANE          = Block(102)
FENCE_GATE          = Block(107)
"""