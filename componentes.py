# COMPONENTES DEL JUEGO
import pygame
import random

class Suelo:
    y_posic = 500 # posicion del suelo en la 'y' de la ventana

    def __init__(self,winw):
        self.x, self.y = (0, self.y_posic) # coordenadas 0,500 de la ventana
        self.recta = pygame.Rect(self.x, self.y, winw, 5) #la recta que define el suelo

    def draw(self,win):
        pygame.draw.rect(win, (255, 255, 255), self.recta)



class Tuberias:
    w = 15 # px
    altura_hueco = 100 # px
    def __init__(self, winw):
        self.x = winw
        self.altura_fondo = random.randint(100, 300)
        self.altura_arriba = Suelo.y_posic - self.altura_fondo - self.altura_hueco
        self.ractangulo_abajo,self.ractangulo_arriba = (pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0))
        self.passed = False
        self.fuera_pantalla = False

    def draw(self, win):
        self.ractangulo_abajo = pygame.Rect(self.x, Suelo.y_posic - self.altura_fondo, self.w, self.altura_fondo)
        pygame.draw.rect(win, (0,255,0), self.ractangulo_abajo)
        self.ractangulo_arriba = pygame.Rect(self.x, 0, self.w, self.altura_arriba)
        pygame.draw.rect(win, (0, 255, 0), self.ractangulo_arriba)

    def move(self):
        self.x -= 1
        if self.x + Tuberias.w <= 50 : # TODO: cambiar el 50 por la variable Pajaro.w
            self.passed = True
        if self.x <= -self.w :
            self.fuera_pantalla = True # si x es menor o igual a -15, con ancho 15, quiere decir si el ulimo px de la tuberia ha pasado la x = 0 de la ventana

