import pygame

def main():
    pygame.init()
    s_w, s_h = 500, 500
    screen = pygame.display.set_mode((s_w, s_h))
    pygame.display.set_caption('color changing sprite')

    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white'),
    }
    current_color = colors['white']

    x, y = 30, 30
    w, h = 60, 60

    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0, x), s_w - w)
        y = min(max(0, y), s_h - h)

        if x == 0: current_color = colors['blue']
        elif x == s_w - w: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == s_h - h: current_color = colors['green']
        else:
            current_color = colors['white']
            
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,(x, y, w, h))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()
        
if __name__ == "__main__":
    main()