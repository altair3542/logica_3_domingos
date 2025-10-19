# Devuelve la TRASPUESTA de m. Soporta matrices rectangulares (p. ej., 2×3 → 3×2).

def traspuesta(m):

    #matriz vacia
    if not m:
        return []

    #validamos rectangularidad...
    cols = len(m[0])
    for fila in m:
        if len(fila) != cols:
            raise ValueError("joa mani, ute que piensa de esta mondá")

    filas = len(m)
    t = []
    for c in range(cols):
        nueva_fila = []
        for f in range(filas):
            nueva_fila.append(m[f][c])
        t.append(nueva_fila)
    return t

# Ejemplo del enunciado
print(traspuesta([[1, 2, 3], [4, 5, 6]]))      # [[1, 4], [2, 5], [3, 6]]

# Casos adicionales
print(traspuesta([[1], [2], [3]]))             # [[1, 2, 3]]
print(traspuesta([[42]]))                      # [[42]]
print(traspuesta([]))                          # []
print(traspuesta([[], []]))                    # []
print(traspuesta([[1, 2, 3], [4, 5, 6, 13], [7, 8, 9]]))
