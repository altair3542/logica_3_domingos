#FUNDAMENTOS ARRAYS UNIDIMENSIONALES SESION 1 

# Que es una estructura de datos: Son formas de organizar los datos para poder usarlos de manera eficiente... 
#(Es como ordenar nuestra habitacion: Cajones de las medias contienen medias, perchas: Colgar camisas y pantalones)

#Problema sin estructura: Tengo 50 notas sueltas ... encontrar la de matematicas. Toma minutos-

#Con estructura (Arreglos): Guardo en un cajon con separadores numerados. Ahora se exactamente donde mirar 

#Arreglod: (Cajon con casilleros)

# Definimos un Arreglo como una coleccion ordenada de elementos del  mismo tipo
#Esto para lenguajes no imterpretados, de tipado estricto, fuertemente tipado y sin inferencia de tipos.

 # indices empiezan desde cero donde el primer cajon es cero

# Tamaño fijo: Al crearlo se decide cuantos espacios va a tener.

# notas = [15, 18, 20, 17, 12]

# print(notas[1])

# como recorremos un arreglo?

# para i desde 0 hasta n-1:
#   mostrar notas[i]

# for i in range(len(notas)):
#     print(f"-> {notas[i]}")

# llenados de arreglos

# entrada simulada

# edades = [0]*5
# valores = [21, 18, 30, 25, 19]
# for i in range(5):
#     edades[i] = valores[i]
# print(edades)
# print(valores)

# Actualizacion por indice

# nombres = ["Ana", "Luis", "Mar", "Sofi"]
# print(nombres)
# indice = int(input("que posicion quieres cambiar?: "))
# nombres[indice] = input("A quien vamos a integrar: ")
# print(nombres)

# Insercion conceptual: si hay espacio, "corro elementos a la derecha y pongo el primero"

# borrado conceptual: "corro elementos" a la izquierda para tapar algun hueco.

# nota... en lenguajes con listas dinamicas como python esto no es necesario.

# arr = [10, 20, 30, 40 , None]
# #insertar un 25 en la posicion 2.
# for i in range(3, -1, -1): #3, 2, 1, 0
#     arr[i+1]=arr[i]
#     print(arr)
# arr[2] = 25
# print(arr)

