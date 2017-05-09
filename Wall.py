import pygame, sys, math
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, tileSize=40):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.image = pygame.image.load("rsc/wall/Wally.png")
        if tileSize:
            self.image = pygame.transform.scale(self.image, [tileSize,tileSize])
        self.rect = self.image.get_rect(center = pos)
        
    def update(self, size):
        pass
