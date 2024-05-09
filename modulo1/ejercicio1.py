import json
#Resuelto en google colabs
with open('libreria.json', 'r') as file:
    libros = json.load(file)

def numeroLibros():
    numLibros = len(libros["book"])
    return numLibros

def filtroPrecio(inf, sup):
    listaNombres = []
    with open("libreria.json", "r") as archivo:
        dicc = json.load(archivo)
        for i in dicc:
            if inf < dicc[i]["price"] > sup:
                listaNombres.append(dicc[i]["title"][1])
    return listaNombres

def filtroCadena(cadena):
    res = {}
    with open("libreria.json", "r") as archivo:
        dicc = json.load(archivo)
        for i in dicc:
            if dicc[i]["title"][1].startswith(cadena):
                res.update(dicc[i]["title"][1], dicc[i]["year"])
    return res

def muestraLibros():
    res = {}
    with open("libreria.json", "r") as archivo:
        dicc = json.load(archivo)
        for i in dicc:
            for autores in dicc[i]:
                res.update(dicc[i]["title"][1], [dicc[i]["author"]])
    return res

#Llamadas a las funciones
numeroLibros()

