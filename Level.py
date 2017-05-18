import pygame, sys, math
from Player  import *
from AIPlayer  import *
from Enemy import *
from ShootingEnemy import *
from Wall import *
from Meatball import *
from specialmeatball import *
from LevelChangeBlock import *

class Level():
    def __init__(self, levelFile, tileSize=44):
        self.tileSize = tileSize
        self.playerSize = tileSize
        self.loadLevel(levelFile)
    
    def unloadLevel(self):
        pass
               
    def loadLevel(self, levelFile):        
        f = open("rsc/levels/"+levelFile, 'r')
        lines = f.readlines()
        f.close()
        
        """
        print lines
        print "________________________"
        
        for line in lines:
            print line
        print "________________________"
        """
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for line in lines:
            print line
        print "________________________"
        
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#':
                    Wall([x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                if c == 'E' or c == 'W' or c == 'S' or c == 'N':
                    LevelChangeBlock([x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize,
                                       c)
                                  
                if c == "b":
                    a =AIPlayer (5,
                                        [x*self.tileSize + self.tileSize/2,
                                         y*self.tileSize + self.tileSize/2])
                    print "ai", a.containers
                if c == "p":
                    p =Player (5,  
                                        [x*self.tileSize + self.tileSize/2,
                                         y*self.tileSize + self.tileSize/2])
                    print "play",p.containers   
                                    
                if c in "x" :       #Pew
                    Enemy(2,
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)

                if c in "y" :       #Beatbox
                    ShootingEnemy(1,
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  
                            
                if c == "o":
                    Meatball([x*self.tileSize + self.tileSize/2,
                                           y*self.tileSize + self.tileSize/2],
                                          self.tileSize)

                if c == "s":
                    Specialmeatball([x*self.tileSize + self.tileSize/2,
                                           y*self.tileSize + self.tileSize/2],
                                          self.tileSize)
                                
                #if c == "$":
                    #Goal([x*self.tileSize + self.tileSize/2,
                                          #y*self.tileSize + self.tileSize/2],
                                          #self.tileSize)

        
#Level("level1.lvl")
