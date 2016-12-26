"""
Responsavel por controlar o aplicativo
"""
from helper import read
#import Tkinter

print("Lendo Arquivos de configuração e Objetos")

file = ".\src\cornellroom.sdl"

obj_types_list = ['object','quad', 'light']
prop_types_list = ['eye', 'size', 'ortho', 'background', 'ambient', 'tonemapping', 'npaths', 'seed', 'output']

obj_list = []  # Lista de objetos a serem redenrizados
prop_dict = {} # dicionario com propriedades da cena

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
