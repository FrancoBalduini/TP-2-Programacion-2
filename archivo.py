from datetime import date

class Archivo:
    def __init__(self, nombre, formato):
        self.__nombre = nombre
        self.__fecha = date.today()
        self.__formato = formato

    def __str__(self):
        return f"Nombre: {self.__nombre}, Fecha: {self.__fecha}, Formato: {self.__formato}"  
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre_cambiado):
        self.__nombre = nombre_cambiado

    @property
    def formato(self):
        return self.__formato    