# arreglos bidimensionales (matrices)

# Objetivos de aprendizaje

# Entender qué es una matriz (arreglo 2D) y cómo se representa como filas × columnas.

# Practicar recorridos por filas, por columnas y diagonales (en matrices cuadradas).

# Realizar operaciones comunes: suma total, sumas por fila/columna, conteos, máximo con posición y transformaciones simples (p. ej., traspuesta).

# Evitar errores típicos (índices, tamaños, diagonales, copia superficial).

# que es una matriz?

#Definición: un arreglo de dos dimensiones: una lista de filas, y cada fila contiene columnas. Piénsalo como una tabla de Excel.

# m = [
#     [3, 1, 2, 7],
#     [0, 5, 9, 4],
#     [6, 8, 2, 1]
# ]

# print(m[1][2])

# filas = len(m)
# columnas = len(m[0])

# print(f"las dimensiones de este arreglo son {filas} x {columnas}")

# 2. recorridos tipicos.

#a recorrido por filas (row major)

# m = [
#     [3, 1, 2],
#     [0, 5, 9],
#     [6, 8, 2]
# ]

# filas = len(m)
# cols = len(m[0])

# for f in range(filas):
#     for c in range(cols):
#         print(f"(f={f}, c={c}) -> {m[f][c]}")

# for c in range(cols):
#     for f in range(filas):
#         print(f"(f={f}, c={c}) -> {m[f][c]}")


# diagonales

# n = len(m)
# cols = len(m[0])

# # validacion de cuadratura.
# if n == cols:
#     # diagonal principal
#     for i in range(n):
#         print(f"principal: {m[i][i]}")

#     # diagonal secundaria:
#     for i in range(n):
#         print(f"secundaria: {m[i][n - 1 - i]}")

#suma total de la matriz

# total = 0

# for f in range(len(m)):
#     for c in range(len(m[0])):
#         total += m[f][c]

# print(f"suma total: {total}")

#sumas por fila y por columna

# filas = len(m)
# cols = len(m[0])

# #sumar por fila...
# for f in range(filas):
#     suma_f = 0
#     for c in range(cols):
#         suma_f += m[f][c]
#     print(f"suma fila {f} : {suma_f}")

# # suma por columnas
# for c in range(cols):
#     suma_c = 0
#     for f in range(filas):
#         suma_c += m[f][c]
#     print(f"Suma de columna {c}: {suma_c}")
