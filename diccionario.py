'''
tuplas van con ()
listas van con []
diccionarios van con {}
'''

midiccionario = {"mishell": "jorge",
                 "paris": "francia", "venezuela": "caracas"}
print(midiccionario["paris"])

# sintaxis basica

midiccionario["caca"] = "caraota"
print(midiccionario)

# agregar al diccionario otro campo

midiccionario["caca"] = "cambip"
print(midiccionario)

# modificar un campo

del midiccionario["caca"]
print(midiccionario)

# borra un campo

mitupla = [1, 2, 3, 4]
dicci = {mitupla[0]: "uno", mitupla[1]: "dos",
         mitupla[2]: "tres", mitupla[3]: "cuatro"}
print(dicci[mitupla[1]])

# usando una tupla como clave de un diccionario y asignando los valores, imprimimos el que queremos con la clave asignada luego

michael = {23: "jordan", "nombre": "misha",
           "equipo": "chicago", "anillos": [1991, 1992, 1993]}
print(michael["anillos"])

# se guardo una tupla en un diccionario y podemos llamarla y mostrarla


michael = {23: "jordan", "nombre": "misha", "equipo": "chicago",
           "anillos": {"temporadas": [1991, 1992, 1993]}}
print(michael["anillos"])

# se guardo un diccionario dentro de otro que tenia una tupla en []

print(michael.keys())
print(michael.values())
print(len(michael))

# formas de imprimir el diccionario
