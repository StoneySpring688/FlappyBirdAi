import pygame
from sys import exit
import config
import componentes
import poblacion

def exit_game():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

def generar_tuberias():
    config.tuberias.append(componentes.Tuberias(config.winW))


def main():
    spawn_time_tuberias = 10
    while True:
        exit_game()
        config.win.fill((0,0,0))

        config.suelo.draw(config.win) # dibujar el suelo
        if spawn_time_tuberias <= 0:
            generar_tuberias()
            spawn_time_tuberias = 200
        spawn_time_tuberias = spawn_time_tuberias-1

        for tuberia in config.tuberias :
            tuberia.draw(config.win)
            tuberia.move()
            if tuberia.fuera_pantalla:
                config.tuberias.remove(tuberia) # si una tuberia no se ve, se elimina

        if not poblacion.sanExtintoLosMuTontos():
            poblacion.update_pajaros_vivos() # dibujar los pajaros vivos
        else :  # Parpadeo Game Over
            config.tuberias = []
            poblacion.seleccion()

        clock.tick(60)
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    poblacion = poblacion.Poblacion(100)
    main()
