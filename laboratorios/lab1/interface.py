from tkinter import *
from Coordenadas import Coordenadas

class ConfDefalt:
    def __init__(self):
        self.title = "Transformações de Coordenadas CG"
        self.screen_width = 700
        self.screen_height = 600
        self.canvasX = 600
        self.canvasY = 500


# entradaX = int(input("Digite o valor da coordenada X: "))
# entradaY = int(input("Digite o valor da coordenada Y: "))
coor1 = Coordenadas(500, 250)
coor1.imprimeCoordenadas()

window = Tk()
cf = ConfDefalt()
window.title(cf.title)

# largura, altura, dist esquerda + dist topo
window.geometry("%dx%d+0+0" % (cf.screen_width, cf.screen_height))

# colocando a img de fundo e especificando a posição dela na tela
canvas = Canvas(window, width=cf.canvasX, height=cf.canvasY, bg="orange")
canvas.pack(side="bottom")
label_plano_cartesiano = Label(window)
label_plano_cartesiano.place(x=0, y=0)

# colocar o pixel como imagem
img = PhotoImage(width=cf.screen_width, height=cf.screen_height)
canvas.create_image((cf.screen_width / 2, cf.screen_height / 2),
                    image=img, state="normal")  # normal, disabled or hidden

# Plano cartesiano
# canvas.create_line(0, cf.canvasY/2, cf.canvasX, cf.canvasY/2)
# canvas.create_line(cf.canvasX/2, 0, cf.canvasX/2, cf.canvasY)

# Valores coordenadas
coordEntrada = Frame(window)
coordEntrada.place(bordermode=OUTSIDE, height=20, width=500, x=50)
msg = Label(coordEntrada,
            text=f"Coordenadas de entrada X:{coor1.cent_ndc_to_user()[0]} | Y: {coor1.cent_ndc_to_user()[(1)]}")
msg["font"] = ("calibre", "12", "bold")
msg.pack(side="bottom")

# Função responsável por marcar o pixel na tela

def pixel():

    auxCentroPlanoCartesianoX = 0
    auxCentroPlanoCartesianoY = 500
    x = coor1.ndc_to_dc()[0]
    y = coor1.ndc_to_dc()[1]

    coordPlanoCartesianoX = auxCentroPlanoCartesianoX + x
    coordPlanoCartesianoY = auxCentroPlanoCartesianoY - y

    if(x > cf.canvasX):
        x = cf.canvasX
    elif(y > cf.canvasY):
        y = cf.canvasY
    elif(y < 0):
        y = 0
    elif(x < 0):
        x = 0

    msg.configure(text=f'Coordenadas do dispositivo X:{x} | Y: {y}')

    data = (  # Definição do grupo de pixeis
        ("blue", "blue", "blue", "blue", "blue"),
        ("blue", "blue", "blue", "blue", "blue"),
        ("blue", "blue", "blue", "blue", "blue"),
        ("blue", "blue", "blue", "blue", "blue"),
        ("blue", "blue", "blue", "blue", "blue")
    )

    img.put(data, (coordPlanoCartesianoX, coordPlanoCartesianoY))


canvas.bind('<Button>', pixel)

pixel()
window.mainloop()
