from Algebra import RGBColour
from Algebra import BLACK, Vector3D, Cross, Normalize, Length, Dot
from objetos import Objeto, Light, ObjectQuadric
from math import pow


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
                ia = float (prop_dict['ambient']) * float (obj.ka)
                result = result + (RGBColour(ia, ia, ia))

                # Iluminação difusa
                p1 = Vector3D(0.0, -1.0, 0.0)
                p2 = obj.normal

                if (Length(p1)!= 1) :
                    p1 = Normalize(p1)
                    pass

                if (Length(obj.normal)!= 1) :
                    p2 = Normalize(obj.normal)
                    pass

                lv = 1.0 * float (obj.kd) * Dot(p1, p2)

                result = result + (RGBColour(lv, lv, lv))

                # Iluminação especular
                p1 = Vector3D(p1.x * (-1), p1.y, p1.z)
                from main import eye
                p2 = eye

                if (Length(p1)!= 1) :
                    p1 = Normalize(p1)
                    pass

                if (Length(eye)!= 1) :
                    p2 = Normalize(eye)
                    pass

                lv = 1.0 * float (obj.ks) * pow(Dot(p1, p2), float (obj.n))

                result = result + (RGBColour(lv, lv, lv))

                dist = distance

        return result
