from clases import *
from Curso import *


while True:
    print("1- Ingresar Alumno.")
    print("2- Ingresar Profesor.")
    print("3- Ver cursos.")
    print("4- Salir.")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        mail = input("Ingrese su Email: ")
        contra = input("Ingrese la contraseña: ")
        for alumn in alumnos:
            bandera = alumn.validar_credenciales(mail, contra)

            if bandera:
                break

        if bandera:
            opcion_Dos = 0
            while opcion_Dos !=3 :
                print("1- Matricularse a un curso.")
                print("2- Ver cursos.")
                print("3- Volver al menú principal.")
                
                opcion_Dos = int(input("Ingrese una opción: "))

                if opcion_Dos == 1:
                    i = 0
                    
                    for curso in cursos_totales:
                        i += 1
                        print(f"{i} {curso.nombre}")

                    curso_selec = int(input("Ingrese el numero del curso al que desea matricularse: "))
                    curso_selec -= 1
                    if not cursos_totales[curso_selec] in alumno.mis_cursos:
                        nombre_curso = cursos_totales[curso_selec].nombre 
                        clave_curso = input("Ingrese la contraseña de dicho curso: ")
                        alumno.matricularse_en_curso(nombre_curso, clave_curso)
                    else:
                        print("Ya se encuentra matriculado a ese curso.")

                elif opcion_Dos == 2:
                    
                    i = 0
                    for curso in alumno.mis_cursos:
                        i += 1
                        print(f"{i} {curso.nombre}")
                #no esta la parte de pedir la opcion, sentimos que no tiene sentido mostrar la lista con los nombres para dsp volverle a decir el nombre
                else:
                    print("seleccione una opcion valida")
        
        else:
            print("Opción Inválida. Intente Nuevamente.")

    elif opcion == 2:
        mail = input("Ingrese su Email: ")
        contra = input("Ingrese la contraseña: ")
        for prof in profesores:
            print(prof.nombre)
            print(prof.apellido)
            print(prof.email)
            print(prof.contrasenia)

            bandera = prof.validar_credenciales(mail, contra)

            if bandera:
                break
        if bandera:
            opcion_Dos = 0
            while opcion_Dos !=3:
                print("1- Dictar curso.")
                print("2- Ver cursos.")
                print("3- Volver al menú principal.")

                opcion_Dos = int(input("Ingrese una opción: "))
                
                if opcion_Dos == 1:
                    curso = Curso(str(input("Ingrese el nombre del nuevo curso: ")))
                    cursos_totales.append(curso)
                    profesor.mis_cursos.append(curso)
                    print(f"Nombre: {curso.nombre} \nContraseña: {curso.contrasenia_matriculacion}")
                elif opcion_Dos == 2:
                    i = 0

                    for curso in profesor.mis_cursos:
                        i += 1
                        print(f"{i} {curso.nombre}")
                    
                    banderaWh = False
                    while not banderaWh:
                        curso_selec = int(input("Ingrese el numero del curso del cual desea conocer los datos: "))
                        if curso_selec <= i and curso_selec > 0:
                            banderaWh = True
                        else:
                            print("Ingrese una opcion correcta")
                    curso_selec -= 1
                    print(f"Nombre: {profesor.mis_cursos[curso_selec].nombre}\nContraseña: {profesor.mis_cursos[curso_selec].contrasenia_matriculacion}")

        else:
            print("Opción Inválida. Intente Nuevamente.")

    elif opcion == 3:
        ###if "completar ver cursos"

       # else:
            print("Todavia no hay cursos disponibles en el campus virtual.\n")

    elif opcion == 4:
        break
    else:
        print("Opción inválida.")

    

