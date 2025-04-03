import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(30, 60)
            self.spawn(random_angle)
            self.spawn(-random_angle)
            self.spawn(0)
        self.kill()

    def spawn(self, angle):
        asteroid = Asteroid(
            self.position.x,
            self.position.y,
            self.radius - ASTEROID_MIN_RADIUS,
        )
        asteroid.velocity = self.velocity.rotate(angle) * 1.5
