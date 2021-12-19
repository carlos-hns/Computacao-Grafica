from tkinter import *
from algoritmos.circulo_ponto_medio import pontosDoCirculo

def onLeftClick(event):
    pixel = (  # Definição do grupo de pixeis
        ("blue", "blue", "blue", "blue", "blue"),
        ("blue", "blue", "blue", "blue", "blue"),
        ("blue", "blue", "blue", "blue", "blue"),
        ("blue", "blue", "blue", "blue", "blue"),
        ("blue", "blue", "blue", "blue", "blue")
    )
    
    print("Event:", event)

    pontosCirculo = pontosDoCirculo(20, (event.x, event.y))
    for ponto in pontosCirculo:
        pontoTranformado = transformarPonto(ponto, 200)
        print("Ponto", ponto)
        print("Ponto transformao", pontoTranformado)
        imagem.put(pixel, (20,20))
        #imagem.put(pixel, (pontoTranformado[0], pontoTranformado[1]))
        

def transformarPonto(ponto, valorMaximoY):
    return (ponto[0], transformarParametroEixoYTkinter(ponto[1], valorMaximoY))

def transformarParametroEixoYTkinter(y, valorMaximoY):
    return  valorMaximoY - y 

window = Tk()
window.title("Desenhano Primitivas")
window.resizable(False, False)

imagem = PhotoImage(width=200,height=200)
tela = Label(window, image=imagem)
tela.bind("<Button-1>", onLeftClick)
tela.pack()

window.mainloop()
