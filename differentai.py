import pygame, sys, math, random
from Player import *
from Bullet import *


class Differentai(Player):
    def __init__(self, maxSpeed =3 , pos=[10,10]):
        Player.__init__(self, maxSpeed, pos)
        size = [65,65]
        self.maxSpeed = maxSpeed     
        self.images = [pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton2.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton21.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton22.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton23.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton24.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton25.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton26.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton27.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton28.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton29.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton210.png"), size),
                       #pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton211.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton212.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton213.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton214.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton215.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton216.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton217.png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/enemy pictures/Spooky scary skeleton218.png"), size),
                       ]
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxFrame = len(self.images) - 1
        self.radius = self.rect.width/2 -1
        self.maxFrame = len(self.images) - 1
        self.animationTimer = 0
        self.animationTimerMax = .01 * 100 #seconds * 60 fps
        self.points = 0
        self.living = True
        self.kind = "AI"
        self.facing = "up"
        
        
    def update(self, size):
        if random.randint(0,75) == 0:
            self.goRandomDirection()
        if random.randint(0,30) == 0:
            Bullet(5, self.speed, self.rect.center)
        Player.update(self, size)
            
    def PlayerCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    self.hit = True
                    #self.speedx = -self.speedx
                    #self.move()
                    #self.speedy = 0
                    #self.didBounceX = True
                    #if not self.didBounceY:
                        #self.speedy = -self.speedy
                        #self.move()
                        #self.speedx = 0
                        #self.didBounceX = True
        
    def bounceWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.move()
                self.speedx = 0
                self.didBounceX = True
                self.speedy = 0
                self.didBounceY = True
                self.goRandomDirection()
        
    def goRandomDirection(self):
        xs = ["left", "right", "stop left", "stop right"]
        ys = ["up", "down", "stop up", "stop down"]
        self.speed = [0, 0]
        while self.speed == [0,0]:
            self.go(xs[random.randint(0,3)])
            self.go(ys[random.randint(0,3)])
            self.speed = [self.speedx, self.speedy]
        
