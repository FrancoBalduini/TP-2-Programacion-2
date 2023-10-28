class Carrera:
    def __init__(self, nombre, cant_anios):
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__cursos = []
        self.__alumnos = []

    def __str__ (self):
        return f"Nombre: {self.__nombre}, Cantidad de Años: {self.__cant_anios}"

    @property
    def nombre(self):
        return self.__nombre
   
    @property
    def cursos(self):
        return self.__cursos
    
    def agr_curso(self, curso):
        self.__cursos.append(curso)

    def get_cant_materias(self):
        return len(self.__cursos)
    

