import tkinter as tk
import requests

# Función para obtener el último registro de la API
def obtener_ultimo_registro():
    url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            ultimo_registro = data[-1]  # Obtener el último registro
            mostrar_datos(ultimo_registro)
        else:
            label_resultado.config(text="No se encontraron registros.")
    else:
        label_resultado.config(text="Error al obtener los datos de la API.")

# Función para mostrar los datos del último registro
def mostrar_datos(ultimo_registro):
    texto = (
        f"ID: {ultimo_registro['id']}\n"
        f"Nombre: {ultimo_registro['nombre']}\n"
        f"Apellido: {ultimo_registro['apellido']}\n"
        f"Ciudad: {ultimo_registro['ciudad']}\n"
        f"Calle: {ultimo_registro['calle']}\n"
    )
    label_resultado.config(text=texto)

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Último Registro del Estudiante")
ventana.geometry("350x250")

# Título de la aplicación
titulo = tk.Label(ventana, text="Datos del Último Estudiante", font=("Helvetica", 14, "bold"))
titulo.pack(pady=10)

# Botón para obtener el último registro
boton = tk.Button(ventana, text="Obtener Último Registro", command=obtener_ultimo_registro)
boton.pack(pady=10)

# Etiqueta donde se mostrarán los datos del último registro
label_resultado = tk.Label(ventana, text="", font=("Helvetica", 12), justify="left")
label_resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
