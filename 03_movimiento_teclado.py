import pygame
pygame.init()
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("03 - Movimiento con Teclado")
clock = pygame.time.Clock()

x, y = 400, 300
vel = 5

run=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]: x-=vel
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: x+=vel
    if teclas[pygame.K_UP] or teclas[pygame.K_w]: y-=vel
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]: y+=vel

    pantalla.fill((40,40,40))
    pygame.draw.rect(pantalla, (0,200,255), (x,y,50,50))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
