from tkinter import *
import math

#defining main function
def main():
    x1 = int(input("ENTER THE X1 : "))
    y1 = int(input("ENTER THE Y1 : "))
    x2 = int(input("ENTER THE X2 : "))
    y2 = int(input("ENTER THE Y2 : "))
    root = Tk()
    pic = PhotoImage(width = 500,height = 500)
    lb = Label(root, image = pic)
    lb.pack()
    color = "blue"

    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    
    for x in range(x1,x2):
        y = int(m*x + y1 + 0.5)
        pic.put(color, (x, y))

        print("Ponto ({}, {}):".format(x, y))

    root.mainloop()

main()