from Usuario import *
from Curso import *
from carrera import *

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_incripcion, carrera: Carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion = anio_incripcion
        self.mis_cursos = []
        self.carrera = carrera


    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Legajo: {self.__legajo}, Año de Inscripcion: {self.__anio_inscripcion}, Carrera: {self.carrera}"
   

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

    def matricularse_en_curso(self, contrasenia_ing, indice, curso_selec):
    
        if cursos_totales[curso_selec].contrasenia_matriculacion == contrasenia_ing:
            alumnos[indice].mis_cursos.append(cursos_totales[curso_selec])
            print("Matriculado correctamente")
            return True
        else:
            print("Contraseña de curso incorrecta.")
            return False

    def desmatricularse_de_curso(self, indice, curso_selec):
        del alumnos[indice].mis_cursos[curso_selec]
        print("Se desmatriculo correctamente.")

    
alumnos = []

#No sabemos por que pero la contraseña se guarda en el lugar del email y la contraseña....
alumno = Estudiante("Lucas", "Blondel", "blondel@gmail.com", "s", 498453, 2023, carrera)
alumnos.append(alumno)


alumno2 = Estudiante("Matias", "Gimenez", "matigimenez@gmail.com", "maticrack1234", 98564, 2023, carrera)
alumnos.append(alumno2)


