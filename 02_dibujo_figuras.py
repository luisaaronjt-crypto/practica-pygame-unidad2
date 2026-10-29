import pygame
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("02 - Dibujando Figuras")
clock = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run=False
    
    pantalla.fill((20,20,20))
    # Dibujos
    pygame.draw.circle(pantalla, (255,255,0), (400,300), 100) # cara
    pygame.draw.circle(pantalla, (0,0,0), (370,280), 10) # ojo
    pygame.draw.circle(pantalla, (0,0,0), (430,280), 10)
    pygame.draw.rect(pantalla, (0,0,0), (360,330,80,10)) # boca
    pygame.draw.line(pantalla, (255,0,0), (0,0), (800,600), 5)

    texto = fuente.render("Pygame puede dibujar todo", True, (255,255,255))
    pantalla.blit(texto, (250, 50))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
