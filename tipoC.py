import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

def calcular_mascara_y_subredesC():
    ip = entry_ip3.get()
    subredes = int(entry_subredes3.get())
    
    mascara = '255.255.255'
    ipsplit = ip.split('.')
    
    ipsplit = ip.split('.')
    ip1 = int(ipsplit[0])
    ip2 = int(ipsplit[3])
    if ip1 < 192 or ip1 >= 224 :
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
    mascara = mascara + '.' + str(k)
    resultado1=pow(2,x)-2
    if resultado1 < 0 :
        resultado1 = 0
        
    resultado23.config(text=f'Numero de hosts: {resultado1} ')
    resultado3.config(text=f'Máscara de red: {mascara}')
    
    combinaciones1 = int(256 / (2 ** exponente))
    
    r = 1
    
    resultado_subredes3.config(text="Subredes generadas:")
    
    while subredes != 0:
        cadena_original = ip
        nuevo_par = str(combinaciones1 * r)
        r = r + 1
        partes = cadena_original.split(".")
        if len(partes) >= 3:
            partes[-1] = nuevo_par
            cadena_modificada = ".".join(partes)
            resultado_subredes3.config(text=resultado_subredes3.cget("text") + f'\n{cadena_modificada}')
            subredes = subredes - 1

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora de Máscara de Red y Subredes TIPO C")
window.geometry("600x1200")
window.configure(bg="#0e8c96")

# Etiqueta y entrada para la dirección IP
label_ip3 = tk.Label(window, text="Ingrese una dirección IP:")
label_ip3.pack()
entry_ip3 = tk.Entry(window)
entry_ip3.pack()

# Etiqueta y entrada para el número de subredes
label_subredes3 = tk.Label(window, text="Número de subredes:")
label_subredes3.pack()
entry_subredes3 = tk.Entry(window)
entry_subredes3.pack()

# Botón para calcular
calcular_button3 = tk.Button(window, text="Calcular", command=calcular_mascara_y_subredes)
calcular_button3.pack()


resultado23= tk.Label(window, text="")
resultado23.pack()

# Etiqueta para mostrar el resultado
resultado3 = tk.Label(window, text="")
resultado3.pack()

# Etiqueta para mostrar las subredes
resultado_subredes3 = tk.Label(window, text="")
resultado_subredes3.pack()

# Iniciar la aplicación
window.mainloop()
