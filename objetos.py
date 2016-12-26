"""
Classe que presenta cada objeto a ser mostrado na cena
"""
from Algebra import *

class Objeto:

    def __init__(self, A, B, C, cor, ka, kd,ks, kt, n):
        """
        :param vertices - lista de vertices:
        :param faces: lista de Faces
        :param cor: cor do objeto (R,G,B):
        :param ka: coeficiente ambiental
        :param kd: coeficiente difuso
        :param ks: coeficiente especular
        :param kt: coeficiente de transparencia
        :param n: expoente de reflexão especular
        """
        self.A = A # Vertice A
        self.B = B # Vertice B
        self.C = C # Vertice C
        self.normal = Normal(A, B, C)
        self.cor = cor
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.kt = kt
        self.n = n


class Light():
    def __init__(self, A, B, C, color, lp):
        self.A = A # Vertice A
        self.B = B # Vertice B
        self.C = C # Vertice C
        self.normal = Normal(A, B, C)
        self.color = color
        self.lp = lp


class ObjectQuadric():
    def __init__(self):
        pass
