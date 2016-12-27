from Algebra import RGBColour
from Algebra import BLACK
from objetos import Objeto, Light, ObjectQuadric


class PathTraceIntegrator:
    background = BLACK # Cor do Background

    #Initializer - creates object list
    def __init__(self):
        self.obj_list = []

    #trace light path
    def trace_ray(self, ray, depth):
        result = self.background

        # Checando interseções com cada objeto
        dist = 50
        for obj in self.obj_list:
            inter = obj.intersect(ray)
            hit = inter[0]
            distance = inter[1]
            if hit and distance < dist:
                result = obj.color

        return result