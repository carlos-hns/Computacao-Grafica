from graphics import *

def dda():
    while True:
        tela = GraphWin('DDA', 500, 500)
        titulo = Text(Point(50, 50), 'DDA')
        titulo.draw(tela)

        ponto1 = tela.getMouse()
        ponto1.draw(tela)

        ponto2 = tela.getMouse()
        ponto2.draw(tela)

        tela.getMouse
        
        x0 = ponto1.x
        y0 = ponto1.y

        x1 = ponto2.x
        y1 = ponto2.y

        dx = x1 - x0
        dy = y1 - y0

        if abs(dx) > abs(dy):
            len = dx
        else:
            len = dy
        
        xinc = dx/float(len)
        yinc = dy/float(len)

        pt = Point(x0, y0)
        pt.setOutline('blue')
        pt.draw(tela)

        for i in range(int(len)):
            x0 = x0 + xinc
            y0 = y0 + yinc
            pt = Point(int(x0), int(y0))
            pt.setOutline('blue')
            pt.draw(tela)

            print("Ponto ({}, {}):".format(x0, y0))

    

dda()