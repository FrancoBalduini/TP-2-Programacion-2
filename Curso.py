import random
import string

class Curso:
    def __init__(self, nombre, contrasenia_matriculacion):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generador_contrasenia()

    def __str__(self):
        return (f"Nombre: {self.__nombre}\nContraseña: {self.__contrasenia_matriculacion}")    
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre_cambiado):
        self.__nombre = nombre_cambiado

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion

    @staticmethod
    def __generador_contrasenia() -> str:
        longitud = 6
        caracteres = string.letras_ascii + string.digitos
        return ''.join(random.choices(caracteres, k=longitud))
    