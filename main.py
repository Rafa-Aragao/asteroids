import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    speeding_up = 0
    score = 0
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    speeds_up = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, drawables, speeds_up)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)
        speeds_up.update(speeding_up)
        for i in asteroids:
            if player.check_collisions(i) == True:
                print("Game Over!")
                print(f"You scored: {score}")
                exit()

               
                
        for i in asteroids:
            for n in shots:
                if n.check_collisions(i):
                    i.split()
                    score += 1
        screen.fill("black")
        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
        screen.blit(score_text, (10, 10)) 
       
        for i in drawables:
            i.draw(screen)
        pygame.display.flip()
        speed_up_rate = 0.1
        dt = clock.tick(60) / 1000
        speeding_up = (clock.tick(60) / 1000) + speed_up_rate
        speed_up_rate += 0.5
        


if __name__ == "__main__":
    main()
