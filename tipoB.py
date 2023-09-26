import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calcular_mascara_y_subredesB():
    ip = entry_ip.get()
    subredes = int(entry_subredes.get())
    
    mascara = '255.255'
    ipsplit = ip.split('.')
    ip1 = int(ipsplit[0])
    ip2 = int(ipsplit[2])
    if ip1 >= 192 or ip1 < 128 :
        messagebox.showwarning("Advertencia", "No metas locuras")
        window.quit()
    if ip2 != 0 :
        messagebox.showwarning("Advertencia", "No se puede realizar de esta manera,no se puede con valores mayores a 0")
        window.quit()
        
    numero_dado = subredes
    exponente = 1
    base = 1
    
    while base < numero_dado:
        exponente += 1
        base = 2 ** exponente
    
    n = exponente
    x = 7
    k = 0
    while n != 0 :
        k = k +  pow(2,x)
        n = n-1
        x= x-1
    mascara = mascara + '.' + str(k) + '.0'
    resultado1=pow(2,x +7)-2
    resultado2.config(text=f'Numerode hosts: {resultado1} ')
    resultado.config(text=f'Máscara de red: {mascara}')
    
    combinaciones1 = int(256 / (2 ** exponente))
    
    r = 1
    
    resultado_subredes.config(text="Subredes generadas:")
    
    while subredes != 0:
        cadena_original = ip
        nuevo_par = str(combinaciones1 * r)
        r = r + 1
        partes = cadena_original.split(".")
        if len(partes) >= 4:  # Asegúrate de que haya al menos 4 partes (para modificar el penúltimo)
            partes[-2] = nuevo_par  # Modificar el penúltimo elemento
            cadena_modificada = ".".join(partes)
            resultado_subredes.config(text=resultado_subredes.cget("text") + f'\n{cadena_modificada}')
        subredes = subredes - 1


# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora de Máscara de Red y Subredes Tipo B")
window.geometry("600x1200")

window.configure(bg="#0e8c96")


# Etiqueta y entrada para la dirección IP
label_ip = tk.Label(window, text="Ingrese una dirección IP:")
label_ip.pack()
entry_ip = tk.Entry(window)
entry_ip.pack()

# Etiqueta y entrada para el número de subredes
label_subredes = tk.Label(window, text="Número de subredes:")
label_subredes.pack()
entry_subredes = tk.Entry(window)
entry_subredes.pack()

# Botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=calcular_mascara_y_subredesB)
calcular_button.pack()


resultado2 = tk.Label(window, text="")
resultado2.pack()

# Etiqueta para mostrar el resultado
resultado = tk.Label(window, text="")
resultado.pack()

# Etiqueta para mostrar las subredes
resultado_subredes = tk.Label(window, text="")
resultado_subredes.pack()

# Iniciar la aplicación
window.mainloop()
