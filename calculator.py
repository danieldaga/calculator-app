import tkinter as tk
from tkinter import messagebox  # Importar el módulo messagebox
import math

# Creacion ventana principal
root = tk.Tk()
root.title("Calculadora Científica")

# Lista para almacenar los cálculos
memory = []

# Función para manejar los clics de los botones
def handle_click(value):
    if value == '=':
        try:
            result = eval(screen.get())
            memory.append(screen.get() + ' = ' + str(result))
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif value == 'C':
        screen.delete(0, tk.END)
    elif value == 'M':
        memory_text = '\n'.join(memory)
        messagebox.showinfo("Memoria", memory_text)  # Utilizar messagebox.showinfo()
    elif value == 'MC':
        memory.clear()
    elif value == 'sin':
        screen.insert(tk.END, 'math.sin(')
    elif value == 'cos':
        screen.insert(tk.END, 'math.cos(')
    elif value == 'tan':
        screen.insert(tk.END, 'math.tan(')
    else:
        screen.insert(tk.END, value)

# Crear la pantalla de la calculadora
screen = tk.Entry(root, width=25, font=("Arial", 18), justify="right", bg="lightgray", borderwidth=2, relief="solid")
screen.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

# Crear los botones
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'sin', 'cos', 'tan', 'π', '(', ')', '^', '√',
    'M', 'MC'
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 12),
                    command=lambda button=button: handle_click(button), bg="lightblue", borderwidth=2, relief="solid")
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 5:
        col = 0
        row += 1

# Configurar el comportamiento de la ventana
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

# Ejecutar la aplicación
root.mainloop()
