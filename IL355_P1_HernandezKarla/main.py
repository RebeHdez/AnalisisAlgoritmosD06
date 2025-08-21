import tkinter as tk, random, time
from tkinter import messagebox
from algoritmos import busqueda_lineal, busqueda_binaria

HAS_MPL = True
try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
except Exception:
    HAS_MPL = False

BG = "lightblue"
TAMANIOS = [100, 1000, 10000, 100000]
datos = []
tam_seleccion = None

def gen():
    global datos
    n = tam_seleccion.get()
    datos = sorted(random.sample(range(n*3), n))
    info.config(text=f"Lista generada (n={len(datos)})")
    out.config(text="Resultados: —")

def buscar(metodo, nombre):
    if not datos:
        return messagebox.showwarning("Aviso", "Primero genera la lista")
    txt = ent.get().strip()
    if not txt:
        return messagebox.showerror("Error", "Escribe un número entero")
    try: x = int(txt)
    except ValueError:
        return messagebox.showerror("Error", "Solo enteros")
    t0 = time.perf_counter()
    idx = metodo(datos, x)
    ms = (time.perf_counter()-t0)*1000
    msg = "no encontrado" if idx == -1 else f"índice {idx}"
    out.config(text=f"{nombre}: {msg} | {ms:.3f} ms")

def comparar():
    if not HAS_MPL:
        return messagebox.showinfo("Gráfica no disponible",
                                   "Instala matplotlib con:\n\npip install matplotlib")
    xs, L, B = [100, 1000, 10000], [], []
    for n in xs:
        arr = sorted(random.sample(range(n*3), n))
        x = arr[-1]
        t0 = time.perf_counter(); busqueda_lineal(arr, x); L.append((time.perf_counter()-t0)*1000)
        t0 = time.perf_counter(); busqueda_binaria(arr, x); B.append((time.perf_counter()-t0)*1000)
    ax.clear()
    ax.set_title("Tiempos (ms) | n"); ax.set_xlabel("n"); ax.set_ylabel("ms")
    ax.plot(xs, L, "o-", label="Lineal"); ax.plot(xs, B, "o-", label="Binaria")
    ax.set_xscale("log"); ax.grid(True, linestyle="--", alpha=.3); ax.legend()
    canvas.draw_idle()

# GUI
root = tk.Tk(); root.title("Búsqueda RH😜"); root.configure(bg=BG); root.geometry("900x600")

tk.Label(root, text="Escribe un número y presiona un botón", bg=BG).pack(pady=8)
ent = tk.Entry(root, width=24, justify="center"); ent.pack(pady=6)

# menu de tamaño
tam_seleccion = tk.IntVar(value=TAMANIOS[0])
menu = tk.OptionMenu(root, tam_seleccion, *TAMANIOS)
menu.config(bg="white")
menu.pack(pady=4)

tk.Button(root, text="Generar lista", command=gen).pack(pady=6)
tk.Button(root, text="Búsqueda Lineal",  command=lambda: buscar(busqueda_lineal,"Lineal")).pack(pady=4)
tk.Button(root, text="Búsqueda Binaria", command=lambda: buscar(busqueda_binaria,"Binaria")).pack(pady=4)
tk.Button(root, text="Comparar y graficar", command=comparar,
          state=("normal" if HAS_MPL else "disabled")).pack(pady=8)

info = tk.Label(root, text="(sin lista)", bg=BG); info.pack(pady=2)
out  = tk.Label(root, text="Resultados: —", bg=BG); out.pack(pady=2)
# Grafica
if HAS_MPL:
    fig = Figure(figsize=(5.6,3.2), dpi=100); ax = fig.add_subplot(111)
    ax.set_title("Tiempos (ms) vs n"); ax.set_xlabel("n"); ax.set_ylabel("ms"); ax.grid(True, linestyle="--", alpha=.3)
    canvas = FigureCanvasTkAgg(fig, master=root); canvas.get_tk_widget().pack(fill="both", expand=True, padx=8, pady=6)

root.mainloop()
