"""
Sistemas de coordenadas do mundo ou do usuário
  É um conjunto de coordenadas cartesianas em um intervalo qualquer definido pelo usuário.

Sistema de coordenadas normalizadas do dispositivo (NDC)
  É um sistema intermediário, definido de tal forma que todo conteúdo da janela de visualização
  possua as coordenadas variando no intevarlo [0,1] X [0,1]
Demonstração:
    NDCx = (2*(X-Xmin))/(Xmax - Xmin) -1
    NDCy = (2*(Y-Ymin))/(Ymax - Ymin) -1 

Sistema  de coordenadas do dispositivo
  É um conjunto de pixels endereçáveis pelo dispositivo. Os pixels são endereçados por dois
"""

class Coordenadas:
    def __init__(self, x, y, xMax=1000, xMin=0, yMax=500, yMin=0):  # construtor da classe
        self.x = x
        self.y = y
        self.xMax = xMax
        self.xMin = xMin
        self.yMax = yMax
        self.yMin = yMin
        self.ndH = 300  # 900 x 1200 tela do dispositivo
        self.ndV = 400

    def user_to_ndc(self):  # coordenadas do usuário para coordenadas normalizadas do dispositivo
        ndcX = (self.x - self.xMin) / (self.xMax - self.xMin)
        ndcY = (self.y - self.yMin) / (self.yMax - self.yMin)
        return ndcX, ndcY

    # coordenadas normalizadas do dispositivo para coordenadas do dispositivo
    def ndc_to_dc(self):
        ndcX, ndcY = self.user_to_ndc()
        dcX = round(ndcX*(self.ndH - 1))
        dcY = round(ndcY*(self.ndV - 1))
        return dcX, dcY

    # coordenadas do dispositivo para coord. normalizadas do dispotivivo
    def dc_to_ndc(self):
        dcX, dcY = self.ndc_to_dc()
        ndcX = round(dcX / (self.ndH - 1), 2)
        ndcY = round(dcY / (self.ndV - 1), 2)
        return ndcX, ndcY

    # coord. normalizadas do dispotivivo para coord. do usuário
    def ndc_to_user(self):
        ndcX, ndcY = self.dc_to_ndc()
        x = ndcX * (self.xMax - self.xMin) - self.xMin
        y = ndcY * (self.yMax - self.yMin) - self.yMin
        return x, y

    # coordenadas normalizadas centradas (-1 a +1)
    # coord. do usuário para coord. normalizadas centradas do dispositivo
    def cent_user_to_ndc(self):
        ndcX = (2 * (self.x - self.xMin) / (self.xMax - self.xMin)) - 1
        ndcY = (2 * (self.y - self.yMin) / (self.yMax - self.yMin)) - 1
        return ndcX, ndcY

    # coord. norm. centradas do dispositivo para coord. do dispositivo

    def cent_ndc_to_dc(self):
        ndcX, ndcY = self.cent_user_to_ndc()
        dcX = round(((ndcX + 1) * (self.ndH)) / 2)
        dcY = round(((ndcY + 1) * (self.ndV)) / 2)
        return dcX, dcY

    # coord. do dispositivo para coord. norm. centradas do dispositivo

    def cent_dc_to_ndc(self):
        dcX, dcY = self.cent_ndc_to_dc()
        ndcX = ((2 * dcX)/(self.ndH)) - 1
        ndcY = ((2 * dcY)/(self.ndV)) - 1
        return ndcX, ndcY

    # coord. norm. centradas do dispositivo para coord. do usuário

    def cent_ndc_to_user(self):
        ndcX, ndcY = self.cent_dc_to_ndc()
        x = (((ndcX + 1) * (self.xMax - self.xMin))/2) - self.xMin
        y = (((ndcY + 1) * (self.yMax - self.yMin))/2) - self.yMin
        return x, y

    def imprimeCoordenadas(self):
        coor1 = Coordenadas(self.x, self.y)
        ndcX, ndcY = coor1.user_to_ndc()
        dcX, dcY = coor1.ndc_to_dc()
        print(f"coordenadas NDC: {str(ndcX)} e {str(ndcY)}")
        print(f"coordenadas DC: {str(dcX)} e {str(dcY)}")

        ndcX, ndcY = coor1.dc_to_ndc()
        x, y = coor1.ndc_to_user()
        print(f"coordenadas DC_TO_NDC: {str(ndcX)} e {str(ndcY)}")
        print(f"coordenadas NDC_TO_USER: {str(x)} e {str(y)}")

        print("\nCom coordenadas normalizadas centradas:")
        cent_ndcX, cent_ndcY = coor1.cent_user_to_ndc()
        cent_dcX, cent_dcY = coor1.cent_ndc_to_dc()
        print(f"coordenadas NDC: {str(cent_ndcX)} e {str(cent_ndcY)}")
        print(f"coordenadas DC: {str(cent_dcX)} e {str(cent_dcY)}")

        cent_ndcX, cent_ndcY = coor1.cent_dc_to_ndc()
        cent_x, cent_y = coor1.cent_ndc_to_user()
        print(f"coordenadas DC_TO_NDC: {str(cent_ndcX)} e {str(cent_ndcY)}")
        print(f"coordenadas NDC_TO_USER: {str(cent_x)} e {str(cent_y)}")
