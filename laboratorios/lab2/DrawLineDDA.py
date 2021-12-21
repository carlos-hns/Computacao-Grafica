import time
from tkinter import *

click_number = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0

def desenhaReta(event):
    global click_number
    global x1, y1
    if click_number == 0:
        x1 = event.x
        y1 = event.y
        imagem.put("black", (int(x1), int(y1)))
        click_number = 1
    else:
        x2 = event.x
        y2 = event.y
    
        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            len = dx
        else:
            len = dy
            
        xinc = dx/float(len)
        yinc = dy/float(len)

        imagem.put("black", (int(x1), int(y1)))        
        for i in range(int(len)):
            x1 = x1 + xinc
            y1 = y1 + yinc
            imagem.put("black", (int(x1), int(y1)))

            print("Ponto ({}, {}):".format(x1, y1))
        
        click_number = 0

window = Tk()
window.title("Desenho da reta usando o algoritmo DDA")
window.resizable(False, False)

imagem = PhotoImage(width=200,height=200)
tela = Label(window, image=imagem)
tela.bind("<Button-1>", desenhaReta)
tela.pack()

window.mainloop()