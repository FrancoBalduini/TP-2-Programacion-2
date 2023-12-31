import random
import string
from archivo import Archivo


class Curso:
    prox_codigo = 0
    def __init__(self, nombre, carrera):
        Curso.prox_codigo += 1
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generador_contrasenia()
        self.archivos = []
        self.__codigo = Curso.prox_codigo
        self.carrera = carrera
    #Le asignamos la carrera para poder mostrarla en la opcion 3
    

    def __str__(self):
        return (f"Nombre: {self.__nombre}\nContraseña: {self.__contrasenia_matriculacion}\nArchivos: {self.archivos}\n")    
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre_cambiado):
        self.__nombre = nombre_cambiado

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @property
    def codigo(self):
        return self.__codigo

    @staticmethod
    def __generador_contrasenia() -> str:
        longitud = 8
        caracteres = string.ascii_letters + string.digits
        return "".join(random.choices(caracteres, k=longitud))
    
    def archivo(self, archivo: Archivo):
        self.archivos.append(archivo)
    

cursos_totales = []
    