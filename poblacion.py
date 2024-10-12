# POBLACION (CONJUNTO DE PLAYERS)
import random

import config
import player

class Poblacion:
    def __init__(self,n=1):
        self.pajaros = []
        self.n = n
        self.generacion = 1
        for i in range(0,n):
            self.pajaros.append(player.Pajaro())

    def update_pajaros_vivos(self):
        vivos = 0
        for pajaro in self.pajaros:
            if not pajaro.muerto:
                vivos += 1
                #print(self.pajaro.muerto)
                pajaro.get_vision()
                pajaro.decidir()
                pajaro.draw(config.win)
                pajaro.gravedad(config.suelo)
                pajaro.set_fitness()
        return vivos

    def san_extinto_los_mu_tontos(self):
        extintos = True
        for pajaro in self.pajaros:
            if not pajaro.muerto:
                extintos = False
        return extintos

    def condicion_de_parada(self):
        """"
        Condición de parada del algoritmo genético
        :return: True y el individuo si se ha encontrado un individuo con fitness >= 3600
        :rtype: (bool, player.Pajaro)
        """
        continuar = True
        individuo = None
        for pajaro in self.pajaros:
            if pajaro.fitness >= 3600:
                continuar = False
                individuo = pajaro
                break
        return continuar, individuo

    def seleccionar(self):
        self.pajaros.sort(key=lambda x: x.fitness, reverse=True)

    def next_gen(self):
        self.seleccionar()
        next_gen = []
        next_gen.append(self.pajaros[0]) # añadir siempre el mejor indivviduo a la siguiente generacion
        while len(next_gen) < len(self.pajaros)-1:
            i1,i2 = self.seleccionar_pajaros_torneo(4,False)
            p1,p2 = self.cruzar(i1,i2,True)
            self.mutar_individuo(p1,0.05)
            self.mutar_individuo(p2,0.05)
            if len(next_gen) < len(self.pajaros):
                next_gen.append(p1)
            if len(next_gen) < len(self.pajaros):
                next_gen.append(p2)
        del self.pajaros[:]
        self.pajaros = next_gen
        self.generacion += 1



    def seleccionar_pajaros_torneo(self, k=3, torneo=True):
        """"
        Selección por torneo \n
        La función elige k competidores al azar de la población actual, y devuelve los  dos mejores
        :param k: numero de competidores
        :type k: int
        :param torneo: si es True se hace torneo, si es False se hace ruleta
        :type torneo: bool
        :return: los dos mejores competidores
        :rtype: (player.Pajaro, player.Pajaro)
        """
        if torneo:
            def torneo():
                competidores = random.sample(self.pajaros, k)
                competidores.sort(key=lambda x: x.fitness, reverse=True)
                return competidores[0]

            pajaro1 = torneo()
            pajaro2 = torneo()
            return pajaro1, pajaro2
        else:
            def ruleta():
                total_fitness = sum(pajaro.fitness for pajaro in self.pajaros)
                pick = random.uniform(0, total_fitness)
                current = 0
                for pajaro in self.pajaros:
                    current += pajaro.fitness
                    if current > pick:
                        return pajaro

            competidores = [ruleta() for _ in range(k)]
            competidores.sort(key=lambda x: x.fitness, reverse=True)
            return competidores[0], competidores[1]

    @staticmethod
    def cruzar( i1, i2, bias):
        """"
        Cruza los genomas de dos pajaros
        :param i1: Individuo a cruzar
        :type i1: player.Pajaro
        :param i2: Individuo a cruzar
        :type i2: player.Pajaro
        :param bias: Indica si se cruza también el bias
        :type bias: bool
        :rtype: (player.Pajaro, player.Pajaro)
        """
        w1 = i1.genomasW.clone()
        w2 = i2.genomasW.clone()
        b1 = i1.genomasB.clone()
        b2 = i2.genomasB.clone()
        for i in range ((len(i1.genomasB)//2)+1 , len (i1.genomasB)): # hasta la mitad se mantiene y empezamos a cruzar en la otra mitad
            aux1 = i1.genomasW[0,i] # torch.Size([1, 3]) ---> tensor([[-0.3098,  0.0622, -0.0313]], requires_grad=True)
            aux2 = i2.genomasW[0,i]
            w1[0,i] = aux2
            w2[0,i] = aux1
        if bias:
            aux1 = i1.genomasB[0]   # torch.Size([1]) ---> tensor([0.2962], requires_grad=True)
            aux2 = i2.genomasB[0]
            b1[0] = aux2
            b2[0] = aux1

        p1 = player.Pajaro(True,b1,w1)
        p2 = player.Pajaro(True,b2,w2)
        return p1,p2

    @staticmethod
    def mutar_individuo(i, probabilidad):
        """"
        Mutación de un individuo
        :param i: Individuo a mutar
        :type i: player.Pajaro
        :param probabilidad: Probabilidad de mutación
        :type probabilidad: float
        """
        if random.random() <= probabilidad:
            bias = i.genomasB
            pesos = i.genomasW
            if random.random() <= 0.6:  # cambio pequeño
                modificador_peso = random.uniform(-0.1, 0.1)
                pesos[0,0] += modificador_peso
                pesos[0,1] += modificador_peso
                pesos[0,2] += modificador_peso
                modificador_bias = random.uniform(-0.1,0.1)
                bias[0] += modificador_bias
            else:   # cambio grande
                modificador_peso = random.uniform(-0.5, 0.5)
                pesos[0,0] += modificador_peso
                pesos[0,1] += modificador_peso
                pesos[0,2] += modificador_peso
                modificador_bias = random.uniform(-0.5,0.5)
                bias[0] += modificador_bias
            i.set_ai(bias,pesos)