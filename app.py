from clases import *
from Curso import *


while True:
    indice = 0
    print("1- Ingresar Alumno.")
    print("2- Ingresar Profesor.")
    print("3- Ver cursos.")
    print("4- Salir.")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        mail = input("Ingrese su Email: ")
        contra = input("Ingrese la contraseña: ")
        for alumn in alumnos:
            indice +=1
            bandera = alumn.validar_credenciales(mail, contra)

            if bandera:
                break

        if bandera:
            indice -= 1
            opcion_Dos = 0
            print("Alumno inicio sesion correctamente!")
            while opcion_Dos !=3 :
                print("1- Matricularse a un curso.")
                print("2- Ver cursos.")
                print("3- Volver al menú principal.")
                
                opcion_Dos = int(input("Ingrese una opción: "))

                if opcion_Dos == 1:
                    i = 0
                    
                    if cursos_totales:
                        for curso in cursos_totales:
                            i += 1
                            print(f"{i} {curso.nombre}")

                    banderaWh = False
                    while not banderaWh:
                        curso_selec = int(input("Ingrese el numero del curso del cual desea matricularse: "))
                        if curso_selec <= i and curso_selec > 0:
                            banderaWh = True
                        else:
                            print("Ingrese una opcion correcta")
                    curso_selec -= 1
                    if not cursos_totales[curso_selec] in alumnos[indice].mis_cursos:
                        clave_curso = input("Ingrese la contraseña de dicho curso: ")
                        alumno.matricularse_en_curso(clave_curso, indice, curso_selec)
                    else:
                        print("Ya se encuentra matriculado a ese curso.")

                elif opcion_Dos == 2:
                    
                    i = 0
                    print("Cursos del alumno:")
                    for curso in alumnos[indice].mis_cursos:
                        i += 1
                        print(f"{i} {curso.nombre}")
                #no esta la parte de pedir la opcion, sentimos que no tiene sentido mostrar la lista con los nombres para dsp volverle a decir el nombre
                else:
                    print("seleccione una opcion valida")
        
        else:
            print("Email de alumno inexsistente. Debe darse de alta en alumnado.")

    elif opcion == 2:
        mail = input("Ingrese su Email: ")
        contra = input("Ingrese la contraseña: ")
        for prof in profesores:
            indice +=1
            bandera = prof.validar_credenciales(mail, contra)

            if bandera:
                break

        if bandera:
            indice -= 1
            opcion_Dos = 0
            print("Profesor inicio sesion correctamente!")
            while opcion_Dos !=3:
                print("1- Dictar curso.")
                print("2- Ver cursos.")
                print("3- Volver al menú principal.")

                opcion_Dos = int(input("Ingrese una opción: "))
                
                if opcion_Dos == 1:
                    curso = Curso(str(input("Ingrese el nombre del nuevo curso: ")))
                    cursos_totales.append(curso)
                    profesores[indice].mis_cursos.append(curso)
                    print(f"Nombre: {curso.nombre} \nContraseña: {curso.contrasenia_matriculacion}")
                elif opcion_Dos == 2:
                    i = 0

                    for curso in profesores[indice].mis_cursos:
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
                    print(f"Nombre: {profesores[indice].mis_cursos[curso_selec].nombre}\nContraseña: {profesores[indice].mis_cursos[curso_selec].contrasenia_matriculacion}")

        else:
            print("Email de profesor inexsistente. Debe darse de alta en alumnado.")

    elif opcion == 3:
        cursos_ordenados = []
        if cursos_totales:
            for cursos in cursos_totales:
                cursos_ordenados.append(cursos.nombre)
            
            cursos_ordenados = sorted(cursos_ordenados)

            for cursos in cursos_ordenados:
                print(f"Materia: {cursos} Carrera: Tecnicatura Universitaria en Programación")

        else:
            print("Aun no hay cursos ingresados")

    elif opcion == 4:
        break
    else:
        print("Opción inválida.")

    

