"""
Classe que presenta cada objeto a ser mostrado na cena
"""
from Algebra import Dot, Vector3D, Normal, Normalize, Cross

class Objeto:

    def __init__(self, A, B, C, color, ka, kd,ks, kt, n):
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
        self.plane_constant = Dot(A, Normal(A, B, C))
        self.color = color
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.kt = kt
        self.n = n


    def intersect(self, ray):

        r = Normalize(ray.d)
        # Checando se o triangulo e o raio são paralelos
        if Dot(r, self.normal) == 0.0:

             # Raio nao intersecta o triangulo
            hit = False
            distance = 0.0
            hit_point = Vector3D(0.0, 0.0, 0.0)

            return (hit, distance, hit_point, self.normal)

           # Calculando o ponto que pode está no plano do triangulo
        t = - (Dot(self.normal, ray.o) + self.plane_constant) / Dot(self.normal, ray.d)
        hit_point = ray.get_hitpoint(t)

        # Se t for negativo o objeto está atras da camera
        if t < 0:
            # Raio nao intersecta o triangulo
            hit = False
            distance = 0.0
            hit_point = Vector3D(0.0, 0.0, 0.0)

            return (hit, distance, hit_point, self.normal)


        # Checando se o Ponto está dentro do triangulo
        # Inside-OutSide Test
        vectorAB = self.B - self.A;
        vectorBC = self.C - self.B;
        vectorCA = self.A - self.C;

        C0 = hit_point - self.A
        C1 = hit_point - self.B
        C2 = hit_point - self.C

        if (Dot(self.normal, Cross(vectorAB, C0)) > 0
             and Dot(self.normal, Cross(vectorBC, C1)) > 0
             and Dot(self.normal, Cross(vectorCA, C2))) > 0:
            hit = True
            distance = t
            hit_point = ray.get_hitpoint(t)
            return (hit, distance, hit_point, self.normal)  # tuple

        # Didn't hit the triangule
        hit = False
        distance = 0.0
        hit_point = Vector3D(0.0, 0.0, 0.0)

        return (hit, distance, hit_point, self.normal)

class Light():
    def __init__(self, A, B, C, color, lp):
        self.A = A # Vertice A
        self.B = B # Vertice B
        self.C = C # Vertice C
        self.normal = Normal(A, B, C)
        self.plane_constant = Dot(A, Normal(A, B, C))
        self.color = color
        self.lp = lp

    def intersect(self, ray):

        r = Normalize(ray.d)
        # Checando se o triangulo e o raio são paralelos
        if Dot(r, self.normal) == 0.0:

             # Raio nao intersecta o triangulo
            hit = False
            distance = 0.0
            hit_point = Vector3D(0.0, 0.0, 0.0)

            return (hit, distance, hit_point, self.normal)

        # Calculando o ponto que pode está no plano do triangulo
        t = - (Dot(self.normal, ray.o) + self.plane_constant) / Dot(self.normal, ray.d)
        hit_point = ray.get_hitpoint(t)

        # Se t for negativo o objeto está atras da camera
        if t < 0:
            # Raio nao intersecta o triangulo
            hit = False
            distance = 0.0
            hit_point = Vector3D(0.0, 0.0, 0.0)

            return (hit, distance, hit_point, self.normal)


        # Checando se o Ponto está dentro do triangulo
        # Inside-OutSide Test
        vectorAB = self.B - self.A;
        vectorBC = self.C - self.B;
        vectorCA = self.A - self.C;

        C0 = hit_point - self.A
        C1 = hit_point - self.B
        C2 = hit_point - self.C

        if (Dot(self.normal, Cross(vectorAB, C0)) > 0
             and Dot(self.normal, Cross(vectorBC, C1)) > 0
             and Dot(self.normal, Cross(vectorCA, C2))) > 0:
            hit = True
            distance = t
            hit_point = ray.get_hitpoint(t)
            return (hit, distance, hit_point, self.normal)  # tuple

        # Didn't hit the triangule
        hit = False
        distance = 0.0
        hit_point = Vector3D(0.0, 0.0, 0.0)

        return (hit, distance, hit_point, self.normal)

class ObjectQuadric():
    def __init__(self):
        pass
