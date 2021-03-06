class Block:
    """Minecraft PI block description. Can be sent to Minecraft.setBlock/s"""
    def __init__(self, id, data=0):
        self.id = id
        self.data = data

    def __cmp__(self, rhs):
        return hash(self) - hash(rhs)

    def __eq__(self, rhs):
        return self.id == rhs.id and self.data == rhs.data

    def __hash__(self):
        return (self.id << 8) + self.data

    def withData(self, data):
        return Block(self.id, data)

    def __iter__(self):
        """Allows a Block to be sent whenever id [and data] is needed"""
        return iter((self.id, self.data))
        
    def __repr__(self):
        return "Block(%d, %d)"%(self.id, self.data)

AIR                 = Block(0)
STONE               = Block(1)
GRASS               = Block(2)
DIRT                = Block(3)
COBBLESTONE         = Block(4)
WOOD_PLANKS         = Block(5)
SAPLING             = Block(6)
BEDROCK             = Block(7)
WATER_FLOWING       = Block(8)
WATER               = WATER_FLOWING
WATER_STATIONARY    = Block(9)
LAVA_FLOWING        = Block(10)
LAVA                = LAVA_FLOWING
LAVA_STATIONARY     = Block(11)
SAND                = Block(12)
GRAVEL              = Block(13)
GOLD_ORE            = Block(14)
IRON_ORE            = Block(15)
COAL_ORE            = Block(16)
WOOD                = Block(17)
LEAVES              = Block(18)
SPONGE				= Block(19)
GLASS               = Block(20)
LAPIS_LAZULI_ORE    = Block(21)
LAPIS_LAZULI_BLOCK  = Block(22)
DISPENSER			= Block(23)
SANDSTONE           = Block(24)
NOTE_BLOCK			= Block(25)
BED                 = Block(26)
POWERED_RAIL		= Block(27)
DETECTOR_RAIL		= Block(28)
STICKY_PISTON		= Block(29)
COBWEB              = Block(30)
GRASS_TALL          = Block(31)
DEAD_BUSH			= Block(32)
PISTON				= Block(33)
WOOL                = Block(35)
WHITE_WOOL			= WOOL.withData(0)
ORANGE_WOOL			= WOOL.withData(1)
MAGENTA_WOOL		= WOOL.withData(2)
LIGHT_BLUE_WOOL		= WOOL.withData(3)
YELLOW_WOOL			= WOOL.withData(4)
LIME_WOOL			= WOOL.withData(5)
PINK_WOOL			= WOOL.withData(6)
GRAY_WOOL			= WOOL.withData(7)
LIGHT_GRAY_WOOL		= WOOL.withData(8)
GREY_WOOL			= WOOL.withData(7)
LIGHT_GREY_WOOL		= WOOL.withData(8)
CYAN_WOOL			= WOOL.withData(9)
PURPLE_WOOL			= WOOL.withData(10)
BLUE_WOOL			= WOOL.withData(11)
BROWN_WOOL			= WOOL.withData(12)
GREEN_WOOL			= WOOL.withData(13)
RED_WOOL			= WOOL.withData(14)
BLACK_WOOL			= WOOL.withData(15)
FLOWER_YELLOW       = Block(37)
DANDELION			= Block(37)
FLOWER_CYAN         = Block(38)
ROSE				= Block(38)
MUSHROOM_BROWN      = Block(39)
MUSHROOM_RED        = Block(40)
GOLD_BLOCK          = Block(41)
IRON_BLOCK          = Block(42)
STONE_SLAB_DOUBLE   = Block(43)
STONE_SLAB          = Block(44)
SANDSTONE_SLAB		= STONE_SLAB.withData(1)
COBBLESTONE_SLAB	= STONE_SLAB.withData(3)
BRICK_SLAB			= STONE_SLAB.withData(4)
STONE_BRICK_SLAB 	= STONE_SLAB.withData(5)
NETHER_BRICK_SLAB	= STONE_SLAB.withData(6)
QUARTZ_SLAB			= STONE_SLAB.withData(7)
BRICK_BLOCK         = Block(45)
TNT                 = Block(46)
BOOKSHELF           = Block(47)
MOSS_STONE          = Block(48)
OBSIDIAN            = Block(49)
TORCH               = Block(50)
FIRE                = Block(51)
STAIRS_WOOD         = Block(53)
CHEST               = Block(54)
REDSTONE_WIRE		= Block(55)
DIAMOND_ORE         = Block(56)
DIAMOND_BLOCK       = Block(57)
CRAFTING_TABLE      = Block(58)
FARMLAND            = Block(60)
FURNACE_INACTIVE    = Block(61)
FURNACE_ACTIVE      = Block(62)
DOOR_WOOD           = Block(64)
LADDER              = Block(65)
RAIL				= Block(66)
STAIRS_COBBLESTONE  = Block(67)
STONE_PRESSURE_PLATE= Block(70)
DOOR_IRON           = Block(71)
WOOD_PRESSURE_PLATE	= Block(72)
REDSTONE_ORE        = Block(73)
SNOW                = Block(78)
ICE                 = Block(79)
SNOW_BLOCK          = Block(80)
CACTUS              = Block(81)
CLAY                = Block(82)
SUGAR_CANE          = Block(83)
FENCE               = Block(85)
PUMPKIN				= Block(86)
NETHERRACK			= Block(87)
SOUL_SAND			= Block(88)
GLOWSTONE_BLOCK     = Block(89)
STAINED_GLASS		= Block(95)
WHITE_STAINED_GLASS	= STAINED_GLASS.withData(0)
ORANGE_STAINED_GLASS	= STAINED_GLASS.withData(1)
MAGENTA_STAINED_GLASS	= STAINED_GLASS.withData(2)
LIGHT_BLUE_STAINED_GLASS	= STAINED_GLASS.withData(3)
YELLOW_STAINED_GLASS	= STAINED_GLASS.withData(4)
LIME_STAINED_GLASS	= STAINED_GLASS.withData(5)
PINK_STAINED_GLASS	= STAINED_GLASS.withData(6)
GRAY_STAINED_GLASS	= STAINED_GLASS.withData(7)
LIGHT_GRAY_STAINED_GLASS	= STAINED_GLASS.withData(8)
GREY_STAINED_GLASS	= STAINED_GLASS.withData(7)
LIGHT_GREY_STAINED_GLASS	= STAINED_GLASS.withData(8)
CYAN_STAINED_GLASS	= STAINED_GLASS.withData(9)
PURPLE_STAINED_GLASS	= STAINED_GLASS.withData(10)
BLUE_STAINED_GLASS	= STAINED_GLASS.withData(11)
BROWN_STAINED_GLASS	= STAINED_GLASS.withData(12)
GREEN_STAINED_GLASS	= STAINED_GLASS.withData(13)
RED_STAINED_GLASS	= STAINED_GLASS.withData(14)
BLACK_STAINED_GLASS	= STAINED_GLASS.withData(15)
STONE_BRICK         = Block(98)
IRON_BARS			= Block(101)
GLASS_PANE          = Block(102)
WHITE_STAINED_GLASS_PANE	= GLASS_PANE.withData(0)
ORANGE_STAINED_GLASS_PANE	= GLASS_PANE.withData(1)
MAGENTA_STAINED_GLASS_PANE	= GLASS_PANE.withData(2)
LIGHT_BLUE_STAINED_GLASS_PANE	= GLASS_PANE.withData(3)
YELLOW_STAINED_GLASS_PANE	= GLASS_PANE.withData(4)
LIME_STAINED_GLASS_PANE	= GLASS_PANE.withData(5)
PINK_STAINED_GLASS_PANE	= GLASS_PANE.withData(6)
GRAY_STAINED_GLASS_PANE	= GLASS_PANE.withData(7)
LIGHT_GRAY_STAINED_GLASS_PANE	= GLASS_PANE.withData(8)
GREY_STAINED_GLASS_PANE	= GLASS_PANE.withData(7)
LIGHT_GREY_STAINED_GLASS_PANE	= GLASS_PANE.withData(8)
CYAN_STAINED_GLASS_PANE	= GLASS_PANE.withData(9)
PURPLE_STAINED_GLASS_PANE	= GLASS_PANE.withData(10)
BLUE_STAINED_GLASS_PANE	= GLASS_PANE.withData(11)
BROWN_STAINED_GLASS_PANE	= GLASS_PANE.withData(12)
GREEN_STAINED_GLASS_PANE	= GLASS_PANE.withData(13)
RED_STAINED_GLASS_PANE	= GLASS_PANE.withData(14)
BLACK_STAINED_GLASS_PANE	= GLASS_PANE.withData(15)
MELON               = Block(103)
FENCE_GATE          = Block(107)
MYCELIUM 			= Block(110)
LILY_PAD			= Block(111)
NETHER_BRICK 		= Block(112)
NETHER_BRICK_FENCE	= Block(113)
ENCHANTING_TABLE	= Block(116)
BREWING_STAND		= Block(117)
CAULDRON			= Block(118)
END_STONE			= Block(121)
REDSTONE_LAMP 		= Block(123)
EMERALD_ORE 		= Block(129)
ENDER_CHEST			= Block(130)
EMERALD_BLOCK		= Block(133)
COMMAND_BLOCK		= Block(137)
BEACON				= Block(138)
COBBLESTONE_WALL	= Block(139)
ANVIL				= Block(145)
REDSTONE_BLOCK		= Block(152)
NETHER_QUARTZ_ORE	= Block(153)
HOPPER				= Block(154)
QUARTZ_BLOCK		= Block(155)
STAINED_CLAY		= Block(159)
WHITE_STAINED_CLAY	= STAINED_CLAY.withData(0)
ORANGE_STAINED_CLAY	= STAINED_CLAY.withData(1)
MAGENTA_STAINED_CLAY	= STAINED_CLAY.withData(2)
LIGHT_BLUE_STAINED_CLAY	= STAINED_CLAY.withData(3)
YELLOW_STAINED_CLAY	= STAINED_CLAY.withData(4)
LIME_STAINED_CLAY	= STAINED_CLAY.withData(5)
PINK_STAINED_CLAY	= STAINED_CLAY.withData(6)
GRAY_STAINED_CLAY	= STAINED_CLAY.withData(7)
LIGHT_GRAY_STAINED_CLAY	= STAINED_CLAY.withData(8)
GREY_STAINED_CLAY	= STAINED_CLAY.withData(7)
LIGHT_GREY_STAINED_CLAY	= STAINED_CLAY.withData(8)
CYAN_STAINED_CLAY	= STAINED_CLAY.withData(9)
PURPLE_STAINED_CLAY	= STAINED_CLAY.withData(10)
BLUE_STAINED_CLAY	= STAINED_CLAY.withData(11)
BROWN_STAINED_CLAY	= STAINED_CLAY.withData(12)
GREEN_STAINED_CLAY	= STAINED_CLAY.withData(13)
RED_STAINED_CLAY	= STAINED_CLAY.withData(14)
BLACK_STAINED_CLAY	= STAINED_CLAY.withData(15)
