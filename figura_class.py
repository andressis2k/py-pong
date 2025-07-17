import pygame as pg

class Red:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def dibujar(self,screen):
        center = self.width // 2
        div_x = self.width // 100
        div_y = self.width // 100
        first_x = center - 4 * div_x
        last_x = 1 + center + 4 * div_x
        for x in range(first_x,last_x,div_x):
            pg.draw.line(screen,(205,156,41),(x,0),(x,self.height),2)
        for y in range(0,self.height,div_y):
            pg.draw.line(screen,(205,156,41),(first_x,y),(last_x,y),2)

class Raqueta:
    def __init__(self,height,pos_x,color=(255,255,255),w=10,h=100):
        self.height = height
        self.pos_x = pos_x
        self.pos_y = (height-h)/2
        self.color = color
        self.w = w
        self.h = h

    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.pos_x,self.pos_y,self.w,self.h))

    def move(self,key_up,key_down):
        key = pg.key.get_pressed()
        if self.pos_y > 0 and key[key_up]:
            self.pos_y -= 2
        if self.pos_y < self.height-self.h and key[key_down]:
            self.pos_y += 2


class Pelota:
    def __init__(self,pos_x,pos_y,color=(255,255,255),rad=30,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.rad = rad
        self.vx = vx
        self.vy = vy
        self.contDer = 0
        self.contIzq = 0

    def draw(self,screen):
        pg.draw.circle(screen,self.color,(self.pos_x,self.pos_y),self.rad)

    def mover(self,x_max,y_max):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_x >= x_max+(2*self.rad):
            self.contDer += 1
            self.pos_x = x_max/2
            self.pos_y = y_max/2
            self.vx *= -1

        if self.pos_x <= 0 - (2*self.rad):
            self.contIzq += 1
            self.pos_x = x_max/2
            self.pos_y = y_max/2
            self.vx *= -1
        
        if self.pos_y >= y_max-(self.rad) or self.pos_y <= 0 + self.rad:
            self.vy *= -1
