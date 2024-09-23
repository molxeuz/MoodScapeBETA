import tkinter as tk
from tkinter import messagebox

# Función para mostrar el mensaje según el estado de ánimo seleccionado
def mostrar_entorno():
    estado = estado_animo.get()
    if estado == "Feliz":
        messagebox.showinfo("MoodScape", "¡Genial! Te llevaremos a un soleado campo lleno de flores.")
    elif estado == "Tranquilo":
        messagebox.showinfo("MoodScape", "Te dirigimos a una tranquila playa con olas suaves.")
    elif estado == "Estresado":
        messagebox.showinfo("MoodScape", "Te llevaremos a un bosque para relajarte entre los árboles.")
    elif estado == "Creativo":
        messagebox.showinfo("MoodScape", "Entramos en una ciudad futurista donde puedes dejar volar tu imaginación.")
    else:
        messagebox.showinfo("MoodScape", "Selecciona tu estado de ánimo para comenzar.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("MoodScape")

# Crear la etiqueta
etiqueta = tk.Label(ventana, text="¿Cómo te sientes hoy?", font=("Arial", 14))
etiqueta.pack(pady=10)

# Crear el menú desplegable para seleccionar el estado de ánimo
estado_animo = tk.StringVar(ventana)
estado_animo.set("Selecciona tu estado de ánimo")  # Valor por defecto

opciones_estado = ["Feliz", "Tranquilo", "Estresado", "Creativo"]
menu_desplegable = tk.OptionMenu(ventana, estado_animo, *opciones_estado)
menu_desplegable.pack(pady=10)

# Crear el botón para generar el entorno
boton = tk.Button(ventana, text="Generar Entorno", command=mostrar_entorno, font=("Arial", 12), bg="lightblue")
boton.pack(pady=20)

# Iniciar el bucle de la aplicación
ventana.mainloop()
