from defines import *
import pygame as pg
import random as rnd

class food:
    def __init__(self, surface, minx, maxx, miny, maxy):
        self.surface = surface
        self.posx = rnd.randint(minx, maxx - 1)
        self.posy = rnd.randint(miny, maxy - 1)

        self.foodblock = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.foodblock.set_alpha(255)
        self.foodblock.fill(RED)

    def getPos(self):
        return (self.posx, self.posy)

    def draw(self):
        fb = self.foodblock
        sf = self.surface
        sf.blit(fb, (self.getPos()[1] * BLOCK_SIZE, self.getPos()[0] * BLOCK_SIZE))