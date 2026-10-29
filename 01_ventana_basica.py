import pygame
pygame.init()

# Ventana básica - base de todo juego
VENTANA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("01 - Ventana Básica Pygame")
clock = pygame.time.Clock()

jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
    
    VENTANA.fill((30, 30, 80)) # fondo azul oscuro
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
