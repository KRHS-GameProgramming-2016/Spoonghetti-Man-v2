import pygame, sys, math
from Player  import *
from AIPlayer  import *
from Enemy import *
from ShootingEnemy import *
from Wall import *
from Meatball import *
from specialmeatball import *

class Level():
    def __init__(self, levelFile, tileSize=44):
        self.walls = []
        self.meatballs = []
        self.tileSize = tileSize
        self.playerSize = tileSize = 10
        self.loadLevel(levelFile)
    
    def unloadLevel(self):
        self.walls = []
      
               
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
                    self.walls += [Wall([x*self.tileSize + self.tileSize/7,
                                        y*self.tileSize + self.tileSize/7],
                                       self.tileSize)
                                  ]
                                  
                if c == "b":
                    self.player2 = AIPlayer (5,
                                        [x*self.tileSize + self.tileSize/10,
                                         y*self.tileSize + self.tileSize/10])
                if c == "p":
                    self.player = Player (5,  
                                        [x*self.tileSize + self.tileSize/.2,
                                         y*self.tileSize + self.tileSize/.2])
                if c == "o":
                    self.meatballs += [Meatball([x*self.tileSize + self.tileSize/2,
                                           y*self.tileSize + self.tileSize/2],
                                          self.tileSize)
                                       ]
                if c == "s":
                    self.meatballs += [Specialmeatball([x*self.tileSize + self.tileSize/2,
                                           y*self.tileSize + self.tileSize/2],
                                          self.tileSize)
                                ]
                #if c == "$":
                    #self.goal = Goal([x*self.tileSize + self.tileSize/2,
                                          #y*self.tileSize + self.tileSize/2],
                                          #self.tileSize)
                   
                    print "MEAATBALL!!!!"

        
#Level("level1.lvl")
