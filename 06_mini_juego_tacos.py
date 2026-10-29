import pygame, random, sys
pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("LLUVIA DE TACOS - Edicion Jarocha 🌮")
clock = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 28, bold=True)
fuente_big = pygame.font.SysFont("Arial", 50, bold=True)

# Colores
BLANCO = (255,255,255)
ROJO_CHILE = (220,20,60)

jugador = pygame.Rect(ANCHO//2, ALTO-80, 100, 20)
vidas = 3
puntos = 0
vel_jugador = 8
vel_caida = 3

class Objeto:
    def __init__(self):
        self.x = random.randint(0, ANCHO-30)
        self.y = -30
        self.tipo = random.choice(["taco","taco","taco","chile"]) # mas tacos que chiles
        self.rect = pygame.Rect(self.x, self.y, 35, 35)
    def mover(self):
        self.y += vel_caida
        self.rect.y = self.y

objetos = [Objeto()]
tiempo_spawn = 0

def dibujar_taco(surf, x, y):
    pygame.draw.ellipse(surf, (255,200,50), (x,y,35,25))
    pygame.draw.ellipse(surf, (139,69,19), (x+5,y+5,25,10))

def dibujar_chile(surf, x, y):
    pygame.draw.ellipse(surf, ROJO_CHILE, (x+10,y,15,30))
    pygame.draw.rect(surf, (0,100,0), (x+15,y,5,-10))

run = True
game_over = False

while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE: run=False
            if game_over and e.key==pygame.K_r:
                # reiniciar
                vidas=3; puntos=0; vel_caida=3; objetos=[Objeto()]; game_over=False; jugador.x=ANCHO//2

    if not game_over:
        teclas=pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]: jugador.x-=vel_jugador
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: jugador.x+=vel_jugador
        jugador.x = max(0, min(jugador.x, ANCHO-jugador.width))

        tiempo_spawn+=1
        if tiempo_spawn>30: # cada 0.5 seg cae uno nuevo
            objetos.append(Objeto())
            tiempo_spawn=0

        for obj in objetos[:]:
            obj.mover()
            if obj.rect.colliderect(jugador):
                if obj.tipo=="taco":
                    puntos+=10
                    if puntos%100==0: vel_caida+=0.5 # sube dificultad
                else:
                    vidas-=1
                    if vidas<=0: game_over=True
                objetos.remove(obj)
            elif obj.y>ALTO:
                if obj.tipo=="taco": vidas-=1 # si dejas caer un taco pierdes vida
                if vidas<=0: game_over=True
                if obj in objetos: objetos.remove(obj)

    # DIBUJADO
    pantalla.fill((30, 144, 255)) # cielo veracruzano
    # plato jugador
    pygame.draw.rect(pantalla, (255,255,255), jugador, border_radius=8)
    pygame.draw.rect(pantalla, (200,200,200), (jugador.x, jugador.y-5, jugador.width, 8), border_radius=5)

    for obj in objetos:
        if obj.tipo=="taco": dibujar_taco(pantalla, obj.x, obj.y)
        else: dibujar_chile(pantalla, obj.x, obj.y)

    txt_p = fuente.render(f"Tacos: {puntos}  Vidas: {vidas}", True, BLANCO)
    pantalla.blit(txt_p, (10,10))

    if game_over:
        sombra = pygame.Surface((ANCHO, ALTO)); sombra.set_alpha(180); sombra.fill((0,0,0))
        pantalla.blit(sombra, (0,0))
        t1 = fuente_big.render("¡SE ACABARON LOS TACOS!", True, BLANCO)
        t2 = fuente.render(f"Puntaje final: {puntos} tacos", True, BLANCO)
        t3 = fuente.render("Presiona R para reiniciar - ESC para salir", True, BLANCO)
        pantalla.blit(t1, (ANCHO//2 - t1.get_width()//2, 200))
        pantalla.blit(t2, (ANCHO//2 - t2.get_width()//2, 280))
        pantalla.blit(t3, (ANCHO//2 - t3.get_width()//2, 330))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
