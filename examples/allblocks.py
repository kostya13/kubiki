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
    BOOKSHELF,
    MOSS_STONE,
    OBSIDIAN,
    CHEST,
    DIAMOND_ORE,
    DIAMOND_BLOCK,
    CRAFTING_TABLE,
    FARMLAND,
    FURNACE_INACTIVE,
    FURNACE_ACTIVE,
    REDSTONE_ORE,
    SNOW,
    ICE,
    SNOW_BLOCK,
    CACTUS,
    CLAY,
    GLOWSTONE_BLOCK,
    STONE_BRICK,
    MELON,
    GLOWING_OBSIDIAN,
    NETHER_REACTOR_CORE
    ]

for i, b in enumerate(bl):
    mc.setBlock(i * 2, 0, 0, b)
