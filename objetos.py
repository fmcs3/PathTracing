"""
Classe que presenta cada objeto a ser mostrado na cena
"""
from pygame import Color
from pygame.math import Vector3

class Objeto:
    # Lista dos vetores normais a cada face
    normal = []

    def __init__(self, vertices, faces, cor, ka, kd,ks, kt, n):
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
        self.vertices = vertices
        self.faces = faces
        self.cor = cor
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.kt = kt
        self.n = n

        # Chamando função para calcular os vetores normais para cada face
        self.__calc()

    # Calcula os vetores normais para cada face
    def __calc(self):
        for face in self.faces:
            # Cada face tem 3 vertices
            # calculamos dois vetores com os vertices
            v = self.vertices[face[0] - 1] - self.vertices[face[1] - 1]
            s = self.vertices[face[0] - 1] - self.vertices[face[2] - 1]

            # Calculando o produto cruzado para achar o vetor normal
            self.normal.append(v.cross(s))

class Luz():
    normal = []

    def __init__(self, vertices, faces, cor, lp):
        self.vertices = vertices
        self.faces = faces
        self.cor = cor
        self.lp = lp


class ObjectQuadric():
    def __init__(self):
        pass
