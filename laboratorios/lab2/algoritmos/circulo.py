import math

class Circulo:

    @staticmethod
    def pontosDoCirculoTrigonometrico(raio, centro):
        pontos = []
        teta = 0

        while (teta <= 45):
            x = raio * math.cos(teta)
            y = raio * math.sin(teta)

            pontos.extend(Circulo.pontosDoCirculoPorSimetria(int(x), int(y), centro))
            teta += 1

        return pontos

    @staticmethod
    def pontosDoCirculoPontoMedio(raio, centro):
        pontos = []

        x = 0
        y = raio

        d = 1 - raio
        pontos.extend(Circulo.pontosDoCirculoPorSimetria(x, y, centro))

        while(y > x):
            if(d < 0):
                d = d + 2 * x + 3
            else:
                d = d + 2 * (x - y) +  5
                y -= 1
            
            x += 1

            pontos.extend(Circulo.pontosDoCirculoPorSimetria(x, y, centro))

        return pontos
    
    @staticmethod
    def pontosDoCirculoPolinomial(raio, centro):
        pontos = []

        x = 0
        xFinal = raio / math.sqrt(2)

        while (x <= xFinal):
            y = math.sqrt(raio ** 2 - x ** 2)
            pontos.extend(Circulo.pontosDoCirculoPorSimetria(int(x), int(y), centro))
            x += 1
        return pontos


    @staticmethod
    def pontosDoCirculoPorSimetria(x, y, centro):
        points = []

        points.append((x + centro[0], y + centro[1]))
        points.append((x + centro[0], -y + centro[1]))
        points.append((-x + centro[0], y + centro[1]))
        points.append((-x + centro[0], -y + centro[1]))
        points.append((y + centro[0], x + centro[1]))
        points.append((y + centro[0], -x + centro[1]))
        points.append((-y + centro[0], x + centro[1]))
        points.append((-y + centro[0], -x + centro[1]))

        return points
