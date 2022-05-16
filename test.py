import pgzrun
import random
import pygame
import sys
import os
import time

mod = sys.modules['__main__']

WIDTH = 600 
HEIGHT = 400
TITLE = "Roguelike"
FPS = 30
q = 0

char = mod.Actor("stand1", (100, 100))

def draw():
    mod.screen.fill("blue")
    char.draw()

def update(dt):
    global q
    if mod.keyboard.RIGHT:
        for i in range(10):
            if q == 0:
                char.image = "stand1"            
                q += 1
            elif q == 1:
                char.image = 'right1'            
                q += 1
            elif q == 2:
                char.image = 'right2'            
                q -= 2
        
            char.x += 1
            # time.sleep(0.1)
        
    


pgzrun.go()