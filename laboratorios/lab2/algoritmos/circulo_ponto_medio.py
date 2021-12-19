def pontosDoCirculo(raio, centro):
    pontos = []

    x = centro[0]
    y = centro[1] + raio

    # valorPontoMedio == d na dedução
    d = 1 - raio
    pontos.extend(pontosDoCirculoPorSimetria(x, y))

    while(y > x):
        if(d < 0):
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) +  5
            y -= 1
        
        x += 1

        # + centerPoint[0]
        # + centerPoint[1]
        pontos.extend(pontosDoCirculoPorSimetria(x, y))

    return pontos

def pontosDoCirculoPorSimetria(x, y):
    points = []

    points.append((x, y))
    points.append((x, -y))
    points.append((-x, y))
    points.append((-x, -y))
    points.append((y, x))
    points.append((y, -x))
    points.append((-y, x))
    points.append((-y, -x))

    return points