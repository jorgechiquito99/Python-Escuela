nombre = "jorge"
apellido = "bermudez urdaneta"
edad = '24'
cedula = 1234523456

complete = nombre + " " + apellido 

#print('v1', complete)

complete2 = 'hola mi nombre es {} y mi apellido es {}'

#print('v2', complete2.format(nombre, apellido))

complete3 = f'hola mi nombre es {nombre} y mi apellido es {apellido} y mi edad es {edad}'

#print('v3', complete3.format(nombre, apellido))

print(f'mi cedula es {cedula}')
print("mi cedula es " + str(cedula))