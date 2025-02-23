import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
from tqdm import tqdm  # Barra de progreso en consola

# Ruta de Poppler (ajusta según tu instalación)
POPPLER_PATH = r"C:\poppler\bin"

# Función para convertir los PDFs seleccionados a imágenes JPG
def convertir_pdfs():
    archivos_pdf = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
    if not archivos_pdf:  # Si no se seleccionaron archivos
        messagebox.showwarning("Advertencia", "No se seleccionaron archivos PDF.")
        return

    carpeta_salida = filedialog.askdirectory()  # Elige la carpeta de salida
    if not carpeta_salida:  # Si no se seleccionó una carpeta de salida
        messagebox.showwarning("Advertencia", "No se seleccionó una carpeta de salida.")
        return

    # Convierte cada archivo PDF seleccionado
    for archivo_pdf in archivos_pdf:
        try:
            nombre_pdf = os.path.splitext(os.path.basename(archivo_pdf))[0]  # Nombre del archivo sin extensión
            imagenes = convert_from_path(archivo_pdf, poppler_path=POPPLER_PATH)

            # Guardar cada página como JPG
            for i, imagen in enumerate(imagenes):
                nombre_salida = os.path.join(carpeta_salida, f"{nombre_pdf}_pagina_{i+1}.jpg")
                imagen.save(nombre_salida, "JPEG")

            messagebox.showinfo("Éxito", f"Conversión completada: {nombre_pdf}")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo convertir {archivo_pdf}: {e}")

# Crear la ventana de interfaz gráfica
ventana = tk.Tk()
ventana.title("Convertidor PDF a JPG")
ventana.geometry("400x200")

# Etiqueta de la ventana
tk.Label(ventana, text="Conversor de PDF a JPG", font=("Arial", 14)).pack(pady=10)

# Botón para seleccionar los archivos y convertir
tk.Button(ventana, text="Seleccionar PDFs y Convertir", command=convertir_pdfs, font=("Arial", 12), bg="lightblue").pack(pady=20)

# Iniciar la ventana de la interfaz
ventana.mainloop()

