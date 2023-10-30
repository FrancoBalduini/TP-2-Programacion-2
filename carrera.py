class Carrera:
    def __init__(self, nombre, cant_anios):
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.cursos = []

    def __str__ (self):
        return f"Nombre: {self.__nombre}, Cantidad de Años: {self.__cant_anios}"

    @property
    def nombre(self):
        return self.__nombre
    
    def agr_curso(self, curso):
        self.cursos.append(curso)

    def get_cant_materias(self):
        return len(self.cursos)
    

carreras_totales = []
carrera = Carrera("Tecnicatura Universitaria en Programación", 2)
carreras_totales.append(carrera)
