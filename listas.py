milista=["jorge","sara","carop","vreerv"]
print(milista[:])
print(milista[2])
print(milista[0])
print(milista[-1])
print(milista[0:3])
print(milista[:3])
print(milista[2:])

#listas

milista.append("jferfe")
print(milista)

#agrega un dato a la lista

milista.insert(2,"posi2")
print(milista)

#agrega un dato a la lista en una posicion

milista.extend(["uno","dos"])
print(milista)

#agrega varios datos o otro lista a una lista 

print(milista.index("sara"))

#devuelve la pocision de el compo proporcionado en el index siempre devuelve el primir indix que coincida en caso de tener 2 iguales en la lista

print("sarsa" in milista)

#deveulve true o false si el elemnto esta en la lista

milista.remove("sara")

#elimina un elemento de la lista

milista.pop()

#elimina el ultimo elemento de una lista

lista1=[1,2,3,4]
lista2=["prueba2","priueba3"]
lista3=lista1+lista2
print(lista3)

#el operador + concatena 2 listas

listarepit=[3]*3
print(listarepit)

#al multiplicar la lista se repite las veces