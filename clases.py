import Usuario
import string
import random
import Curso 

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_incripcion):
        super.__init__(self, nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion = anio_incripcion
        self.mis_cursos = []


    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Legajo: {self.__legajo}, Año de Inscripcion: {self.__anio_inscripcion}"
   

    @property
    def legajo(self):
        return self.__legajo

    @legajo.setter
    def legajo(self, legajo_cambiado):
        self.__legajo = legajo_cambiado

    @property
    def anio_inscripcion(self):
        return self.__anio_inscripcion

    @anio_inscripcion.setter
    def anio_inscripcion(self, anio_inscripcion_cambiado):
        self.__anio_inscripcion = anio_inscripcion_cambiado 

    def matricularse_en_curso(self, curso, contrasenia_matriculacion):
        if curso.carrera == self.carrera:
            if curso not in self.mi_cursos and curso.contrasenia_matriculacion == contrasenia_matriculacion:
                self.mi_cursos.append(curso)
                return True
        return False

    def ver_cursos_matriculados(self):
        return self.mi_cursos    
    
class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super.__init__(self, nombre, apellido, email, contrasenia)
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


alumnos = []


cursos= []


profesor = Profesor("Dario", "Martinez", "martinesdario@gmail.com", "dariomartinez", "ingeniero", 1987)
profesores.append(profesor)


alumno1 = Estudiante("Lucas", "Blondel", "blondel@gmail.com", "lblondel123", 498453, 2023)
alumnos.append(alumno1)


alumno2 = Estudiante("Matias", "Gimenez", "matigimenez@gmail.com", "maticrack1234", 98564, 2023)
alumnos.append(alumno2)


