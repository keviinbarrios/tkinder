# tkinder
# Modulo para crear interfaces graficas de usuario


#importamos el modulo
from tkinter import * 

#crear la ventana raiz
ventana = Tk()

#cambiar titulo
ventana.title("Prueba")

#cambiar el tamaño de la ventana
ventana.geometry("750x450")

#bloquear el tamaño de la ventana
ventana.resizable(0,0)



# Arrancar y mostrar la ventana hasta que se cierre 
ventana.mainloop()



