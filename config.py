# SETTINGS DEL PROGRAMA
import pygame

import componentes

__UMBRAL_DE_SALTO__ = 0.63 # TODO cambiar a 0.73
winH = 720
winW = 550
win=pygame.display.set_mode((winW,winH))
pygame.display.set_caption('Flappy Bird')

suelo = componentes.Suelo(winW)
tuberias = []