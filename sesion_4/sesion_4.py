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

def sumar_uno_valor(n):
    n = n + 1
    return n

x = 10
y = sumar_uno_valor(x)
print(x, y)

def sumar_uno_lista(a):
    for i in range(len(a)):
        a[i] += 1

arr = [1, 2, 3]
print(arr)
sumar_uno_lista(arr)
print(arr)
