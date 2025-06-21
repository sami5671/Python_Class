import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                print("0 printed")
            elif event.key == pygame.K_a:
                print("a printed")
            else:
                print("something happen")
