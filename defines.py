# colors
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

SCALE = 20  #game resolution

BLOCK_SIZE = SCALE

#game speed
SPEED      = 8
SPEED_TICK = 2
SPEED_INC  = 5

#map settings
OFFSET     = 4
MAP_LENGTH = 20
MAP_ORIGIN = (0, BLOCK_SIZE * OFFSET)

#screen settings
SCREEN_WIDTH  = (BLOCK_SIZE * MAP_LENGTH) + (BLOCK_SIZE * 2)
SCREEN_HEIGHT = (BLOCK_SIZE * MAP_LENGTH) + (BLOCK_SIZE * 2) + (BLOCK_SIZE * OFFSET)

#info
sStartText    = "PRESS ANY KEY TO START"
sGameOverText = "Game Over"
sScore        = "Score: "

# motion direction constants
UP    = 0
DOWN  = 1
LEFT  = 2
RIGHT = 3