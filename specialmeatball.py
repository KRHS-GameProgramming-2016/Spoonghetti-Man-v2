import pygame, sys, math
from Meatball import *

class Specialmeatball(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self)
        #Meatball.__init__(self, pos, size)
        self.image = pygame.image.load("rsc/ball/spicy.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.points = 2
