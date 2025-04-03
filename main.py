import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from ui import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

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

    topleft = Group(
        screen,
        [
            Card(screen, 40),
            Card(screen, 40)
        ],
        GroupPosition.TOP_LEFT,
    )

    topright = Group(
        screen,
        [
            Card(screen, 90, 24),
            Card(screen, 90, 24)
        ],
        GroupPosition.TOP_RIGHT,
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for sprite in asteroids:
            if sprite.collided(player):
                sprite.split()
                if player.lives == 1:
                    print("Game Over! Your score was", player.score)
                    return
                player.lives -= 1
                player.position = pygame.Vector2(
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

            for shot in shots:
                if shot.collided(sprite):
                    shot.kill()
                    sprite.split()
                    player.score += 1

        topleft.cards[0].update(f"Lives: {player.lives}")
        topleft.cards[1].update(f"Score: {player.score}")
        topright.cards[0].update(
            f"Fire Rate: {player.firerate_level}\nCost: {player.firerate_cost}\n{'MAX' if player.firerate_level >= MAX_FIRERATE_LEVEL else 'Press 1\nto upgrade'}")
        topright.cards[1].update(
            f"Multi-shot: {player.multi_shot_level}\nCost: {player.multi_shot_cost}\n{'MAX' if player.multi_shot_level >= MAX_MULTI_SHOT_LEVEL else 'Press 2\nto upgrade'}")

        screen.fill("black")

        UI.render()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

        AsteroidField.spawn_rate = max(
            0.1, AsteroidField.spawn_rate - (player.score // 200) * 0.1)


if __name__ == "__main__":
    main()
