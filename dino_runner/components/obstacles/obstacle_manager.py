import pygame
import random
from dino_runner.components.obstacles import bird

from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus


class ObstacleManager:
    def __init__(self):
        self.obstacles= []

    def update(self, game ):
        if len(self.obstacles)==0:
            if random.randint(0,2)== 0:                
                cactus = SmallCactus(SMALL_CACTUS) 
                self.obstacles.append(cactus)
            elif random.randint(0,2)== 1:
                cactus = LargeCactus(LARGE_CACTUS)
                self.obstacles.append(cactus) 
           ## elif random.randint(0,2)== 2:
             ##   bird = Bird(BIRD)
               ## self.obstacles.append(bird)   

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("you crashed")
                pygame.time.delay(1000)
                game.playing = False
                
            break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)