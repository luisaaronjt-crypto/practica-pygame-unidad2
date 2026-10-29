import pygame
pygame.init()
pantalla = pygame.display.set_mode((800,600))
fuente = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

jugador = pygame.Rect(100,100,50,50)
moneda = pygame.Rect(400,300,30,30)
puntos=0

run=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
    teclas=pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: jugador.x-=5
    if teclas[pygame.K_RIGHT]: jugador.x+=5
    if teclas[pygame.K_UP]: jugador.y-=5
    if teclas[pygame.K_DOWN]: jugador.y+=5

    if jugador.colliderect(moneda):
        puntos+=1
        moneda.x = pygame.time.get_ticks() % 700 + 50
        moneda.y = pygame.time.get_ticks() % 500 + 50

    pantalla.fill((20,20,20))
    pygame.draw.rect(pantalla, (0,255,0), jugador)
    pygame.draw.rect(pantalla, (255,215,0), moneda)
    txt=fuente.render(f"Puntos: {puntos}", True, (255,255,255))
    pantalla.blit(txt, (10,10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
