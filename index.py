import tkinter as tk
import requests
from tkinter import messagebox

class DAO:
    def __init__(self):
        self.__url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def ultimo_dato(self):
        response = requests.get(self.__url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[-1]
        return None


class aña:
    def __init__(self, sus):
        self.__sus = sus
        self.__sus.title("Último Dato")
        self.__sus.geometry("300x200")

        self.__etiqueta = tk.Label(self.__sus, text="Último Dato Del Registro", justify="left")
        self.__etiqueta.pack(pady=20)

        self.__boton2 = tk.Button(self.__sus, text="Obtener ultimo dato", command=self.__mostrar)
        self.__boton2.pack(pady=10)

    def __mostrar(self):
        dao = DAO()
        ultimo = dao.ultimo_dato()

        if ultimo:

            datos = (
                f"ID: {ultimo['id']}\n"
                f"Nombre: {ultimo['nombre']}\n"
                f"Apellido: {ultimo['apellido']}\n"
                f"Ciudad: {ultimo['ciudad']}\n"
                f"Calle: {ultimo['calle']}"
            )
            self.__etiqueta.config(text=datos)
        else:
            messagebox.showerror("Error", "No se pudo obtener el último dato.")
