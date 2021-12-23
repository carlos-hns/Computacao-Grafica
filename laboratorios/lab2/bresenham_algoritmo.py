from tkinter import *
import math

larguraTela = 400
alturaTela = 400

x1 = 0 #int(input("Valor x1 : "))
y1 = alturaTela #int(input("Valor Y1 : "))
x2 = larguraTela #int(input("Valor x2 : "))
y2 = alturaTela #int(input("Valor Y2 : "))
start = (x1, y1)
end = (x2, y2)

root = Tk()
pic = PhotoImage(width = larguraTela, height = alturaTela)
lb = Label(root,image = pic)
lb.pack()
color = "blue"

def bresenham(start, end):
    x1, y1 = start
    x2, y2 = end
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    print('x = %s, y = %s' % (x, y))
    # Lista com coordenadas
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print('x = %s, y = %s' % (x, y))
        pic.put(color, (x, y))
        xcoordinates.append(x)
        ycoordinates.append(y)
        

# plota linhas no primeiro oitante
while y2 > alturaTela/2:
    bresenham(start, end)
    y2 -= 10
    start = (x1, y1)
    end = (x2, y2)

root.mainloop()