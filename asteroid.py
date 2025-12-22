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
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            d1 = self.velocity.rotate(angle)
            d2 = self.velocity.rotate(0 - angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = d1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = d2 * 1.2

        
