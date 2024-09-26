# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:41:55 2024

@author: Karli
"""
import tkinter as tk
from tkinter import messagebox
import re

# Limpiar campos
def CleanData():
    tb_nombre.delete(0, tk.END)
    tb_apellidos.delete(0, tk.END)
    tb_edad.delete(0, tk.END)
    tb_estatura.delete(0, tk.END)
    tb_telefono.delete(0, tk.END)
    op_genero.set(0)

def Delete():
    CleanData()

# Validación de datos
def entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
def telefono_valido(valor):
    return valor.isdigit() and len(valor) == 10

def texto_valido(valor):
    # Corrige la expresión regular para permitir solo letras y espacios
    return bool(re.match("^[a-zA-Z\s]+$", valor))

def SaveData():
    nombres = tb_nombre.get()
    apellidos = tb_apellidos.get()
    edad = tb_edad.get()
    estatura = tb_estatura.get()
    telefono = tb_telefono.get()
    # Obtención de género en los Radiobuttons
    genero = ""
    if op_genero.get() == 1:
        genero = "Hombre"
    elif op_genero.get() == 2:
        genero = "Mujer"
    
    # Validación de los datos
    if (entero_valido(edad) and decimal_valido(estatura) and telefono_valido(telefono)
        and texto_valido(nombres) and texto_valido(apellidos)):
        # Cadena de caracteres
        datos = (
            f"Nombres: {nombres}\n"
            f"Apellidos: {apellidos}\n"
            f"Edad: {edad} años\n"
            f"Estatura: {estatura}\n"
            f"Teléfono: {telefono}\n"
            f"Género: {genero}\n"
 )
        # Guardado de datos
        with open(
            "C:\\Users\\Karli\\Documents\\datosform.txt",
            "a",
        ) as archivo:
            archivo.write(datos + "\n\n")
        
        # Mensaje de confirmación
        messagebox.showinfo("INFORMACIÓN", "Los datos se han guardado correctamente:\n\n" + datos)
    else: 
        # Mensaje de error en caso de validación fallida
        messagebox.showinfo("ERROR", "Los datos contienen formatos no válidos:\n\n")

# Configuración de la ventana principal
window = tk.Tk()
window.geometry("520x500")
window.title("FORMULARIO VR.1")

# Variable para los Radiobuttons
op_genero = tk.IntVar()
# Creación de los campos de entrada
lb_nombre = tk.Label(window, text="Nombres")
lb_nombre.pack()
tb_nombre = tk.Entry(window)
tb_nombre.pack()

lb_apellidos = tk.Label(window, text="Apellidos")
lb_apellidos.pack()
tb_apellidos = tk.Entry(window)
tb_apellidos.pack()

lb_telefono = tk.Label(window, text="Teléfono")
lb_telefono.pack()
tb_telefono = tk.Entry(window)
tb_telefono.pack()

lb_edad = tk.Label(window, text="Edad")
lb_edad.pack()
tb_edad = tk.Entry(window)
tb_edad.pack()

lb_estatura = tk.Label(window, text="Estatura")  # Corregido de "Estatrua"
lb_estatura.pack()
tb_estatura = tk.Entry(window)
tb_estatura.pack()

lb_genero = tk.Label(window, text="Género")
lb_genero.pack()

# Uso de los Radiobuttons
rbHombre = tk.Radiobutton(window, text="Hombre", variable=op_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton(window, text="Mujer", variable=op_genero, value=2)
rbMujer.pack()

# Creación de botones
btnClean = tk.Button(window, text="Borra valores", command=Delete)  # Removido ()
btnClean.pack()
btnSave = tk.Button(window, text="Guardar", command=SaveData)  # Removido ()
btnSave.pack()

# Ejecución de la ventana principal
window.mainloop()
    
