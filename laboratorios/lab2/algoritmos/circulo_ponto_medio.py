def pontosDoCirculo(raio, centro):
    pontos = []

    x = 0
    y = raio

    # valorPontoMedio == d na dedução
    d = 1 - raio
    pontos.extend(pontosDoCirculoPorSimetria(x, y, centro))

    while(y > x):
        if(d < 0):
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) +  5
            y -= 1
        
        x += 1

        pontos.extend(pontosDoCirculoPorSimetria(x, y, centro))

    return pontos

def pontosDoCirculoPorSimetria(x, y, centro):
    points = []

    points.append((x + centro[0], y + centro[1]))
    points.append((x + centro[0], -y + centro[1]))
    points.append((-x + centro[0], y + centro[1]))
    points.append((-x + centro[0], -y + centro[1]))
    points.append((y + centro[0], x + centro[1]))
    points.append((y + centro[0], -x + centro[1]))
    points.append((-y + centro[0], x + centro[1]))
    points.append((-y + centro[0], -x + centro[1]))

    return points