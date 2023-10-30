from Profesor import *
from Curso import *
from Estudiante import *


while True:
    indice = 0
    print("1- Ingresar Alumno.")
    print("2- Ingresar Profesor.")
    print("3- Ver cursos.")
    print("4- Salir.")

    opcion = int(input("Ingrese una opción: "))

    #Ingresar como alumno
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
            #Menu alumno
            while opcion_Dos !=4 :
                print("1- Matricularse a un curso.")
                print("2- Desmatricularse de un curso")
                print("3- Ver cursos.")
                print("4- Volver al menú principal.")
                
                opcion_Dos = int(input("Ingrese una opción: "))

                if opcion_Dos == 1:
                    i = 0
                    
                    if alumnos[indice].carrera.cursos:
                        cursos_ordenados = []
                        cursos_ordenados = sorted(alumnos[indice].carrera.cursos, key=lambda codigo: codigo.codigo)

                        for curso in alumnos[indice].carrera.cursos:
                            i += 1
                            print(f"{i} {curso.nombre}")

                    """Enunciado: Además se valida que el alumno pertenezca a la carrera a la que dicho...
                    Comentario:Creemos que no hace falta validarlo ya que al tomarlo de alumno es obvio que ya pertenece a la carrera"""

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
                    if alumnos[indice].mis_cursos:
                        i = 0
                        for curso in alumnos[indice].mis_cursos:
                            i += 1
                            print(f"{i} {curso.nombre}")
                        banderaWh = False
                        while not banderaWh:
                            curso_selec = int(input("Ingrese el numero del curso del cual desea desmatricularse: "))
                            if curso_selec <= i and curso_selec > 0:
                                banderaWh = True
                            else:
                                print("Ingrese una opcion correcta")
                        curso_selec -= 1
                        alumno.desmatricularse_de_curso(indice, curso_selec)
                    else:
                        print("Aun no esta matriculado a ningun curso.")

                elif opcion_Dos == 3:
                    if alumnos[indice].mis_cursos:
                        i = 0
                        print("Cursos del alumno:")
                        for curso in alumnos[indice].mis_cursos:
                            i += 1
                            print(f"{i} {curso.nombre}")
                        for archivo in curso.archivos:
                            print(f"{archivo.nombre}.{archivo.formato}")
                    else:
                        print("Aun no posee cursos.")

                elif opcion_Dos == 4:
                    print("Regresando al menu principal...")
                else:
                    print("seleccione una opcion valida")
        
        else:
            print("Email de alumno inexsistente. Debe darse de alta en alumnado.")

    #Ingresar como profesor
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
            #Menu profesor
            while opcion_Dos !=3:
                print("1- Dictar curso.")
                print("2- Ver cursos.")
                print("3- Volver al menú principal.")

                opcion_Dos = int(input("Ingrese una opción: "))
                
                if opcion_Dos == 1:
                    i = 0
                    for carrera in carreras_totales:
                        i += 1
                        print(f"{i} {carrera.nombre}")
                    carrera_selec = int(input("Seleccione la carrera en la cual desea dictar el curso: "))
                    carrera_selec -= 1
                    curso = Curso(str(input("Ingrese el nombre del nuevo curso: ")), carreras_totales[carrera_selec])
                    carreras_totales[carrera_selec].agr_curso(curso)
                    cursos_totales.append(curso)
                    profesores[indice].mis_cursos.append(curso)
                    print(f"Nombre: {curso.nombre}\nCodigo: {curso.codigo}\nContraseña: {curso.contrasenia_matriculacion}")
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
                    print(f"Nombre: {profesores[indice].mis_cursos[curso_selec].nombre}\nCodigo: {profesores[indice].mis_cursos[curso_selec].codigo}\nContraseña: {profesores[indice].mis_cursos[curso_selec].contrasenia_matriculacion}\nCantidad de archivos: {len(profesores[indice].mis_cursos[curso_selec].archivos)}")
                    opc = input("Desea adjuntar un archivo? (Ingrese S/N): ")
                    if opc == "S":
                        nombre_archivo = input("Ingrese el nombre del archivo: ")
                        formato_archivo = input("Ingrese el formato del archivo: ")
                        archivo_creado = Archivo(nombre_archivo, formato_archivo)
                        profesores[indice].mis_cursos[curso_selec].archivos.append(archivo_creado)

        else:
            print("Email de profesor inexsistente. Debe darse de alta en alumnado.")

    #Mostrar cursos
    elif opcion == 3:
        cursos_ordenados = []
        if cursos_totales:
            cursos_ordenados = sorted(cursos_totales, key=lambda nombres: nombres.nombre)
        
            for cursos in cursos_ordenados:
                print(f"Materia: {cursos.nombre} Carrera: {cursos.carrera.nombre}")

        else:
            print("Aun no hay cursos ingresados")

    elif opcion == 4:
        break
    else:
        print("Opción inválida.")

    

