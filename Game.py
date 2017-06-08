import pygame, sys, math, random
from Meatball import *
from Level import *
from Chest import*
from Player import *
from AIPlayer import *
from differentai import *
from specialmeatball import *
from catbread import *
#from spicymeatball import *
from Wall import*  
from Timer import*
from Score import*
from Bullet import*



# set window position from: http://pygame.org/wiki/SettingWindowPosition
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,15)

pygame.init()

clock = pygame.time.Clock()
tileSize = 44
width = 23*tileSize 
height = 17*tileSize
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0


all = pygame.sprite.OrderedUpdates()
thePlayers = pygame.sprite.Group()
meatballs = pygame.sprite.Group()
walls = pygame.sprite.Group()
levelChangeBlocks = pygame.sprite.Group()
chests = pygame.sprite.Group()
bullets = pygame.sprite.Group()

Player.containers = all, thePlayers
AIPlayer.containers = all, thePlayers
Meatball.containers = all, meatballs
Specialmeatball.containers = all, meatballs
Wall.containers = all, walls
LevelChangeBlock.containers = all, levelChangeBlocks
Chest.containers = all, chests
Bullet.containers = all, bullets


while True:
    levx = 1
    levy = 1
    world = 1
    level = Level(str(world)+"."+str(levy)+str(levx)+".lvl", tileSize)     
    bgImage = pygame.image.load("Background/Floor.png").convert()
    bgRect = bgImage.get_rect() 
    for p in thePlayers.sprites():
        player2 = p
    player = Player (5, [4*tileSize + tileSize/2,
                         6*tileSize + tileSize/2])
    print levelChangeBlocks.sprites()
    timer = Timer([132, 50])
    score = Score([100, height - 30])
    #score2 = Score([width - 100, height - 30])
    #levelIndicator = LevelIndicator([width-10, 16], lev)
    while player.living:
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
        
        for meatball in meatballs:
            if player.bounceMeatball(meatball):
                meatball.kill()
                score.setValue(player.points)
                
       
        playersHitsWalls = pygame.sprite.groupcollide(thePlayers, walls, False, False)
        playersHitsMeatballs = pygame.sprite.groupcollide(thePlayers, meatballs, False, True)
        playersHitsPlayers = pygame.sprite.groupcollide(thePlayers, thePlayers, False, False)
        playerHitsLevelChangeBlocks = pygame.sprite.spritecollide(player, levelChangeBlocks, False)
        playerHitsChests = pygame.sprite.spritecollide(player, chests, False)
        playersHitsBullets = pygame.sprite.spritecollide(player, bullets, False)
        bulletsHitsWalls = pygame.sprite.groupcollide(bullets, walls, True, False)
        
        for p in playersHitsWalls:
            for wall in playersHitsWalls[p]:
                p.bounceWall(wall)
                
        for bullet in playersHitsBullets:
            player.living = False
        
        for p1 in playersHitsPlayers:
            for p2 in playersHitsPlayers[p1]:
                if p1 != p2:
                    p1.living = False
                
        for chest in playerHitsChests:
            if chest.kind == 'd':
                world = 2     
                levx = 1
                levy = 1
                px = tileSize+tileSize/2+25
                py = player.rect.center[1]
                pPos = [px, py]
                for s in all.sprites():
                    s.kill()
                level = Level(str(world)+"."+str(levy)+str(levx)+".lvl", tileSize) 
                print str(levx)+str(levy)+".lvl"    
                #bgImage = pygame.image.load("rsc/Chest.png").convert()
                bgRect = bgImage.get_rect() 
                for p in thePlayers.sprites():
                    if p.kind == "human":
                        player = p
                    else:
                        player2 = p
                player = Player(5, pPos)
                break
                
       
        for blk in playerHitsLevelChangeBlocks:
            if blk.kind == 'E':
                levx += 1
                px = tileSize+tileSize/2+25
                py = player.rect.center[1]
                pPos = [px, py]
                for s in all.sprites():
                    s.kill()
                level = Level(str(world)+"."+str(levy)+str(levx)+".lvl", tileSize) 
                print str(levx)+str(levy)+".lvl"    
                bgImage = pygame.image.load("Background/Floor.png").convert()
                bgRect = bgImage.get_rect() 
                for p in thePlayers.sprites():
                    if p.kind == "human":
                        player = p
                    else:
                        player2 = p
                player = Player(5, pPos)
                break
                
            if blk.kind == 'S':
                levy += 1
                px = player.rect.center[0]
                py = tileSize+tileSize/2+25
                pPos = [px, py]
                for s in all.sprites():
                    s.kill()
                level = Level(str(world)+"."+str(levy)+str(levx)+".lvl", tileSize) 
                print str(levx)+str(levy)+".lvl"    
                bgImage = pygame.image.load("Background/Floor.png").convert()
                bgRect = bgImage.get_rect() 
                for p in thePlayers.sprites():
                    if p.kind == "human":
                        player = p
                    else:
                        player2 = p
                player = Player(5, pPos)
                break
                
            if blk.kind == 'W':
                levx -= 1
                px = width-tileSize-tileSize/2-25
                py = player.rect.center[1]
                pPos = [px, py]
                for s in all.sprites():
                    s.kill()
                level = Level(str(world)+"."+str(levy)+str(levx)+".lvl", tileSize) 
                print str(levx)+str(levy)+".lvl"    
                bgImage = pygame.image.load("Background/Floor.png").convert()
                bgRect = bgImage.get_rect() 
                for p in thePlayers.sprites():
                    if p.kind == "human":
                        player = p
                    else:
                        player2 = p
                player = Player(5, pPos)
                break
                
            if blk.kind == 'N':
                levy -= 1
                px = player.rect.center[0]
                py = height-tileSize-tileSize/2-25
                pPos = [px, py]                
                for s in all.sprites():
                    s.kill()
                level = Level(str(world)+"."+str(levy)+str(levx)+".lvl", tileSize) 
                print str(levx)+str(levy)+".lvl"    
                bgImage = pygame.image.load("Background/Floor.png").convert()
                bgRect = bgImage.get_rect() 
                for p in thePlayers.sprites():
                    if p.kind == "human":
                        player = p
                    else:
                        player2 = p
                player = Player(5, pPos)
                break
                
        print r, g, b
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(score.image, score.rect)
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    for s in all.sprites():
        s.kill()
