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
        if((0 <= ponto[0] <= 200) and (0 <= ponto[1] <= 200)):
            imagem.put(pixel, (ponto[0], ponto[1]))
        

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
