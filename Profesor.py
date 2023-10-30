from Usuario import *
from Curso import *
from carrera import *


class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.mis_cursos = []

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Título: {self.__titulo}, Año de Egreso: {self.__anio_egreso}"    
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo_cambiado):
        self.__titulo = titulo_cambiado

    @property
    def anio_egreso(self):
        return self.__anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, anio_egreso_cambiado):
        self.__anio_egreso = anio_egreso_cambiado


    def dictar_curso(self, curso: Curso):
        self.mis_cursos.append(curso)

    def ver_cursos_dictados(self):
        return self.mis_cursos    



profesores = []


#No sabemos por que pero la contraseña se guarda en el lugar del email y la contraseña....
profesor = Profesor("Catalina", "Lopez", "catlopez@gmail.com", "a", "Ingeniera", 1996)
profesores.append(profesor)

profesor = Profesor("Dario", "Martinez", "martinesdario@gmail.com", "martinezD87", "ingeniero", 1987)
profesores.append(profesor)