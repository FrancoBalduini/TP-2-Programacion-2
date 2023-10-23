from abc import ABC, abstractmethod

class Usuario(ABC): 
    def __init__(self, nombre, apellido, email, contrasenia):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
    

    @abstractmethod
    def __str__():
        pass

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre_cambiado):
        self._nombre = nombre_cambiado

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido_cambiado):
        self._apellido = apellido_cambiado

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email_cambiado):
        self._email = email_cambiado

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def email(self, contrasenia_cambiada):
        self._contrasenia = contrasenia_cambiada
    
    def validar_credenciales(self, email, contrasenia) -> bool: 
        return self.email == email and self.contrasenia == contrasenia
    
