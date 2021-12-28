from tkinter import *

class RetaBresenham:
    def __init__(self,imagem):
        self.imagem = imagem

    def desenhaRetaBresenham(self,start,end):
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
            self.imagem.put("blue", (x, y))
            xcoordinates.append(x)
            ycoordinates.append(y)



