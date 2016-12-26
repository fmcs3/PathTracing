from Algebra import BLACK, Ray
from random import random
from main import prop_dict
from winsound import Beep #for beep sound when complete

FILENAME = prop_dict['output']

#save pixel to array
def save_pixel(self, single_pixel, x, y):
    pixel = single_pixel * 255
    pixel.clamp(0.0, 255.0)
    #write to array
    i = ((self.height - y - 1) * self.width + x)
    self.image_array[i*3 + 0] = int(pixel.r)
    self.image_array[i*3 + 1] = int(pixel.g)
    self.image_array[i*3 + 2] = int(pixel.b)

def render(self, integrator):
    ray = Ray()
    ray.o = self.eye
    pixel = BLACK  # create black pixel
    for x in range(0, self.width):
        for y in range(0, self.height):
            pixel = BLACK  # start at black
            for s in range(0, self.spp):
                sp_x = (x + random()) - (self.width / 2.0)
                sp_y = (y + random()) - (self.height / 2.0)
                ray.d = self.get_direction(sp_x, sp_y)
                pixel = pixel + integrator.trace_ray(ray, 1)
            pixel = pixel / self.spp
            self.save_pixel(pixel, x, y)  # save pixel to pixel array
        print((x / self.width) * 100, "%")
    # save image to file
    self.save_image(FILENAME)  # FILENAME is define at top of source file
    # Play sound to signal a beep (For Windows)
    for i in range(1, 4):
        Beep(i * 500, 250)