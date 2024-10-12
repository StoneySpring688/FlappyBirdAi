# POBLACION (CONJUNTO DE PLAYERS)
import config
import player

class Poblacion:
    def __init__(self,n=1):
        self.pajaros = []
        self.n = n
        for i in range(0,n):
            self.pajaros.append(player.Pajaro())

    def update_pajaros_vivos(self):
        for pajaro in self.pajaros:
            if not pajaro.muerto:
                #print(self.pajaro.muerto)
                pajaro.get_vision()
                pajaro.decidir()
                pajaro.draw(config.win)
                pajaro.gravedad(config.suelo)

    def sanExtintoLosMuTontos(self):
        extintos = True
        for pajaro in self.pajaros:
            if not pajaro.muerto:
                extintos = False
        return extintos

    def seleccion(self):
        self.pajaros = []
        for i in range(0,self.n):
            self.pajaros.append(player.Pajaro())