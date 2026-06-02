import pygame

pygame.init()

font = pygame.font.SysFont("Times new Roman", 36)
# Display
screen=pygame.display.set_mode((600, 500))

# Caption
text = font.render("My First Gaming Screen" ,True, (125, 0, 255))

# Colours
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
          done=True
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(250, 190, 30, 60))
    screen.blit(text, (150, 250))

    pygame.display.flip()