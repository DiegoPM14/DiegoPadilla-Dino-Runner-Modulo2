import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    BIRD_HEIGHTS = [225, 250, 290, 320]
    def __init__(self, image):
        self.step_index= 0
        image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)

   