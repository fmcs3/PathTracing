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
        for obj in self.obj_list:
            oh_my = obj.intersect(ray)
            if oh_my[0]:
                result = obj.color

        return result