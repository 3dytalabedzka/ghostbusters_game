import pygame
from pygame.locals import *

class Car(pygame.sprite.Sprite):
    '''
    Class describing player (car), as moving object in game
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.car_image = pygame.image.load("images/smol_car.png")

        self.car_siren_1 = pygame.image.load("images/car_siren_1.png")
        self.car_siren_2 = pygame.image.load("images/car_siren_2.png")
        self.siren = False
        self.siren_flag = 0
        self.siren_time = 0

        self.rect = self.car_image.get_rect()
        self.car_x = 46
        self.car_y = 480
        self.rect.move_ip(self.car_x, self.car_y)
        self.speed_x = 83

    def move_right(self):
        '''
        Function allowing to change laneont to right 
        makes sure to keep car on the street
        '''
        self.rect = self.rect.move(self.speed_x, 0)
        if self.rect.left > 295:
            self.rect.left = 295 
            
    def move_left(self):
        self.rect = self.rect.move(-self.speed_x, 0)
        if self.rect.left < 46:
            self.rect.left = 46 
    
    def siren_on(self):
        '''
        Function letting to use siren in car
        only visual efect 
        '''
        if self.siren == True:
            self.siren_time += 1
            if self.siren_time == 5:
                if self.siren_flag == 0:
                    self.siren_flag = 1
                    self.car_image = self.car_siren_1
                else:
                    self.car_image = self.car_siren_2
                    self.siren_flag = 0
                self.siren_time = 0

        