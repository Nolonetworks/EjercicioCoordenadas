import math

class Punto:

    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    def Imprimir(self):
        PuntoTupla = (self.X,self.Y)
        print('El punto de coordenadas es el siguiente: ' + str(PuntoTupla))

    def CalculoCuadrante(self):
        if self.X == 0 and self.Y == 0:
            print('El punto de coordenadas esta en el origen')
        elif self.X>=0 and self.Y>=0:
            print('El punto de coordenadas esta en el primer cuadrante')
        elif self.X>=0 and self.Y<=0:
            print('El punto de coordenadas esta en el cuarto cuadrante')
        elif self.X<=0 and self.Y>=0:
            print('El punto de coordenadas esta en el segundo cuadrante')
        elif self.X<=0 and self.Y<=0:
            print('El punto de coordenadas esta en el tercer cuadrante')

    def Vectorizador(self, Z=0, W=0):
        self.vector1 = Z-self.X
        self.vector2 = W-self.Y
        vector = (self.vector1,self.vector2)
        return vector

class Rectangulo:
    
    def __init__(self, a=0, b=0, a1=0, b1=0):
        self.a = a
        self.b = b
        self.a1 = a1
        self.b1 = b1
    
    def base(self):
        self.base = int(abs(self.a-self.a1))
        print('La base de su rectangulo es :' + str(self.base))
        pass

    def altura(self):
        self.altura = int(abs(self.b-self.b1))
        print('La altura de su rectangulo es :' + str(self.altura))
        pass

    def area(self):
        self.area = self.altura*self.base
        print('La area de su rectangulo es :' + str(self.area))
        pass
        