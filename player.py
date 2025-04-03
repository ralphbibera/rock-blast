import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *
import math


class Player(CircleShape):
    last_shot_cooldown = 0
    score = 999
    lives = 3
    firerate_level = FIRERATE_BASE_LEVEL
    firerate_cost = FIRERATE_COST
    multi_shot_level = MULTI_SHOT_BASE_LEVEL
    multi_shot_cost = MULTI_SHOT_COST

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.last_shot_cooldown -= dt

        if keys[pygame.K_1]:
            if self.score >= self.firerate_cost and self.firerate_level < MAX_FIRERATE_LEVEL:
                self.score -= self.firerate_cost
                self.firerate_level += 1
                self.firerate_cost += FIRERATE_COST * 0.5

        if keys[pygame.K_2]:
            if self.score >= self.multi_shot_cost and self.multi_shot_level < MAX_MULTI_SHOT_LEVEL:
                self.score -= self.multi_shot_cost
                self.multi_shot_level += 1
                self.multi_shot_cost += MULTI_SHOT_COST * 0.5

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.last_shot_cooldown > 0:
                return
            self.shoot()
            self.last_shot_cooldown = PLAYER_SHOOT_COOLDOWN - \
                (self.firerate_level - 1) * 0.1

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH

        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(
            self.rotation) * PLAYER_SHOOT_SPEED

        if self.multi_shot_level > 1:
            for i in range(self.multi_shot_level):
                shot = Shot(self.position.x, self.position.y)
                shot.velocity = pygame.Vector2(0, 1).rotate(
                    self.rotation + (i * 360 / self.multi_shot_level)) * PLAYER_SHOOT_SPEED
