import pygame
from sys import exit

import config
import componentes
import poblacion

def exit_game():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            if guardar:
                _, individuo = poblacion.condicion_de_parada()
                if individuo is not None:
                    individuo.ai.export_to_onnx("mejor_modelo.onnx")
            exit()

def generar_tuberias():
    config.tuberias.append(componentes.Tuberias(config.winW))

def mostrar_info(win, generacion, vivos):
    font = pygame.font.SysFont(None, 25)
    texto = f"Generación: {generacion} - Vivos: {vivos}"
    img = font.render(texto, True, (255, 255, 255))
    win.blit(img, (10, 10))

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

        if not poblacion.san_extinto_los_mu_tontos():
            vivos = poblacion.update_pajaros_vivos() # dibujar los pajaros vivos
        else :
            config.tuberias = []
            poblacion.next_gen()
            vivos = len(poblacion.pajaros)

        mostrar_info(config.win, poblacion.generacion, vivos)

        clock.tick(60)
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    poblacion = poblacion.Poblacion(30)
    guardar = False
    main()

