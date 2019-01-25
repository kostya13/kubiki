import mcpi.minecraft as minecraft
from  mcpi.block import *
mc = minecraft.Minecraft.create()

bl = [
    SAPLING, #_UNKNOWN
    STONE,
    GRASS,
    DIRT,
    COBBLESTONE,
    WOOD_PLANKS,
    BEDROCK,
    WATER,
    LAVA,
    SAND,
    GRAVEL,
    GOLD_ORE,
    IRON_ORE,
    COAL_ORE,
    WOOD,
    LEAVES,
    GLASS,
    LAPIS_LAZULI_ORE,
    LAPIS_LAZULI_BLOCK,
    SANDSTONE,
    WOOL,
    GOLD_BLOCK,
    IRON_BLOCK,
    STONE_SLAB_DOUBLE,
    BRICK_BLOCK,
    TNT,
    
    
    STONE_BRICK,
    ]

for i, b in enumerate(bl):
    mc.setBlock(i * 2, 0, 0, b)
