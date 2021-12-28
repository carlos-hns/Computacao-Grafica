from tkinter import *

class RetaPontoMedio:
    def __init__(self,imagem):
        self.imagem = imagem

    def desenhaRetaPontoMedio(self,start, end):
        # Condições iniciais de configuração
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = y2 - y1
    
        # Determine o quão íngreme a linha é
        is_steep = abs(dy) > abs(dx)
    
        # Rodar linha
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
    
        # Troque os pontos inicial e final, se necessário, e armazene o estado de troca
        swapped = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            swapped = True
    
        # Recalcular diferenciais
        dx = x2 - x1
        dy = y2 - y1
    
        # Calcular erro
        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1
    
        # Iterar sobre a caixa delimitadora, gerando pontos entre o início e o fim
        y = y1
        points = []
        for x in range(x1, x2 + 1):
            coord = (y, x) if is_steep else (x, y)
            points.append(coord)
            error -= abs(dy)
            self.imagem.put("blue", coord)
            print("Ponto (x = %.2f, y = %.2f)"%coord)
            if error < 0:
                y += ystep
                error += dx
    
        # Reverte a lista se as coordenadas forem trocadas
        if swapped:
            points.reverse()
        return points



