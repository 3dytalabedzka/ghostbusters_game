import pygame, sys, random, pickle
from pygame.locals import *
from car import Car
from ghost import Ghost
from driver import Driver
from road import Road
 
White=(255,255,255)
Grey=(100,100,100)

class Game:
    '''
    Main class describing game, uses classes 
    describing player, spites and background 
    to spawn those objects
    '''
    def __init__(self):
        self.car = Car()
        self.road = Road()

        self.the_end = False

        self.fps = 60 
        self.clock = pygame.time.Clock()

        self.ghosts = pygame.sprite.Group()
        self.ghost_respawn = 60

        self.drivers = pygame.sprite.Group()
        self.driver_respawn = 60
        self.driver_respawn_update = 0
        self.min_time = 60
        self.max_time = 120

        self.lives = 3
        self.score = 0

        self.control_left = K_LEFT
        self.control_right = K_RIGHT

        self.myfont = pygame.font.SysFont("monospace", 25)
        self.lives_text = self.myfont.render("LIVES", True, (255,255,255))
        self.score_text = self.myfont.render("POINTS", True, (255,255,255))
        self.score_counter = self.myfont.render(str(self.score), True, (255,255,255))

        self.car_crash = pygame.mixer.Sound("music/car_crash.wav")
        self.ghost_vacuum = pygame.mixer.Sound("music/ghost.wav")
        self.game_over = pygame.mixer.Sound("music/game_over.wav")
        pygame.mixer.music.set_volume(0.1)
        self.car_crash.set_volume(0.4)
        self.ghost_vacuum.set_volume(0.6)
        self.game_over.set_volume(0.6)
        pygame.mixer.music.load("music/Ghostbusters_remix.mp3")
        pygame.mixer.music.play(-1)
        
        self.screen = pygame.display.set_mode((700,600))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0, 0))
        pygame.display.set_caption("Gostbusters") 
        
        self.icon = pygame.image.load("images/ghost_lv1.png")
        pygame.display.set_icon(self.icon)

        self.heart = pygame.image.load("images/heart.png")
        self.trophy = pygame.image.load("images/trophy.png")
        self.grave = pygame.image.load("images/grave.png")
        self.star = pygame.image.load("images/star.png")

    def Lives(self):
        '''
        Function detecting collisions, handles player lives
        '''
        collisions = pygame.sprite.spritecollide(self.car, self.drivers, True)
        for driver in collisions:
            pygame.mixer.Sound.play(self.car_crash)
            self.lives -= 1
        if self.lives == 3:
            self.screen.blit(self.heart, (450,160))
            self.screen.blit(self.heart, (525,160))
            self.screen.blit(self.heart, (600,160))
        elif self.lives == 2:
            self.screen.blit(self.heart, (450,160))
            self.screen.blit(self.heart, (525,160))
        elif self.lives == 1:
            self.screen.blit(self.heart, (450,160))

    def Score(self):
        '''
        Function counting points
        '''
        collisions = pygame.sprite.spritecollide(self.car, self.ghosts, True)
        for ghost in collisions:
            pygame.mixer.Sound.play(self.ghost_vacuum)
            self.score += ghost.points
        self.score_counter = self.myfont.render(str(self.score), True, (255,255,255))
    
    def Faster_respawn(self):
        '''
        Function makes spawning cars more frequent 
        as the game continues (so game is more challenging
        as the time goes by)
        '''
        if self.driver_respawn_update == 200:
            if self.min_time <= 20:
                self.min_time = 20
            else:
                self.min_time -= 1
            if self.max_time <= 30:
                self.max_time = 30
            else:
                self.max_time -= 2
            self.driver_respawn_update = 0

    def Scoreboard(self, end_score):
        '''
        Function in charge of scoreboard
        keeps top scores in 'highscore' file 
        !!!(If you want to start without highscore you just have to remove highscore.py)
        shows end message 
        '''
        best_scores = []

        infile = open("highscore", "rb")
        best_scores = pickle.load(infile)
        infile.close()

        best_scores.append(end_score)
        best_scores = sorted(best_scores, reverse=True)
        best_scores.remove(best_scores[-1])

        if end_score in best_scores:
            text_game_over = self.myfont.render("Congratulations, you're "+str(best_scores.index(end_score)+1)+", points "+str(end_score), True, White)
            self.screen.blit(self.trophy, (300,300))
            self.screen.blit(self.star, (50,50))
            self.screen.blit(self.star, (550,500))
        else:
            text_game_over = self.myfont.render("GAME OVER   your score: "+str(end_score), True, White)
            self.screen.blit(self.grave, (250,300))
        self.screen.blit(text_game_over, (50,200))

        outfile = open("highscore", "wb")
        pickle.dump(best_scores, outfile)
        outfile.close()
    
    def Game_over(self):
        '''
        Function checks if player lost all the lives,
        ends game if so
        '''
        if self.lives <= 0:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(self.game_over)
            self.screen.fill((0,0,0))
            self.Scoreboard(self.score)
            pygame.display.update()
            pygame.time.delay(4500)
            self.the_end = True

    def Run_game(self):
        '''
        Main function calling all the other function when game starts
        produces sprites and moves them, counts time
        '''
        while not self.the_end:
            
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == QUIT or pressed_keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                if pressed_keys[self.control_left]:
                    self.car.move_left()
                if pressed_keys[self.control_right]:
                    self.car.move_right()

            self.ghost_respawn -= 1
            if self.ghost_respawn == 0:
                self.ghosts.add(Ghost())
                self.ghost_respawn = random.randint(50,100)

            for ghost in self.ghosts:
                if ghost.rect.top > 540:
                    self.ghosts.remove(ghost)

            self.driver_respawn -= 1
            if self.driver_respawn == 0:
                self.drivers.add(Driver())
                self.driver_respawn = random.randint(self.min_time,self.max_time)
            
            for driver in self.drivers:
                if driver.rect.top > 550:
                    self.drivers.remove(driver)
            
            self.driver_respawn_update += 1

            self.background.blit(self.road.images[self.road.first],(self.road.x, self.road.first_bg_y))
            self.background.blit(self.road.images[self.road.second],(self.road.x, self.road.second_bg_y))
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.car.car_image,self.car.rect)
            self.screen.blit(self.score_text, (500, 10))
            self.screen.blit(self.score_counter, (520, 60))
            self.screen.blit(self.lives_text, (430, 110))
            self.car.siren_on()
            self.Lives()
            self.Score()
            self.Faster_respawn()
            self.Game_over()
            self.ghosts.update()
            self.ghosts.draw(self.screen)
            self.drivers.update()
            self.drivers.draw(self.screen)
            self.road.upgrade()
            pygame.display.flip()
            self.clock.tick(self.fps)
