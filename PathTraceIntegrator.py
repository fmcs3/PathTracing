from Algebra import RGBColour
from Algebra import BLACK, Vector3D
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

                # Iluminação do objeto
                result = obj.color

                # Iluminação ambiente
                from main import prop_dict
                result = result + (RGBColour(float (obj.ka), float (obj.ka), float (obj.ka)) * float (prop_dict['ambient']))

                # Iluminação difusa
                #from main import obj_list
                #result = result + RGBColour(1.0, 1.0, 1.0) + RGBColour(float (obj.kd), float (obj.kd), float (obj.kd))
                dist = distance

        return result
