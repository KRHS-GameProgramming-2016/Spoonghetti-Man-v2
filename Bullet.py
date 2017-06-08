import pygame, sys, math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, maxSpeed, shooterSpeed, pos=[10,10]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        size = [20,20]
        self.maxSpeed = maxSpeed     
        self.image = pygame.transform.scale(pygame.image.load("rsc/SHOOT1.png"), size)
        self.rect = self.image.get_rect(center = pos)
        
        if shooterSpeed[0] > 0:
            self.speedx = self.maxSpeed
        elif shooterSpeed[0] < 0:
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
        
        if shooterSpeed[1] > 0:
            self.speedy = self.maxSpeed
        elif shooterSpeed[1] < 0:
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
            
        self.speed = [self.speedx, self.speedy]
        if self.speed == [0,0] :
            self.kill()
        self.radius = self.rect.width/2 -1
        
    def move(self):
        self.rect = self.rect.move(self.speed)

    def update(self, size):
        self.move()
        self.bounceScreen(size)
               
    def bounceScreen(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.kill()
        if self.rect.top < 0 or self.rect.bottom > height:
            self.kill()
