import tkinter as tk

root = tk.Tk()
root.title("Mi primera GUI :) lol")
root.geometry("1250x400")
root.configure(bg="lightpink")

lbl = tk.Label(root, text="¡Holii, GUI!", bg="lightpink")
lbl.pack(pady=50)

root.mainloop()