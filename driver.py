import pygame, random
from pygame.locals import *

class Driver(pygame.sprite.Sprite):
    '''
    Class describing oponents - in game other cars
    chooses random lane that car moves on also speed and color of the car
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        car_1 = pygame.image.load("images/bad_car_1.png")
        car_2 = pygame.image.load("images/bad_car_2.png")
        car_3 = pygame.image.load("images/bad_car_3.png")
        self.car_images = [car_1, car_2, car_3]  
        self.car_color = random.randint(0,2) 
        self.image = self.car_images[self.car_color]
        self.rect = self.image.get_rect() 
        self.bad_car_x = random.choice([46, 129, 212, 295])
        self.bad_car_y = -100
        self.rect.move_ip(self.bad_car_x, self.bad_car_y)
        self.speed = random.randint(8,10)

    def update(self):
        '''
        Function that moves drives on the screen
        '''
        self.rect = self.rect.move(0, self.speed)