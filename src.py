import pygame
import random
import math
from pygame.locals import *
from sys import exit
from pygame import mixer

# initializing pygame
pygame.init()

# creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,
								screen_height))

background = pygame.image.load('resources/back.png').convert()
sprite = pygame.image.load('resources/play.png').convert_alpha()

# caption and icon
pygame.display.set_caption("Welcome to RetardedMan\
 by:- CIA")

font = pygame.font.Font('resources/DejaVuSans-Bold.ttf', 20)

# Game Over
game_over_font = pygame.font.Font('resources/DejaVuSans-Bold.ttf', 64)

score = 100
health = 60
damage = 50
health - damage > 0

class nigger(object):
    
    def __init__(self, armor, shells):
         self.name = name
         self.armor = armor
         self.image = play
         self.location = nigger(0, 0)
         self.destination = nigger(0, 0)
         self.speed = 0.
         
         self.brain = StateMachine()
         
         self.id = 0
         
    def render(self, surface):
        
        armor,shells = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x-w/2, y-h/2))
 
    def process(self, time_passed):
        
        self.brain.think()
        
        if self.speed > 0 and self.location != self.destination:     
        
         vec_to_destination = self.destination - self.location
         distance_to_destination = vec_to_destination.get_length()
         heading = vec_to_destination.get_normalized()
         travel_distance = min(distance_to_destination, time_passed * self.speed)
         self.location += travel_distance * heading
         
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
    
    @classmethod
    def from_name(cls, armor, shells):
        return nigger(cls, armor[0] - armor[0], armor[1] - armor[1])
    
    def get_magnitude(self):
        return math.sqrt( self.armor**2 + self.shells**2 )
    
    def normalize(self):
        magnitude = self.get_magnitude()
        self.armor /= magnitude
        self.shells /= magnitude

pressed_keys = pygame.key.get_pressed()
if pressed_keys[K_SPACE]:
   fire()

pygame.display.update()
