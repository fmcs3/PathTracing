from Algebra import RGBColour
from main import prop_dict


class PathTraceIntegrator:
    #Initializer - creates object list
    def __init__(self):
        self.primitives = []
    #trace light path
    def trace_ray(self, ray, depth):

            result = RGBColour(prop_dict['background'][0], prop_dict['background'][1], prop_dict['background'][2]) #black - change to background