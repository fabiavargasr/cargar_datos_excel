import tkinter as tk
import xlrd



class Ventana:
    def __init__(self, master):
        self.master = master
        master.title("Mi programa con interfaz gráfica")
        
        # Etiquetas de pregunta, texto y respuesta
        self.etiqueta_pregunta = tk.Label(master, text="Pregunta:")
        self.etiqueta_pregunta.grid(row=0, column=0, sticky="w")
        
        self.etiqueta_texto = tk.Label(master, text="Texto:")
        self.etiqueta_texto.grid(row=1, column=0, sticky="w")
        
        self.etiqueta_respuesta = tk.Label(master, text="Respuesta:")
        self.etiqueta_respuesta.grid(row=2, column=0, sticky="w")
        
        # Campos de entrada de texto
        self.entrada_pregunta = tk.Entry(master, width=80)
        self.entrada_pregunta.grid(row=0, column=1, sticky="w", columnspan=2)
        
        self.entrada_texto = tk.Entry(master, width=80)
        self.entrada_texto.grid(row=1, column=1, sticky="w", columnspan=2)
        
        self.entrada_respuesta = tk.Entry(master, width=80)
        self.entrada_respuesta.grid(row=2, column=1, sticky="w", columnspan=2)
        
        # Botones
        self.boton_preguntar = tk.Button(master, text="Preguntar", command=self.imprimir_pregunta)
        self.boton_preguntar.grid(row=3, column=0)
        
        self.boton_sumar = tk.Button(master, text="Sumar", command=self.imprimir_sumar)
        self.boton_sumar.grid(row=3, column=1)
        
        self.boton_cargar = tk.Button(master, text="Cargar", command=self.imprimir_cargar)
        self.boton_cargar.grid(row=3, column=2)
        
        self.boton_almacenar = tk.Button(master, text="Almacenar", command=self.almacenar_respuesta)
        self.boton_almacenar.grid(row=4, column=1)
        
    def imprimir_pregunta(self):
        pregunta = self.entrada_pregunta.get()
        self.entrada_texto.delete(0, tk.END)
        self.entrada_texto.insert(0, pregunta)
        
    def imprimir_sumar(self):
        self.entrada_texto.delete(0, tk.END)
        self.entrada_texto.insert(0, "sumar")
        
    def imprimir_cargar(self):
        self.entrada_texto.delete(0, tk.END)
        self.entrada_texto.insert(0, "cargar")
        nombre_archivo="datos.csv"
        columnad=1
        mat_dat=[]
        mat_dat=self.cargar_archivo_xls('~/Documentos/doctorado/python_gpt/datos.xls')
        #print(nombres)
        
        
        self.imprimir_matriz(mat_dat)
        
        
        
        
    def almacenar_respuesta(self):
        respuesta = self.entrada_respuesta.get()
        with open("respuesta.txt", "w") as archivo:
            archivo.write(respuesta)


    def cargar_archivo_xls(nombre_archivo, columna):
    
        columna=1
        workbook = xlrd.open_workbook(nombre_archivo)
        sheet = workbook.sheet_by_index(0)
        
        column_data = []
        for row in range(sheet.nrows):
            column_data.append(sheet.cell_value(row, columna))
        
        return column_data

    def imprimir_matriz(matriz):
        for fila, valores_fila in enumerate(matriz):
            for columna, valor_celda in enumerate(valores_fila):
                mensaje = f"En el texto se presenta '{valor_celda}' en la posición [{fila}, {columna}]"
                print(mensaje)


# Crear la ventana y ejecutar la aplicación
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
mi_ventana = Ventana(root)
root.mainloop()

# Resumen: Este programa muestra una interfaz gráfica que tiene tres campos de texto para entrada, 
# tres botones que realizan diferentes acciones (imprimir texto en un campo de texto, almacenar texto en un archivo), 
# y un botón
