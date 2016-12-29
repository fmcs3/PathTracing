from Algebra import RGBColour
from Algebra import BLACK, Vector3D, Cross, Normalize, Length, Dot, local_color, Ray, flip_direction, random_direction
from objetos import Objeto, Light, ObjectQuadric
import random
from math import pow


class PathTraceIntegrator:
    background = BLACK # Cor do Background
    ambient = 0.5

    #Initializer - creates object list
    def __init__(self):
        self.obj_list = []


    #trace light path
    def trace_ray(self, ray, depth):
        difuso = BLACK
        especular = BLACK

        # Checando interseções com cada objeto
        dist = 50
        hit = False
        objeto = 1
        hit_point = 1

        for obj in self.obj_list:
            inter = obj.intersect(ray)
            tmp_hit = inter[0]
            distance = inter[1]

            if tmp_hit and distance < dist:
                dist = distance
                objeto = obj
                hit = tmp_hit
                hit_point = inter[2]

        if hit:
            result = local_color(objeto, ray, self.ambient)
        else:
            return self.background

        if depth == 0 or isinstance(objeto, Light):
                return result

        # Calculando os Raios Secúndarios
        ktot = obj.kd + obj.ks + obj.kt
        aleatorio = random.random()*ktot

        if aleatorio < obj.kd:                            ## Raio Difuso
            x = random.random()
            y = random.random()
            dir = random_direction(x, y, obj.normal)

            new_ray = Ray(hit_point, Normalize(dir))
            difuso = self.trace_ray(new_ray, depth - 1)
        elif aleatorio < obj.kd + obj.ks:        #         ## Raio especular
            L = Normalize(flip_direction(ray.d))
            N = objeto.normal
            R = (N * (Dot(N, L)) - L) * 2.0

            new_ray = Ray(hit_point, Normalize(R))
            especular = self.trace_ray(new_ray, depth - 1)
        else:                                               ## Raio Transmitido
            pass

        # Emitando Raio Difuso


        # Emitindo Raio Difuso

        return result + difuso*0.5 + especular*0.5
