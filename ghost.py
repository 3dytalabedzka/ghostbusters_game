import pygame, random
from pygame.locals import *

class Ghost(pygame.sprite.Sprite):
    '''
    Class representing objects giving players points (ghosts)
    chooses random level of ghost and its speed
    as well as place where it spawns
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ghost_1 = pygame.image.load("images/ghost_lv1.png")
        ghost_2 = pygame.image.load("images/ghost_lv2.png")
        ghost_3 = pygame.image.load("images/ghost_lv3.png")
        self.ghost_images = [ghost_1, ghost_2, ghost_3]  
        self.g_level = random.randint(0,2) 
        if self.g_level == 0:
            self.points = 100
        elif self.g_level == 1:
            self.points = 150
        else:
            self.points = 200
        self.image = self.ghost_images[self.g_level]
        self.rect = self.image.get_rect() 
        self.ghost_x = random.randint(35,300)
        self.ghost_y = -60
        self.rect.move_ip(self.ghost_x, self.ghost_y)
        self.speed_y = random.randint(7,12)
        self.speed_x = 0
        
    def update(self):
        '''
        Function moves ghost randomly along x asis
        and steadily along y, making sure its stays on screen
        '''
        self.speed_x = random.choice([-10, 0, 10])
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if self.rect.left < 46:
            self.rect.left = 46 
        if self.rect.left > 295:
            self.rect.left = 295