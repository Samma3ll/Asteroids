import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player, Bullet
from asteroid import Asteroid
from asteroidfied import AsteroidField


def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"updatable: {updatable}")
    print(f"drawable: {drawable}")
    print(f"asteroids: {asteroids}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for i in asteroids:
            if i.colliding(player):
                sys.exit("Game over!")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        time = clock.tick(60)
        dt = time / 1000


if __name__ == "__main__":
    main()
