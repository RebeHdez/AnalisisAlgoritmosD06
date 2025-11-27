from random import sample

# =================== Bubble Sort ===================
def bubble_sort(vectorbs, debug=False):
    if debug: print("El vector a ordenar es:", vectorbs)
    n = len(vectorbs)
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if vectorbs[j] > vectorbs[j+1]:
                vectorbs[j], vectorbs[j+1] = vectorbs[j+1], vectorbs[j]
    if debug: print("El vector ordenado con Bubble Sort es:", vectorbs)
    return vectorbs

# =================== Merge Sort ===================
def merge_sort(vectormerge, debug=False):
    """Ordena la lista usando Merge Sort. Complejidad O(n log n)."""
    if debug: print("El vector a ordenar con Merge Sort es:", vectormerge)

    def merge(vectormerge):
        if len(vectormerge) > 1:
            medio = len(vectormerge) // 2
            izq = vectormerge[:medio]
            der = vectormerge[medio:]

            merge(izq)
            merge(der)

            i = j = k = 0
            while i < len(izq) and j < len(der):
                if izq[i] < der[j]:
                    vectormerge[k] = izq[i]
                    i += 1
                else:
                    vectormerge[k] = der[j]
                    j += 1
                k += 1

            while i < len(izq):
                vectormerge[k] = izq[i]
                i += 1
                k += 1
            while j < len(der):
                vectormerge[k] = der[j]
                j += 1
                k += 1

    merge(vectormerge)
    if debug: print("El vector ordenado con Merge Sort es:", vectormerge)
    return vectormerge

# =================== Quick Sort ===================
def quick_sort(vectorquick, debug=False):
    """Ordena la lista usando Quick Sort. Complejidad O(n log n) promedio."""
    if debug: print("El vector a ordenar con Quick Sort es:", vectorquick)

    def quick(vectorquick, start=0, end=None):
        if end is None:
            end = len(vectorquick) - 1
        if start >= end:
            return

        def particion(vectorquick, start, end):
            pivot = vectorquick[start]
            menor = start + 1
            mayor = end

            while True:
                while menor <= mayor and vectorquick[mayor] >= pivot:
                    mayor -= 1
                while menor <= mayor and vectorquick[menor] <= pivot:
                    menor += 1
                if menor <= mayor:
                    vectorquick[menor], vectorquick[mayor] = vectorquick[mayor], vectorquick[menor]
                else:
                    break
            vectorquick[start], vectorquick[mayor] = vectorquick[mayor], vectorquick[start]
            return mayor

        p = particion(vectorquick, start, end)
        quick(vectorquick, start, p-1)
        quick(vectorquick, p+1, end)

    quick(vectorquick)
    if debug: print("El vector ordenado con Quick Sort es:", vectorquick)
    return vectorquick

# =================== Búsquedas ===================
def busqueda_lineal(arr, obj):
    for i, v in enumerate(arr):
        if v == obj:
            return i
    return -1

def busqueda_binaria(arr, obj):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] == obj: return m
        l, r = (m+1, r) if arr[m] < obj else (l, m-1)
    return -1
