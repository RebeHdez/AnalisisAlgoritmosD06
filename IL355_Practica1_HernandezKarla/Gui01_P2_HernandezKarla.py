import tkinter as tk

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "mundo"
    lbl.config(text=f"Hola Compa, {nombre} 👋")

root = tk.Tk()
root.title("Saludada de Compas😁👍")
root.geometry("460x420")
root.configure(bg="lightblue")

lbl = tk.Label(root, text="Ey, Escribe tu nombre y presiona el botón", bg="lightblue")
lbl.pack(pady=50)

entrada = tk.Entry(root)
entrada.pack(pady=30)

btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=10)

btn = tk.Button(root, text="Saludaa", command=saludar)
btn.pack(pady=10)

root.mainloop()
