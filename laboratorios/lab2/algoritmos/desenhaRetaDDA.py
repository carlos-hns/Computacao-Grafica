from tkinter import *

class RetaDDA:
    def __init__(self,imagem):
        self.click_number = 0
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.imagem = imagem

    def desenhaRetaDDA(self,event):
        self.click_number
        self.x1
        self.y1
        pixel = (  # Definição do grupo de pixeis
            ("blue", "blue")
        )
        if self.click_number == 0:
            self.x1 = event.x
            self.y1 = event.y
            self.imagem.put(pixel, (int(self.x1), int(self.y1)))
            self.click_number = 1
        else:
            self.x2 = event.x
            self.y2 = event.y
        
            dx = self.x2 - self.x1
            dy = self.y2 - self.y1

            if abs(dx) > abs(dy):
                len = dx
            else:
                len = dy
                
            xinc = dx/float(len)
            yinc = dy/float(len) 
                
            for i in range(int(len)):
                self.x1 = self.x1 + xinc
                self.y1 = self.y1 + yinc
                self.imagem.put(pixel, (int(self.x1), int(self.y1)))

                print("Ponto (x = %.0f, y = %.0f)"%(self.x1, self.y1))
            
            self.click_number = 0

