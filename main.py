# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                sys.exit()
            for s in shots:
                if a.collision(s):
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()