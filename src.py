import pygame
import random
import math
from pygame import mixer

# initializing pygame
pygame.init()

# creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,
								screen_height))

# caption and icon
pygame.display.set_caption("Welcome to RetardedMan\
 by:- CIA")

font = pygame.font.Font('resources/DejaVuSans-Bold.ttf', 20)

# Game Over
game_over_font = pygame.font.Font('resources/DejaVuSans-Bold.ttf', 64)

score = 100
health = 60
damage = 50
score != 100
health - damage > 0

class nigger(object):
    def __str__(self):
        
        if self.alive:
           return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
           return "%s (DEAD)" % self.name
       
    def fire_at(self, enemy):

        if self.ammo >= 1:
            self.ammo -= 1
            self.name, "fires on", enemy.name
            enemy.hit()
        else:
            self.name, "has no shells!"

    def hit(self):

        self.armor -= 20
        self.name, "is hit!"
        if self.armor <= 0:
            self.explode()
            
    def explode(self):

        self.alive = False
        self.name, "explodes!"
        
    pygame.display.update()
