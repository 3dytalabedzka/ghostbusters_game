import pygame, random
from pygame.locals import *

class Road:
    '''
    Class describing moving background
    '''
    def __init__(self):
        road_1 = pygame.image.load("images/bg_1.png")
        road_2 = pygame.image.load("images/bg_2.png")
        road_3 = pygame.image.load("images/bg_3.png")
        self.images = [road_1, road_2, road_3]
        self.x = 0
        self.first_bg_y = 0
        self.rect_bg = self.images[0].get_rect()
        self.height = self.rect_bg.height
        self.second_bg_y = self.height
        self.move_speed = 6
        self.first = 0
        self.second = 1

    def upgrade(self):
        '''
        Function combines two images and adds new images
        to complete whole changing background, moves it down
        '''
        self.first_bg_y += self.move_speed
        if self.first_bg_y >= self.height:
            self.first_bg_y = -self.height
            self.first = random.randint(0,2)
        self.second_bg_y += self.move_speed
        if self.second_bg_y >= self.height:
            self.second_bg_y = -self.height
            self.second = random.randint(0,2)