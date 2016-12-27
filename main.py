"""
Responsavel por controlar o aplicativo
"""
from helper import read
from tkinter import * #for GUI
from Algebra import Vector3D
from Camera import *
from PathTraceIntegrator import *

print("Lendo Arquivos de configuração e Objetos")

file = ".\src\cornellroom.sdl"
DIRECTORY = './' # alterar de acordo com computador

obj_types_list = ['object','quad', 'light']
prop_types_list = ['eye', 'size', 'ortho', 'background', 'ambient', 'tonemapping', 'npaths', 'seed', 'output']

obj_list = []  # Lista de objetos a serem redenrizados
prop_dict = {} # dicionario com propriedades da cena

FILENAME = str (prop_types_list[8])

# Lendo os arquivos de configurações e objetos
f = open(file, 'r')

for line in f:
    # Pulando linhas em branco
    if len(line) < 2:
        continue

    words = line.split()
    line_type = words[0] ## Tipo da linha
    values = words[1:]   ## Valores do objeto ou propriedade

    if line_type == '#':
        pass
    elif line_type in obj_types_list:
        new_objs_list = (read(line_type, values))
        obj_list = (obj_list,  new_objs_list)
    elif line_type in prop_types_list:
        prop_dict[line_type] = (read(line_type, values))
    else:
        print ("Tipo não encontrado")
        print(line_type)


#print("Lista de objetos: ", obj_list)
#print("Lista de propriedades: ", prop_dict)

#Create Camera
eye = Vector3D(prop_dict['eye'][0], prop_dict['eye'][1], prop_dict['eye'][2]) #higher z = more narrow view
#eye = Vector3D(-3.0, 0.0, 190.0) # para testar
focal = Vector3D(0.0, 0.0, 0.0)
view_distance = 1000 #larger = more orthographic like
up = Vector3D(0.0, 1.0, 0.0)
height = int (prop_dict['size'][0])
width = int (prop_dict['size'][1])
spp = int (prop_dict['npaths'])
cam = Camera(eye, focal, view_distance, up, height, width, spp)
pathTracer = PathTraceIntegrator()
cam.render(pathTracer) #trace scene and save image

#-------------------------------------------------Temporary GUI
#GUI using tkinter
root = Tk()
root.title("PyPath")

#open saved image image
#use camera variables set above
viewer = Canvas(root, width=width, height=height)
image_name = PhotoImage(file = DIRECTORY + FILENAME)
viewer.create_image(width/2.0, height/2.0, image = image_name)
viewer.grid(row=0, column=0)

root.mainloop()
