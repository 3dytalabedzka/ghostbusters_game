import pygame, sys, pickle
from pygame.locals import *
from game import Game
 
White=(255,255,255)
Grey=(100,100,100)

class Menu:
    '''
    Class representing main menu
    '''
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512) 
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.game = Game()
        self.menu_font = pygame.font.SysFont("monospace", 40)

        self.green = pygame.image.load("images/green.png")
        self.ghost1 = pygame.image.load("images/ghost_lv1.png")
        self.ghost2 = pygame.image.load("images/ghost_lv2.png")
        self.ghost3 = pygame.image.load("images/ghost_lv3.png")
        self.buster = pygame.image.load("images/buster_menu.png")
        self.car = pygame.image.load("images/bad_car_1.png")
        self.gear = pygame.image.load("images/gear.png")
        self.busters_image = pygame.image.load("images/little_busters.png")

    def button(self,text,xb,yb,xt,yt,function=None):
        '''
        Function creating buttons
        '''
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed() 
        if xb+275 > mouse[0] > xb and yb+100 > mouse[1] > yb:
            pygame.draw.rect(self.game.screen, (102,102,153),(xb,yb,275,100))
            if clicked[0] and function != None:
                function()
        else:
            pygame.draw.rect(self.game.screen, (0,51,102),(xb,yb,275,100))
        t = self.menu_font.render(text, True, White)
        self.game.screen.blit(t, (xt,yt))

    def menu(self):
        '''
        Function making main menu, buttons with functions the call,
        lets player start the game or exit it
        '''
        while True:
            if self.game.the_end:
                self.game = Game()
                self.menu()

            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT or pressed_keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.game.screen.fill((0,0,0))
            
            self.game.screen.blit(self.green, (0,405))
            self.game.screen.blit(self.ghost2, (300,500))
            self.game.screen.blit(self.ghost2, (200,530))
            self.game.screen.blit(self.ghost2, (500,530))
            self.game.screen.blit(self.buster, (50,480))

            self.button("START",50,10,130,38,self.game.Run_game)
            self.button("PODIUM",375,10,443,38,self.rating)
            self.button("RULES",50,160,130,188,self.rules)
            self.button("EXIT",375,160,465,188,self.exit)
            self.button("OPTIONS",50,305,105,338,self.options)
            self.button("AUTHOR",375,305,443,338,self.author)

            pygame.display.update()

    def rating(self):
        '''
        After pressing button 'PODIUM'
        displays screen with 5 top scores
        '''
        while True:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT or pressed_keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.game.screen.fill((0,0,0))

            best_scores = []

            infile = open("highscore", "rb")
            best_scores = pickle.load(infile)
            infile.close()
            title = self.menu_font.render("Ranking", True, White)
            first = self.game.myfont.render("1. "+str(best_scores[0]), True, White)
            second = self.game.myfont.render("2. "+str(best_scores[1]), True, White)
            third = self.game.myfont.render("3. "+str(best_scores[2]), True, White)
            forth = self.game.myfont.render("4. "+str(best_scores[3]), True, White)
            fifth = self.game.myfont.render("5. "+str(best_scores[4]), True, White)
            self.game.screen.blit(title, (280,20))
            self.game.screen.blit(first, (20,100))
            self.game.screen.blit(second, (20,160))
            self.game.screen.blit(third, (20,220))
            self.game.screen.blit(forth, (20,280))
            self.game.screen.blit(fifth, (20,340))

            self.game.screen.blit(self.game.trophy, (400,100))
            self.game.screen.blit(self.game.star, (250,250))
            self.game.screen.blit(self.game.star, (20,450))

            self.button("MENU",212,480,300,502,self.menu)

            pygame.display.update()

    def rules(self):
        '''
        After pressing button 'RULES'
        displays screen with rules of the game
        '''
        while True:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT or pressed_keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.game.screen.fill((0,0,0))

            rule1 = self.game.myfont.render("In this game you're a ghost hunter!", True, White)
            rule6 = self.game.myfont.render("While driving you have to catch ghosts", True, White)
            rule2 = self.game.myfont.render("but watch out for other cars!", True, White)
            rule3 = self.game.myfont.render("You can use <- -> or A D to move sideways", True, White)
            rule4 = self.game.myfont.render("catching a ghost           collision -1 live", True, White)
            rule5 = self.game.myfont.render("100 pt   150 pt   200 pt", True, White)
            self.game.screen.blit(rule1, (10,10))
            self.game.screen.blit(rule6, (10,70))
            self.game.screen.blit(rule2, (10,130))
            self.game.screen.blit(rule3, (10,190))
            self.game.screen.blit(rule4, (10,250))
            self.game.screen.blit(rule5, (10,310))
            self.game.screen.blit(self.ghost1, (30,370))
            self.game.screen.blit(self.ghost2, (160,370))
            self.game.screen.blit(self.ghost3, (290,370))
            self.game.screen.blit(self.car, (500,310))

            self.button("MENU",212,480,300,502,self.menu)

            pygame.display.update()

    def exit(self):
        pygame.quit()
        sys.exit()
    
    def options(self):
        '''
        Function providing player option to change steering,
        advancement level and turn on siren in car
        '''
        while True:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT or pressed_keys[K_ESCAPE]: 
                    pygame.quit()
                    sys.exit()
                if pressed_keys[K_1]:
                    self.game.min_time = 40
                    self.game.max_time = 70
                    self.game.lives = 1
                if pressed_keys[K_2]:
                    self.game.min_time = 60
                    self.game.max_time = 120
                    self.game.lives = 3
                if pressed_keys[K_3]:
                    self.game.control_left = K_LEFT
                    self.game.control_right = K_RIGHT
                if pressed_keys[K_4]:
                    self.game.control_left = ord('a')
                    self.game.control_right = ord('d')
                if pressed_keys[K_5]:
                    self.game.car.siren = True
                if pressed_keys[K_6]:
                    self.game.car.siren = False
                
            self.game.screen.fill((0,0,0))

            if self.game.lives == 3:
                poziom = "easy"
            else:
                poziom = "hard"

            option1_text1 = self.game.myfont.render("Hard mode: press '1', easy mode: '2'", True, White)
            option1_text2 = self.game.myfont.render("(in hard you only get 1 live)", True, White)
            option1 = self.game.myfont.render("DIFFICULTY LEVEL : "+poziom, True, White)
            self.game.screen.blit(option1_text1, (10,10))
            self.game.screen.blit(option1_text2, (10,60))
            self.game.screen.blit(option1, (150,110))

            if self.game.control_left == K_LEFT:
                ster = "<-  ->"
            else:
                ster = "A    D"

            option2_text1 = self.game.myfont.render("To use arrow keys, press '3'", True, White)
            option2_text2 = self.game.myfont.render("for A D press '4'", True, White)
            option2 = self.game.myfont.render("STEERING : "+ster, True, White)
            self.game.screen.blit(option2_text1, (10,180))
            self.game.screen.blit(option2_text2, (10,230))
            self.game.screen.blit(option2, (150,280))

            if self.game.car.siren == True:
                syrena = "on"
            else:
                syrena = "off"

            option3_text1 = self.game.myfont.render("To turn on siren, press '5',to turn off: '6'", True, White)
            option3 = self.game.myfont.render("SIREN : "+syrena, True, White)
            self.game.screen.blit(option3_text1, (10,350))
            self.game.screen.blit(option3, (150,400))
           
            self.game.screen.blit(self.gear, (580,430))

            self.button("MENU",212,480,300,502,self.menu)
            
            pygame.display.update()

    def author(self):
        '''
        Function providing screen with info about author
        '''
        while True:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT or pressed_keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.game.screen.fill((0,0,0))

            text1 = self.game.myfont.render("Hey, my name is Edyta Łabędzka and this is", True, White)
            text2 = self.game.myfont.render("my first game. It can be noticed that I'm ", True, White)
            text3 = self.game.myfont.render("quite fond of 'Ghostbusters'. I once thought", True, White)
            text4 = self.game.myfont.render("it would be a nice theme for a game and here", True, White)
            text5 = self.game.myfont.render("it is. I hope that you will enjoy the game.", True, White)
            text6 = self.game.myfont.render("GOOD LUCK!", True, White)
            self.game.screen.blit(text1, (10,10))
            self.game.screen.blit(text2, (10,70))
            self.game.screen.blit(text3, (10,130))
            self.game.screen.blit(text4, (10,190))
            self.game.screen.blit(text5, (10,250))
            self.game.screen.blit(text6, (10,310))
            
            self.game.screen.blit(self.busters_image, (350,350))

            self.button("MENU",212,480,300,502,self.menu)

            pygame.display.update()
            
if __name__ == "__main__" :
    start_game = Menu()
    start_game.menu()
