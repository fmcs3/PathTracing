from Algebra import Vector3D

class PhotonMappingIntegrator:
    numberPhotons = 1

    # Initializer - creates object list
    def __init__(self):
        self.obj_list = []

    #photon path
    def trace_ray(self, ray, depth):

        # Checando interseções com cada objeto
        dist = 100
        hit = False
        objeto = 1
        hit_point = Vector3D(0.0, 0.0, 0.0)
        normal = Vector3D(0.0, 0.0, 0.0)

        for obj in self.obj_list:
            inter = obj.intersect(ray)
            tmp_hit = inter[0]
            distance = inter[1]

            if tmp_hit and distance < dist:
                dist = distance
                objeto = obj
                hit = tmp_hit
                hit_point = inter[2]
                normal = inter[3]

        if hit: ## Se o raio bateu no objeto calculamos a cor do ponto
            if isinstance(objeto, Light):
                return objeto.color
            else:
                result = local_color(objeto, normal, ray, self.ambient)
        else:
            return self.background