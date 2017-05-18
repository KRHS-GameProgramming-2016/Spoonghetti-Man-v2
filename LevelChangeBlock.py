import pygame, sys, math, random

class LevelChangeBlock(pygame.sprite.Sprite):
    def __init__(self, pos, size, kind):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = size
        self.image = pygame.image.load("rsc/wall/Wallys.png")
        
        if size:
            self.image = pygame.transform.scale(self.image, [size, size])
        
        self.rect = self.image.get_rect(center = pos)
        self.kind = kind
