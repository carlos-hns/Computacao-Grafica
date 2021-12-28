import sys
from tkinter import *

from algoritmos.circulo import Circulo
from algoritmos.desenhaRetaDDA import RetaDDA
from algoritmos.bresenham_algoritmo import RetaBresenham
from algoritmos.ponto_medio import RetaPontoMedio
from tela import desenharPontos

alturaTela = 200
larguraTela = 200

def onLeftClick(event):
    ponto = (event.x, event.y)
    selecionarAlgoritmo(entrada, ponto)

def selecionarAlgoritmo(entrada, ponto):
    match entrada:
        case '1':
            pontosDoCirculoTrig= Circulo.pontosDoCirculoTrigonometrico(20, ponto)
            desenharPontos(pontosDoCirculoTrig,imagem)
        case '2':
            pontosDoCirculoPM = Circulo.pontosDoCirculoPontoMedio(20, ponto)
            desenharPontos(pontosDoCirculoPM,imagem)
        case '3':
            pontosDoCirculoP = Circulo.pontosDoCirculoPolinomial(20, ponto)
            desenharPontos(pontosDoCirculoP,imagem)
        case '4':
            pontosDaRetaDDA = RetaDDA(imagem).desenhaRetaDDA
            tela.bind("<Button-1>", pontosDaRetaDDA)
        case '5':
            y2 = alturaTela
            desenhaRetaB =  RetaBresenham(imagem)

            # plota linhas do primeiro oitante
            while y2 > alturaTela/2:
                start = (0, alturaTela)
                end = (larguraTela, y2)
                desenhaRetaB.desenhaRetaBresenham(start,end)
                y2 -= 5
        case '6':
            retaPM = RetaPontoMedio(imagem)
            y2 = alturaTela

            # plota linhas do primeiro oitante
            while y2 > alturaTela/2:
                start = (0, alturaTela)
                end = (larguraTela, y2)
                retaPM.desenhaRetaPontoMedio(start, end)
                y2 -= 5
        case '7':
            print("Fim do programa.")
        case _:
            sys.exit("Valor de entrada inválido. Fim do programa.")

print("Inicio do programa:")
entrada = input(
"""
Digite o número listado para executar o respectivo algoritmo: 
1 - Algoritmo do Círculo Trigonométrico
2 - Algoritmo do Círculo do Ponto Médio
3 - Algoritmo do Círculo Polinomial
4 - Algotitmo da Reta DDA
5 - Algoritmo da Reta Bresenham
6 - Algoritmo da Reta do Ponto Médio
7 - Sair do programa
"""
)

window = Tk()
window.title("Desenhando Primitivas")
window.resizable(False, False)

imagem = PhotoImage(width=larguraTela,height=alturaTela)
tela = Label(window, image=imagem)
tela.bind("<Button-1>", onLeftClick)

tela.pack()
window.mainloop()



