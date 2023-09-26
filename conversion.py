import tkinter as tk
from tkinter import ttk


def ip_to_binary():
    ip = entry_ip.get()
    print(ip)
    try:
        # Divide la dirección IP en octetos y los convierte en binario
        octetos = ip.split('.')
        binary_ip = '.'.join([bin(int(octeto))[2:].zfill(8) for octeto in octetos])
        label_result.config(text=f"IP en binario: {binary_ip}")
    except ValueError:
        label_result.config(text="Dirección IP no válida")


# Crear la ventana principal
window = tk.Tk()
window.title("Conversor de IP a Binario")

# Etiqueta y entrada para la dirección IP
label_ip = tk.Label(window, text="Ingrese una dirección IP:")
label_ip.pack()
entry_ip = tk.Entry(window)
entry_ip.pack()

# Botón para realizar la conversión
convert_button = tk.Button(window, text="Convertir a Binario", command=ip_to_binary)
convert_button.pack()

# Etiqueta para mostrar el resultado
label_result = tk.Label(window, text="")
label_result.pack()

# Iniciar la aplicación
window.mainloop()
