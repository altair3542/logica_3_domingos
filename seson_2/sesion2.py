# Algoritmos de ordenación de arreglos. (burbuja e inserción)

# Objetivos de aprendizaje

# Comprender por qué necesitamos ordenar datos.

# Aplicar Burbuja (con y sin optimización) e Inserción paso a paso.

# Interpretar trazas de ejecución y evitar errores comunes (límites, comparaciones).

# Validar que un arreglo quedó efectivamente ordenado.

# requisitos previos...

# que es un arreglo, como se declara, como se accede por indice, como se recorre con for.

# comparadores >, <, >=, <=.

# por que ordenar?: se facilita la busqueda la comparacion y los reportes.

# notas de menor a mayor me permiten ver quienes aprobaron rapidamente, o puedo validar los precios de una tienda para comprar del mas barato al mas caro.

# siempre debo definir el criterio de orden, sea ascendente y descendente.

# Metodo de ordenación por burbuja.

# por que se llama burbuja.

# por que visualmente, cuando se ordenan parecen burbujas donde lops elementos mas grandes se van empujando hacia el final del arreglo.

# idea general:

# usa para comparar pares adyacentes.
# si estan en orden incorrecto, se intercambian y repiten pasadas hasta que no se necesite hacer intercambios. (esto ultimo puede optimizarse.)

arr = [5, 1, 4, 2, 8, 3, 10, 11, 9, 6]
n = len(arr)
print(arr)

for pasada in range(n - 1):
    hubo_cambio = False
    for i in range(n - 1 - pasada):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            hubo_cambio = True
            print(arr)
    if not hubo_cambio:
        break
print(arr)
