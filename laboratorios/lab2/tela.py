
def desenharPontos(listaDePontos,imagem):
    for ponto in listaDePontos:
        if((0 <= ponto[0] <= 200) and (0 <= ponto[1] <= 200)):
            imagem.put(pixel("blue"), (ponto[0], ponto[1]))

def pixel(cor):
    return (cor)