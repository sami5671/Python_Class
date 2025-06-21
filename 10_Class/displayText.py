import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Hello Pygame World")

font = pygame.font.SysFont("myanmartext", 30, italic=True, bold=True)

text = font.render("My First Pygame", True, (255, 255, 255))
textRect = text.get_rect()

textRect.center = (600 // 2, 600 // 2)


# game loop
while True:
    screen.fill((179, 66, 245))
    screen.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
