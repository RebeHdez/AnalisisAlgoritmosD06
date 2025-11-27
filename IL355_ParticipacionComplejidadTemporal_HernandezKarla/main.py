# main.py
import tkinter as tk
import random
import time
from tkinter import messagebox
from Complejidad import busqueda_lineal, busqueda_binaria, bubble_sort, merge_sort, quick_sort

# Dependencias para la gráfica en Tkinter
HAS_MPL = True
try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
except Exception:
    HAS_MPL = False

# Variables
BG = "lightblue"
TAMANIOS = [50, 100, 500, 1000]
datos = []
tam_seleccion = None

# generar datos
def gen():
    global datos
    n = tam_seleccion.get()
    datos = random.sample(range(n*3), n)  # ahora genera desordenada
    info.config(text=f"Lista generada ✔ (n={len(datos)})")
    out.config(text="Resultados: —")

# medir el tiempo de ejecución de los algoritmos
def medir_tiempo(algoritmo, lista):
    copia = lista[:]  # trabajar con copia
    t0 = time.perf_counter()
    algoritmo(copia)
    return (time.perf_counter() - t0)  # Tiempo en segundos

# compara algoritmos de ordenamiento y grafica en el GUI
def comparar():
    if not HAS_MPL:
        return messagebox.showinfo("Gráfica no disponible", "Instala matplotlib con:\n\npip install matplotlib")
    
    xs, bubble, merge, quick = TAMANIOS, [], [], []
    for n in xs:
        arr = random.sample(range(n*3), n)  # lista desordenada
        bubble.append(medir_tiempo(bubble_sort, arr))
        merge.append(medir_tiempo(merge_sort, arr))
        quick.append(medir_tiempo(quick_sort, arr))

    # Crear gráfica con estilo como la captura
    ax.clear()
    ax.set_title("Comparación de Algoritmos de Ordenamiento")
    ax.set_xlabel("Tamaño de la lista (N)")
    ax.set_ylabel("Tiempo de ejecución (segundos)")

    ax.plot(xs, bubble, "o-", label="Bubble Sort", color="blue")
    ax.plot(xs, merge, "o-", label="Merge Sort", color="orange")
    ax.plot(xs, quick, "o-", label="Quick Sort", color="green")

    # Aquí la diferencia clave:
    ax.set_xticks(xs)  # poner los tamaños exactos en el eje X
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend()
    canvas.draw_idle()


# Imprimir tabla de tiempos en consola
def imprimir_tabla():
    bubble_results = [medir_tiempo(bubble_sort, random.sample(range(i*3), i)) for i in TAMANIOS]
    merge_results = [medir_tiempo(merge_sort, random.sample(range(i*3), i)) for i in TAMANIOS]
    quick_results = [medir_tiempo(quick_sort, random.sample(range(i*3), i)) for i in TAMANIOS]

    print("Tamaño de lista | Bubble Sort | Merge Sort | Quick Sort")
    for idx, tam in enumerate(TAMANIOS):
        print(f"{tam:15} | {bubble_results[idx]:.5f} s | {merge_results[idx]:.5f} s | {quick_results[idx]:.5f} s")

# Interfaz gráfica
root = tk.Tk()
root.title("Comparativa de Algoritmos de Ordenamiento")
root.configure(bg=BG)
root.geometry("900x600")

tk.Label(root, text="Escribe un número y presiona un botón", bg=BG).pack(pady=8)
ent = tk.Entry(root, width=24, justify="center")
ent.pack(pady=6)

tam_seleccion = tk.IntVar(value=TAMANIOS[0])
menu = tk.OptionMenu(root, tam_seleccion, *TAMANIOS)
menu.config(bg="white")
menu.pack(pady=4)

tk.Button(root, text="Generar lista", command=gen).pack(pady=6)
tk.Button(root, text="Comparar y graficar", command=comparar).pack(pady=8)
tk.Button(root, text="Imprimir tabla de tiempos", command=imprimir_tabla).pack(pady=8)

info = tk.Label(root, text="(sin lista)", bg=BG)
info.pack(pady=2)
out = tk.Label(root, text="Resultados: —", bg=BG)
out.pack(pady=2)

# Gráfica embebida en Tkinter
if HAS_MPL:
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_title("Tiempos vs N")
    ax.set_xlabel("N")
    ax.set_ylabel("Tiempo (segundos)")
    ax.grid(True, linestyle="--", alpha=0.7)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=8, pady=6)

root.mainloop()
