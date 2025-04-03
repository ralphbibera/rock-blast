import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from ui import draw_card, draw_item
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    dt = 0

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for sprite in asteroids:
            if sprite.collide(player):
                if player.lives == 1:
                    print("Game Over!")
                    return

                player.lives -= 1
                player.position = pygame.Vector2(
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

            for shot in shots:
                if sprite.collide(shot):
                    sprite.split()
                    shot.kill()
                    player.score += 1

        screen.fill("black")

        draw_card(screen, f"Score: {player.score}", "white", (10, 10))
        draw_card(screen, f"Lives: {player.lives}", "white", (SCREEN_WIDTH - 80, 10))

        draw_item(screen, f"Score: {player.score}", "white", (80, 80))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
