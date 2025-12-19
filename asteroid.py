import random
from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if not self.radius <= ASTEROID_MIN_RADIUS:
            log_event("asteroid_spit") 
        
