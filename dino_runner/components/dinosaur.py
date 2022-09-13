import pygame
from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5
    DUCK_VEL = 8.5
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = self.JUMP_VEL
        self.duck_vel = self.DUCK_VEL

    def update(self, user_input):
       
       if self.dino_run: 
          self.run()
       elif self.dino_jump:
             self.jump()
       elif self.dino_duck:
            self.duck()
        
       if user_input[pygame.K_UP] and not self.dino_jump:
          self.dino_jump = True
          self.dino_run = False
          self.dino_duck = False
       elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck= False

       if user_input[pygame.K_DOWN] and not self.dino_duck:     
          self.dino_jump = False
          self.dino_run = False
          self.dino_duck= True
       elif not self.dino_duck:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck= False

       if self.step_index >=10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index<5 else RUNNING[1]
        self.dino_rect =self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index +=1

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_vel *4

        self.jump_vel -= 0.8

        if self.jump_vel < -8.5:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = DUCKING
        self.dino_rect.y = self.duck_vel * 4

        self.duck_vel -=0.8

        if self.duck_vel<- 8.5:
            self.dino_rect.y = self.Y_POS
            self.dino_duck = False
            self.duck_vel= self.DUCK_VEL

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
        