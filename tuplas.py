tuplas1=(1,2,3,4,"jorge",3)
print(tuplas1)

#tuplas

milistatupla=list(tuplas1)
print(milistatupla)

#convierte una tupla en lista

tupla2=tuple(milistatupla)
print(tupla2)

#convierte una lista en tupla

print(tuplas1.count(3))

#cuenta cuantos elementos tiene esa dupla del elmento

print(len(tuplas1))

#devuelve la longitud de elementos

tuplas1=(1,2,3,4,"jorge",3)

tupla3=(1,2,3,4)
uno, dos, tres, cuatro,=tupla3
print(uno)
print(dos)
print(tres)
print(cuatro)