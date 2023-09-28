import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

def calcular_mascara_y_subredesA():
    ip = entry_ip1.get()
    subredes = int(entry_subredes1.get())
    
    mascara = '255'
    ipsplit = ip.split('.')
    
    ipsplit = ip.split('.')
    ip1 = int(ipsplit[0])
    ip2 = int(ipsplit[1])
    if ip1 <= 0 or ip1 >= 128 :
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
    mascara = mascara + '.' + str(k) + '.0.0'
    print(mascara)
    resultado1=pow(2,x + 14)-2
    if resultado1 < 0 :
        resultado1 = 0
        
    resultado21.config(text=f'Numero de hosts: {resultado1} ')
    resultado13.config(text=f'Máscara de red: {mascara}')
    
    combinaciones1 = int(256 / (2 ** exponente))
    
    r = 1
    
    resultado_subredes1.config(text="Subredes generadas:")
    
    while subredes != 0:
        cadena_original = ip
        nuevo_par = str(combinaciones1 * r)
        r = r + 1
        partes = cadena_original.split(".")
        if len(partes) >= 4:  
            partes[-3] = nuevo_par  
            cadena_modificada = ".".join(partes)
            resultado_subredes1.config(text=resultado_subredes1.cget("text") + f'\n{cadena_modificada}')  
        subredes = subredes - 1
# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora de Máscara de Red y Subredes TIPO A")
window.geometry("600x1200")
window.configure(bg="#0e8c96")

# Etiqueta y entrada para la dirección IP
label_ip1 = tk.Label(window, text="Ingrese una dirección IP:")
label_ip1.pack()
entry_ip1 = tk.Entry(window)
entry_ip1.pack()

# Etiqueta y entrada para el número de subredes
label_subredes1 = tk.Label(window, text="Número de subredes:")
label_subredes1.pack()
entry_subredes1 = tk.Entry(window)
entry_subredes1.pack()

# Botón para calcular
calcular_button1 = tk.Button(window, text="Calcular", command=calcular_mascara_y_subredesA)
calcular_button1.pack()


resultado21 = tk.Label(window, text="")
resultado21.pack()

# Etiqueta para mostrar el resultado
resultado13 = tk.Label(window, text="")
resultado13.pack()

# Etiqueta para mostrar las subredes
resultado_subredes1 = tk.Label(window, text="")
resultado_subredes1.pack()

# Iniciar la aplicación
window.mainloop()
