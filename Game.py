import pygame, sys, math, random
from Meatball import *
from Level import *
#from Enemy import *
#from ShootingEnemy import *
#from LevelIndicator import *
from Player import *
#from Title import *
from AIPlayer import *
from specialmeatball import *
#from spicymeatball import *
from Wall import*  
from Timer import*
#from Spoonghettimonster import *
#from LevelIndicator import *
#from Goal import *
pygame.init()

clock = pygame.time.Clock()

width = 24*44 
height = 17*44
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0


all = pygame.sprite.OrderedUpdates()
thePlayers = pygame.sprite.Group()
meatballs = pygame.sprite.Group()
walls = pygame.sprite.Group()

Player.containers = all, thePlayers
AIPlayer.containers = all, thePlayers
Meatball.containers = all, meatballs
Specialmeatball.containers = all, meatballs
Wall.containers = all, walls


levx = 1
levy = 1


while True:
    level = Level(str(levx)+str(levy)+".lvl")     
    bgImage = pygame.image.load("Background/Floor.png").convert()
    bgRect = bgImage.get_rect() 
    for p in thePlayers.sprites():
        if p.kind == "human":
            player = p
        else:
            player2 = p
    timer = Timer([132, 50])
    score = Score([100, height - 30])
    #score2 = Score([width - 100, height - 30])
    #levelIndicator = LevelIndicator([width-10, 16], lev)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.go("up")
                if event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_RIGHT:
                    player.go("right")
                if event.key == pygame.K_LEFT: 
                    player.go("left")
                #if event.key == pygame.K_w:
                    #player2.go("up")
                #if event.key == pygame.K_s:
                    #player2.go("down")
                #if event.key == pygame.K_d:
                    #player2.go("right")
                #if event.key == pygame.K_a:
                    #player2.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_LEFT:
                    player.go("stop left")
                #if event.key == pygame.K_w:
                    #player2.go("stop up")
                #if event.key == pygame.K_s:
                    #player2.go("stop down")
                #if event.key == pygame.K_d:
                    #player2.go("stop right")
                #if event.key == pygame.K_a:
                    #player2.go("stop left")
    
        all.update(size)
        
        playersHitsWalls = pygame.sprite.groupcollide(thePlayers, walls, False, False)
        playersHitsMeatballs = pygame.sprite.groupcollide(thePlayers, meatballs, False, True)
        
        for p in playersHitsWalls:
            for wall in playersHitsWalls[p]:
                p.bounceWall(wall)

        for p in playersHitsMeatballs:
            for wall in playersHitsMeatballs[p]:
                print "HIT"
                
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
