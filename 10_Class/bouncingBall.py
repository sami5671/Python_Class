import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

ball = pygame.image.load("ball.jpg")
ballRect = ball.get_rect()


speed = [0, 1]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # ball bouncing code
    ballRect = ballRect.move(speed)
    if ballRect.left < 0 or ballRect.right > 600:
        speed[0] = -speed[0]
    if ballRect.top < 0 or ballRect.bottom > 600:
        speed[1] = -speed[1]

    screen.fill((255, 255, 255))
    screen.blit(ball, ballRect)
    pygame.display.flip()
