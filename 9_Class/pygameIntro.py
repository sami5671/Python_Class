# 1. importing pygame
import pygame

# 2. pygame initialize
pygame.init()


#  screen (x, y axis )
screen = pygame.display.set_mode((700, 400))


# 3. game loop

while True:
    screen.fill((255, 224, 162, 255))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
