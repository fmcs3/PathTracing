from Algebra import RGBColour
from Algebra import BLACK, Vector3D, Cross, Normalize, Length, Dot
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
                p1 = Vector3D(0.0, -1.0, 0.0)
                p2 = obj.normal

                if (Length(inter[2])!= 1) :
                    p1 = Normalize(inter[2])
                    pass

                if (Length(obj.normal)!= 1) :
                    p2 = Normalize(obj.normal)
                    pass

                lv = 1.0 * float (obj.kd) * Dot(p1, p2)

                result = result + (RGBColour(lv, lv, lv))
                dist = distance

        return result
