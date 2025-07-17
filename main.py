import pygame as pg
import figura_class
import random
import math
#from time import sleep

single_player = True

def movimiento(angle):
    rad = angle * math.pi / 180
    x = math.cos(rad)
    y = math.sin(rad)
    return x,y

width = 1280
height = 720

red = figura_class.Red(width,height)
pg.init()

# Obtenemos la tasa de refresco
tasa_refresco = pg.time.Clock()

screen = pg.display.set_mode((width, height))

marcador_font = pg.font.SysFont("arial",30)

anchor1 = 10
anchor2 = 10

# Creamos la raqueta indicando el ancho de la pantalla, la posición horizontal
raqueta1 = figura_class.Raqueta(height,10,w=anchor1)
raqueta2 = figura_class.Raqueta(height,width-10-anchor2,w=anchor2)

# Creamos la pelota indicando la posición original (x, y) y el color
pelota = figura_class.Pelota(width/2,height/2,(198,79,53))

if single_player:
    raqueta1.pos_y = 0
    raqueta1.h = height


running = True

# Definimos el ángulo inicial aleatoriamente, para ver quién empieza
angle = random.choice((0,-180))
angle = 50
while running:
    # Obtenemos la tasa de refresco en milisegundos
    speed = tasa_refresco.tick(400)
    pg.display.set_caption(f"Pong v0.1 - Velocidad: {abs(pelota.vx)}")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_PAGEUP and pelota.vx >= 0 or (event.key == pg.K_PAGEDOWN and pelota.vx <= 0):
                pelota.vx += 1
            if event.key == pg.K_PAGEDOWN and pelota.vx >= 0 or (event.key == pg.K_PAGEUP and pelota.vx <= 0):
                pelota.vx -= 1
            
    

    screen.fill((230,200,33))

    
    #pg.draw.line(screen,(205,156,41),(width/2,0),(width/2,height),2)
    red.dibujar(screen)

    # Mostramos los marcadores
    marcador1 = marcador_font.render(str(pelota.contIzq),True,"red")
    marcador2 = marcador_font.render(str(pelota.contDer),True,"red")
    if not single_player:
        screen.blit(marcador1,(width/4*3,50))
    screen.blit(marcador2,(width/4,50))

    # Movemos las raquetas
    raqueta1.move(pg.K_w,pg.K_s) 
    raqueta2.move(pg.K_UP,pg.K_DOWN) 
    #raqueta2.pos_y = 450
    # Movemos la pelota 

    pelota.mover(width,height)
    if pelota.pos_x - pelota.rad - raqueta1.w <= raqueta1.pos_x and abs(pelota.pos_y - (raqueta1.pos_y + raqueta1.h/2)) <= raqueta1.h/2 + pelota.rad:
        pelota.vx *= -1
    if pelota.pos_x + pelota.rad >= raqueta2.pos_x and abs(pelota.pos_y - (raqueta2.pos_y + raqueta2.h/2)) <= raqueta2.h/2 + pelota.rad:
        pelota.vx *= -1
    
    raqueta1.draw(screen)
    raqueta2.draw(screen)
    pelota.draw(screen)

    pg.display.flip()
    #input(f"Pelota {pelota.pos_y}, Raqueta 2 {raqueta2.pos_y}, Raqueta 2 + r/2 {raqueta2.pos_y + raqueta2.h/2}, Raqueta2h/2 + pelota.rad {raqueta2.h/2 + pelota.rad}")
