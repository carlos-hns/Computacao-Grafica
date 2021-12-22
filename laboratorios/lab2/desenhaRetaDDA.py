import time
from tkinter import *

click_number = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0

def desenhaRetaDDA(event):
    global click_number
    global x1, y1
    pixel = (  # Definição do grupo de pixeis
        ("blue", "blue")
    )
    if click_number == 0:
        x1 = event.x
        y1 = event.y
        imagem.put(pixel, (int(x1), int(y1)))
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
               
        for i in range(int(len)):
            x1 = x1 + xinc
            y1 = y1 + yinc
            imagem.put(pixel, (int(x1), int(y1)))

            print("Ponto (x = %.3f, y = %.3f)"%(x1, y1))
        
        click_number = 0

window = Tk()
window.title("Desenho da reta usando o algoritmo DDA")
window.resizable(False, False)

imagem = PhotoImage(width=400,height=400)
tela = Label(window, image=imagem)
tela.bind("<Button-1>", desenhaRetaDDA)
tela.pack()

window.mainloop()