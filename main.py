import tkinter as tk
from tkinter import  messagebox
from funciones import * 

lista_nombres = None
diccionario_nombres = None


def main():
    root = tk.Tk()
    root.title("Python, parcial n°1")
    root.geometry("300x300")

    def mostrar_ordernarNombres():
        global lista_nombres  
        try:
            lista_nombres = ordernarNombres() 
            messagebox.showinfo("Lista", lista_nombres)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        
    boton = tk.Button(root, text="Ordenar Nombres", command=mostrar_ordernarNombres)
    boton.pack(pady=10)  
    
    
    def mostrar_convertirDiccionario():
        global diccionario_nombres
        if lista_nombres: 
            try:
                diccionario_nombres = convertirDiccionario(lista_nombres)
                messagebox.showinfo("Diccionario", diccionario_nombres)
            except Exception as e:
                messagebox.showerror("Error", f"{e}")
        else:
            messagebox.showwarning("Error", "Primero debes ordenar los nombres")
        
    boton2 = tk.Button(root, text="Convertir a diccionario", command=mostrar_convertirDiccionario)
    boton2.pack(pady=10)    
    
    
    def crear_frecuenciaNombres():
        if diccionario_nombres: 
            try:
                txtFrecuenciaNombres(diccionario_nombres)  
                messagebox.showinfo("Txt", "Archivo de frecuencia de nombres creado")
            except Exception as e:
                messagebox.showerror("Error", f"{e}")
        else:
            messagebox.showwarning("Error", "Primero debes convertir los nombres a diccionario")
    
    boton3 = tk.Button(root, text="Crear archivo txt", command=crear_frecuenciaNombres)
    boton3.pack(pady=10)  
    
    
    def mostrar_graficoNombres():
        try:
            graficoFrecuenciaNombres()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    boton4 = tk.Button(root, text="Crear grafico nombres", command= mostrar_graficoNombres)
    boton4.pack(pady=10)
    

    def mostrar_cadenaInicialMayuscula():
        cadena = "hola, como estas y holah hh?"
        messagebox.showinfo("Cadena", inicialMayuscula(cadena))
    
    boton5 = tk.Button(root, text="Cadena con inicial mayuscula", command= mostrar_cadenaInicialMayuscula)
    boton5.pack(pady=10)
    
    
    root.mainloop()
    
    
    
if __name__ == "__main__":
    main()

