import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

window = tk.Tk()
window.title("Calculadora de Máscara de Red y Subredes TIPO C")
window.geometry("1200x1200")
window.configure(bg="#0e8c96")

#TIPO A ---- TIPO A

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
    
    if int(ipsplit[1]) != 0 or int(ipsplit[2]) != 0 or int(ipsplit[3]) !=0 :
        messagebox.showwarning("Advertencia", "No metas locuras, hay valor que necesitan ser 0")
        window.quit()
    
    octetos = ip.split('.')
    binary_ip = '.'.join([bin(int(octeto))[2:].zfill(8) for octeto in octetos])
    label_resultmascara1.config(text=f"IP en binario: {binary_ip}")    
    
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
    
    octetos = mascara.split('.')
    binary_ip2 = '.'.join([bin(int(octeto))[2:].zfill(8) for octeto in octetos])
    label_resultmascara2.config(text=f"Mascara de Red: {binary_ip2}")
    
    
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
            text_area1.insert(tk.INSERT, cadena_modificada + "\n" )  
        subredes = subredes - 1


frame1 = tk.Frame(window, bg='black',padx=10,pady=10)
frame1.pack(side="left",fill="both",expand=True)


label_ip1 = tk.Label(frame1, text="TIPO A ---- Ingrese una dirección IP:")
label_ip1.pack()
entry_ip1 = tk.Entry(frame1)
entry_ip1.pack()

# Etiqueta y entrada para el número de subredes
label_subredes1 = tk.Label(frame1, text="Número de subredes:")
label_subredes1.pack()
entry_subredes1 = tk.Entry(frame1)
entry_subredes1.pack()

# Botón para calcular
calcular_button1 = tk.Button(frame1, text="Calcular", command=calcular_mascara_y_subredesA)
calcular_button1.pack()


resultado21 = tk.Label(frame1, text="")
resultado21.pack()

# Etiqueta para mostrar el resultado
resultado13 = tk.Label(frame1, text="")
resultado13.pack()

label_resultmascara1 = tk.Label(frame1, text="")
label_resultmascara1.pack()

label_resultmascara2 = tk.Label(frame1, text="")
label_resultmascara2.pack()




# Etiqueta para mostrar las subredes
resultado_subredes1 = tk.Label(frame1, text="")
resultado_subredes1.pack()

text_area1 = scrolledtext.ScrolledText(frame1, width=15, height=20, font=('Times New Roman', 15))
text_area1.pack()


# ---- TIPO B -----

def calcular_mascara_y_subredesB():
    ip = entry_ip2.get()
    subredes = int(entry_subredes2.get())
    

    
    mascara = '255.255'
    ipsplit = ip.split('.')
    ip1 = int(ipsplit[0])
    ip2 = int(ipsplit[2])
    
    
    if  int(ipsplit[2]) != 0 or int(ipsplit[3]) !=0 :
        messagebox.showwarning("Advertencia", "No metas locuras, hay valor que necesitan ser 0")
        window.quit()
    
    octetos = ip.split('.')
    binary_ip = '.'.join([bin(int(octeto))[2:].zfill(8) for octeto in octetos])
    label_resultmascara11.config(text=f"IP en binario: {binary_ip}")
    
    
    
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
    
    resultado22.config(text=f'Numerode hosts: {resultado1} ')
    resultado2.config(text=f'Máscara de red: {mascara}')
    
    
    octetos = mascara.split('.')
    binary_ip22 = '.'.join([bin(int(octeto))[2:].zfill(8) for octeto in octetos])
    label_resultmascara22.config(text=f"Mascara de Red: {binary_ip22}")
    
    
    
    combinaciones1 = int(256 / (2 ** exponente))
    
    r = 1
    
    resultado_subredes2.config(text="Subredes generadas:")
    
    while subredes != 0:
        cadena_original = ip
        nuevo_par = str(combinaciones1 * r)
        r = r + 1
        partes = cadena_original.split(".")
        if len(partes) >= 4:  # Asegúrate de que haya al menos 4 partes (para modificar el penúltimo)
            partes[-2] = nuevo_par  # Modificar el penúltimo elemento
            cadena_modificada = ".".join(partes)
            text_area2.insert(tk.INSERT, cadena_modificada + "\n" )
            
        subredes = subredes - 1


frame2 = tk.Frame(window, bg='white',padx=10,pady=10)
frame2.pack(side="left",fill="both",expand=True)

# Etiqueta y entrada para la dirección IP
label_ip2 = tk.Label(frame2, text="TIPO B ---- Ingrese una dirección IP:")
label_ip2.pack()
entry_ip2 = tk.Entry(frame2)
entry_ip2.pack()

# Etiqueta y entrada para el número de subredes
label_subredes2 = tk.Label(frame2, text="Número de subredes:")
label_subredes2.pack()
entry_subredes2 = tk.Entry(frame2)
entry_subredes2.pack()

# Botón para calcular
calcular_button2 = tk.Button(frame2, text="Calcular", command=calcular_mascara_y_subredesB)
calcular_button2.pack()


resultado22 = tk.Label(frame2, text="")
resultado22.pack()

# Etiqueta para mostrar el resultado
resultado2 = tk.Label(frame2, text="")
resultado2.pack()


label_resultmascara11 = tk.Label(frame2, text="")
label_resultmascara11.pack()

label_resultmascara22 = tk.Label(frame2, text="")
label_resultmascara22.pack()

# Etiqueta para mostrar las subredes
resultado_subredes2 = tk.Label(frame2, text="")
resultado_subredes2.pack()

text_area2 = scrolledtext.ScrolledText(frame2, width=15, height=20, font=('Times New Roman', 15))
text_area2.pack()


# ----- TIPO C ------

def calcular_mascara_y_subredesC():
    ip = entry_ip3.get()
    subredes = int(entry_subredes3.get())
    
    mascara = '255.255.255'
    ipsplit = ip.split('.')
    
  
    ipsplit = ip.split('.')
    ip1 = int(ipsplit[0])
    ip2 = int(ipsplit[3])
    
    if   int(ipsplit[3]) !=0 :
        messagebox.showwarning("Advertencia", "No metas locuras, hay valor que necesitan ser 0")
        window.quit()
        

      
    octetos = ip.split('.')
    binary_ip = '.'.join([bin(int(octeto))[2:].zfill(8) for octeto in octetos])
    label_resultmascara111.config(text=f"IP en binario: {binary_ip}")
    
    
    
    
    
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
    
    octetos = mascara.split('.')
    binary_ip222 = '.'.join([bin(int(octeto))[2:].zfill(8) for octeto in octetos])
    label_resultmascara222.config(text=f"Mascara de Red: {binary_ip222}")
    
    
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
            text_area3.insert(tk.INSERT, cadena_modificada + "\n" )
        subredes = subredes - 1


frame3 = tk.Frame(window, bg='black',padx=10,pady=10)
frame3.pack(side="left",fill="both",expand=True)

# Etiqueta y entrada para la dirección IP
label_ip3 = tk.Label(frame3, text="TIPO C ----- Ingrese una dirección IP:")
label_ip3.pack()
entry_ip3 = tk.Entry(frame3)
entry_ip3.pack()

# Etiqueta y entrada para el número de subredes
label_subredes3 = tk.Label(frame3, text="Número de subredes:")
label_subredes3.pack()
entry_subredes3 = tk.Entry(frame3)
entry_subredes3.pack()

# Botón para calcular
calcular_button3 = tk.Button(frame3, text="Calcular", command=calcular_mascara_y_subredesC)
calcular_button3.pack()


resultado23= tk.Label(frame3, text="")
resultado23.pack()

# Etiqueta para mostrar el resultado
resultado3 = tk.Label(frame3, text="")
resultado3.pack()


label_resultmascara111 = tk.Label(frame3, text="")
label_resultmascara111.pack()

label_resultmascara222 = tk.Label(frame3, text="")
label_resultmascara222.pack()


# Etiqueta para mostrar las subredes
resultado_subredes3 = tk.Label(frame3, text="")
resultado_subredes3.pack()

text_area3 = scrolledtext.ScrolledText(frame3, width=15, height=20, font=('Times New Roman', 15))
text_area3.pack()

#IP A BINARIO


def ip_to_binary():
    ip = entry_ip4.get()
    print(ip)
    try:
        # Divide la dirección IP en octetos y los convierte en binario
        octetos = ip.split('.')
        binary_ip = '.'.join([bin(int(octeto))[2:].zfill(8) for octeto in octetos])
        label_result4.config(text=f"IP en binario: {binary_ip}")
    except ValueError:
        label_result4.config(text="Dirección IP no válida")

frame4 = tk.Frame(window, bg='white',padx=10,pady=10)
frame4.pack(side="left",fill="both",expand=True)

# Etiqueta y entrada para la dirección IP
label_ip4 = tk.Label(frame4, text="Ingrese una dirección IP:")
label_ip4.pack()
entry_ip4 = tk.Entry(frame4)
entry_ip4.pack()

# Botón para realizar la conversión
convert_button4 = tk.Button(frame4, text="Convertir a Binario", command=ip_to_binary)
convert_button4.pack()

# Etiqueta para mostrar el resultado
label_result4 = tk.Label(frame4, text="")
label_result4.pack()




# Iniciar la aplicación
window.mainloop()

