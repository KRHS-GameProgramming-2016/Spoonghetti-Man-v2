import pygame, sys, math 

class Score(pygame.sprite.Sprite):
    def __init__(self, pos, value = 0):
        self.value = value
        self.font = pygame.font.Font("rsc/Fonts/Courier font/coure.fon", 51)
        self.image = self.font.render("Score: " + str(self.value), True, (100,0,00))
        self.rect = self.image.get_rect(center = pos)
    
    def change(self, amount = 1):
        self.value += amount
        if self.value <= 0:
            self.value = 0
        self.image = self.font.render("Score: " + str(self.value), True, (100,0,00))
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def setValue(self, amount = 0):
        self.value = amount
        if self.value <= 0:
            self.value = 0
        self.image = self.font.render("Score: " + str(self.value), True, (100,0,00))
        self.rect = self.image.get_rect(center = self.rect.center)

