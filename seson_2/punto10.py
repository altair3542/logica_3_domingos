a = [9, 7, 8, 3,11,15,22,50,69,6,2,1]
print("incial", a)

for i in range(1, len(a)):
    actual = a[i]
    j = i -1
    desplazamientos = 0

    # desplazamos hacia la derecha todos los numeros mayores que actual.
    while j >= 0 and a[j] > actual:
        a[j + 1] = a[j]
        j -= 1
        desplazamientos +=1

    #insertar actual en el hueco donde va
    a[j + 1] = actual

    print(f"i = {i}, actual={actual}, desplazamientos ={desplazamientos}, arreglo={a}")

print("ordenado", a)
