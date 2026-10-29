import pygame
pygame.init()
pantalla=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

x,y=100,500
vy=0
gravedad=0.6
anim=0

run=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE and y>=500:
            vy=-15

    teclas=pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]: x+=5; anim+=1
    if teclas[pygame.K_LEFT]: x-=5; anim+=1

    vy+=gravedad
    y+=vy
    if y>500: y=500; vy=0

    pantalla.fill((135,206,235))
    pygame.draw.rect(pantalla,(100,50,0),(0,550,800,50)) # suelo
    color = (255,0,0) if anim%20<10 else (200,0,0)
    pygame.draw.rect(pantalla,color,(x,y,40,50))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
