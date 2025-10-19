# Funciones y busquedas en arreglos.

# Objetivos de aprendizaje

# Entender qué es una función, cómo recibe parámetros y retorna resultados.

# Diferenciar efectos al pasar inmutables (números, strings) vs mutables (listas).

# Implementar búsqueda lineal como función y búsqueda binaria (cuando el arreglo está ordenado).

# Integrar: ordenar → buscar → reportar (pipeline sencillo).

# Evitar errores comunes (límites, condiciones, precondiciones de binaria).

# Requisitos previos (5 min)

# Arreglos 1D (índices, recorrido).

# Ordenación básica (Burbuja / Inserción).

# Operadores relacionales (<, <=, ==, >, >=) y while/for.

# 1) ¿Qué es una función?

# Idea: una función es una “máquina” con entradas (parámetros) y salida (valor retornado). Nos permite reutilizar código y organizar mejor los programas.


# parametro = 5
# def cuadrado(x):
#     return x * x

# print(cuadrado(parametro))
# print(parametro)


# parametros...

# son los insumos con lo que va a trabajar mi función.
# los parametros pueden ser mutables o inmutables.

#inmutables: int, str o boolean: si los cambiamos dentro de la function, no necesariamente van a cambiar por fuera.

#mutables: listas y diccionarios: si los modificamos por function, el dato de insumo SI CAMBIA por fuera...

# def sumar_uno_valor(n):
#     n = n + 1
#     return n

# x = 10
# y = sumar_uno_valor(x)
# print(x, y)

# def sumar_uno_lista(a):
#     for i in range(len(a)):
#         a[i] += 1

# arr = [1, 2, 3]
# print(arr)
# sumar_uno_lista(arr)
# print(arr)

# busqueda lineal...

# cuando usar la busqueda lineal?

# usamos busquedas lineales cuando el arreglo NO ESTA ORDENADO o no importa la eficiencia para tamaños pequeños o medios...

# especificacion:
# entrada: objetivo (valor a ser buscado), arr (lista donde vamos a buscar)

#salida: indice de la primera posicion que coincida con la busqueda o -1 si no está

# def buscar_lineal(arr, objetivo):
#     for i in range(len(arr)):
#         if arr[i] == objetivo:
#             return i
#     return -1

# datos = [7, 2, 9, 4, 2]
# print(buscar_lineal(datos, 2))
# print(buscar_lineal(datos, 5))

# Errores a evitar

# Olvidar return -1 al final.

# Empezar i en 1 (debe ser 0).

# Confundir “primera coincidencia” con “todas las coincidencias”.

# 4) Búsqueda binaria

# Idea: mirar al centro y descartar la mitad que no sirve.
# Requisito: el arreglo debe estar ordenado (ascendente aquí).

# Especificación

# Entrada: arr_ordenado (lista ascendente), objetivo

# Salida: índice donde aparece; -1 si no está.

def buscar_binaria(arr, objetivo):
    ini, fin = 0, len(arr) - 1
    while ini <= fin:
        mid = (ini + fin) // 2
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            ini = mid + 1
        else:
            fin = mid - 1
    return -1

arr = [1, 2, 4, 5, 9]

print(buscar_binaria(arr, 5))
print(buscar_binaria(arr, 6))
