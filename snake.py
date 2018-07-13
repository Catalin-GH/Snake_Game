import pygame as pg
from defines import *

class snake:
    def __init__(self, surface, headposx=10, headposy=10):
        self.surface = surface
        self.length = 5
        self.poslist = [(headposx, y) for y in reversed(range(headposy - self.length + 1, headposy + 1))]
        self.direction = RIGHT
        self.crashed = False

        self.snakeblock = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.snakeblock.set_alpha(255)
        self.snakeblock.fill(GREEN)

        self.backblock = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.backblock.set_alpha(255)
        self.backblock.fill(BLACK)

    def getHeadPos(self):
        return (self.poslist[0])

    def getMotionDir(self):
        return self.direction

    def getPosList(self):
        return self.poslist

    def setMotionDir(self, direction):
        self.direction = direction

    def incLength(self):
        self.length += 1

    def move(self):
        direction = self.getMotionDir()
        headPos = self.getHeadPos()

        if direction == UP:
            poslist = [(headPos[0] - 1, headPos[1])]
        elif direction == DOWN:
            poslist = [(headPos[0] + 1, headPos[1])]
        elif direction == LEFT:
            poslist = [(headPos[0], headPos[1] - 1)]
        elif direction == RIGHT:
            poslist = [(headPos[0], headPos[1] + 1)]

        poslist.extend(self.poslist[:-1])
        self.poslist = poslist

        # check if crashed
        if self.getHeadPos() in self.getPosList()[1:]:
            self.crashed = True

    # check if the snake has crashed
    def chrashed(self):
        return self.crashed

    # grow the snake. add a new position at the end
    def grow(self):
        lastpos = self.getPosList()[-1]
        self.length += 1
        self.poslist.append((lastpos[0] - 1, lastpos[1]))

    # draw the snake
    def draw(self):
        skb = self.snakeblock
        sf = self.surface

        for blockElem in self.getPosList():
            sf.blit(skb, (blockElem[1] * BLOCK_SIZE, blockElem[0] * BLOCK_SIZE))

    # delete the snake
    def remove(self):
        bkb = self.backblock
        sf = self.surface

        # draw block for every snake position
        for blockpos in self.getPosList():
            sf.blit(bkb, (blockpos[1] * BLOCK_SIZE, blockpos[0] * BLOCK_SIZE))