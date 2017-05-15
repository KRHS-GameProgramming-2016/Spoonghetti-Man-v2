import pygame, sys, math
from Meatball import *

class Specialmeatball(Meatball):
    def __init__(self, pos=[0,0], size=None):
        Meatball.__init__(self, pos, size)
        self.image = pygame.image.load("rsc/ball/spicy.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.points = 2
