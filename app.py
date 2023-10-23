from clases import *


while True:
    print("1- Ingresar Alumno.")
    print("2- Ingresar Profesor.")
    print("3- Ver cursos.")
    print("4- Salir.")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        email = input("Ingrese su Email: ")
        contrasenia = input("Ingrese la contraseña: ")
        alumno = Estudiante(email,contrasenia)
        if alumno.email == email and alumno.contrasenia == contrasenia:
            while True:
                print("1- Matricularse a un curso.")
                print("2- Desmatricularse de un curso.")
                print("3- Ver cursos.")
                print("4- Volver al menú principal.")

               
                opcion_Dos = int(input("Ingrese una opción: "))
        else:
            print("Opción Inválida. Intente Nuevamente.")

    elif opcion == 2:
        email = input("Ingrese su Email: ")
        contrasenia = input("Ingrese la contraseña: ")
        profesor = Profesor(email,contrasenia)
        if profesor.email == email and profesor.contrasenia == contrasenia:
            while True:
                print("1- Dictar curso.")
                print("2- Ver cursos.")
                print("3- Volver al menú principal.")

                opcion_Tres = int(input("Ingrese una opción: "))
        else:
            print("Opción Inválida. Intente Nuevamente.")

    elif opcion == 3:
        if "completar ver cursos"

        else:
            print("Todavia no hay cursos disponibles en el campus virtual.\n")

    elif opcion == 4:
        break
    else:
        print("Opción inválida.")

    

