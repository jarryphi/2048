import pygame

def text_to_screen(screen, text, x, y, size = 50,
        color = (255, 255, 255)):
        text = str(text)
        font = pygame.font.SysFont('Comic Sans Ms', 30)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
