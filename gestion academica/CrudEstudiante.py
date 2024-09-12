from Crud import ICrud
import time
from Estudiante import Student
from Utilidades import limpiarPantalla,gotoxy,dibujarCabeza,Validar,BLUE,RESET,GREEN,RED
from clsJson import JsonFile

class menuEstudiante(ICrud):
    def create():
        limpiarPantalla()
        dibujarCabeza('Registrar Estudiante')
        nombre=Validar.letras(f"{BLUE}Ingrese el nombre del estudiante:{RESET}  ",1,5)
        apellido=Validar.letras(f"{BLUE}Ingrese el apellido del estudiante:{RESET} ",1,6)
        while True:
            gotoxy(1,12);option=input('¿Esta seguro de crear el estudiante?(s/n): ')
            if option.lower()=='s':
                estudiante=Student(nombre,apellido)
                json_file=JsonFile('File/estudiantes.json')
                student=json_file.read()
                student.append(estudiante.getJson())
                json_file.save(student)
                gotoxy(50,15);print(f"{GREEN}Estudiante creado con exito{RESET}👍 ")
                break
            if option.lower()=='n':
                gotoxy(50,15);print(f"❌{RED}Operacion cancelada{RESET}❌")
                break
            else:
                gotoxy(50,15);print(' '*20)
                gotoxy(50,15);print('Opcion no valida')
                time.sleep(2)
                gotoxy(50,15);print(' '*20)
        input('Presiona una tecla para continuar....')

    def update():
        limpiarPantalla()
        dibujarCabeza('Actualizar Estudiante')
        id=input(f"{BLUE}Ingrese el id del estudiante: {RESET}")
        json_file=JsonFile('File/estudiantes.json')
        students=json_file.read()
        update_students=[]
        found=False
        for student in students:
            if student['id']==id:
                found=True
                print('Estudiante encontrado')
                print(BLUE,'='*120,RESET)
                gotoxy(50,7);print(GREEN,'Datos del estudiante',RESET)
                print(GREEN,'Nombre: ',BLUE,student['nombre'],RESET)
                print(GREEN,'Apellido: ',BLUE,student['apellido'],RESET)
                print(GREEN,'Estado: ',BLUE,str(student['activo']))
                print(BLUE,'='*120,RESET)
                nombre=Validar.letras(f"{BLUE}Ingrese el nuevo nombre del estudiante: {RESET}",1,13)
                apellido=Validar.letras(f"{BLUE}Ingrese el nuevo apellido del estudiante: {RESET}",1,14)
                while True:
                    gotoxy(1,15);option=input('¿Desea actualizar el estado del estudiante?(s/n): ')
                    if option.lower()=='s':
                        student["activo"] = not student["activo"]
                        break
                    elif option.lower()=='n':
                        break
                    else:
                        gotoxy(50,15);print(' '*20)
                        gotoxy(50,15);print('Opcion no valida')
                        time.sleep(2)
                        gotoxy(50,15);print(' '*20)
                student['nombre']=nombre
                student['apellido']=apellido
            update_students.append(student)
        if found:
            gotoxy(1,16);print(f"{GREEN}Actualizado con exito 👍{RESET}")
            json_file.save(update_students)
        else:
            print(f"❌{RED}Estudiante no encontrado{RESET}❌")
        input('Presione una tecla para continuar...')
    def delete():
        limpiarPantalla()
        dibujarCabeza('Eliminar Estudiante')
        id=input(f"{BLUE}Ingrese el id del estudiante: {RESET}")
        json_file=JsonFile('File/estudiantes.json')
        students=json_file.read()
        update_students=[]
        found=False
        for student in students:
            if student['id'] ==id:
                found=True
                gotoxy(1,6);print(('Estudiante encontrado'))
                print(BLUE,'='*120,RESET)
                gotoxy(50,8);print(GREEN,'Datos del estudiante',RESET)
                print(GREEN,'Nombre: ',BLUE,student['nombre'],RESET)
                print(GREEN,'Apellido: ',BLUE,student['apellido'],RESET)
                print(GREEN,'Estado: ',BLUE,str(student['activo']))
                print(BLUE,'='*120,RESET)
            
            
        if found:
            while True:
                gotoxy(1,13);decision=input('Esta seguro de eliminar los datos?(s/n): ')
                if decision.lower()=='s':
                    for student in students:
                        if student['id']!=id:
                            update_students.append(student)
                    gotoxy(50,14);print(f"{GREEN}Datos eliminado  con exito 👍{RESET}")
                    json_file.save(update_students)
                    break
                elif decision.lower()=='n':
                    print('Operacion cancelada')
                    break
                else:
                    gotoxy(40,13);print(' '*20)
                    gotoxy(40,13);print('Opcion no valida')
                    gotoxy(40,13);print(' '*20)
                    time.sleep(2)
        else:
            gotoxy(1,5);print(f"❌{RED}Estudiante no encontrado{RESET}❌")
            time.sleep(2)
        input('Presiona una tecla para continuar')
    def consult():
        limpiarPantalla()
        dibujarCabeza('Consultar Estudiante')
        id=input(f"{BLUE}Ingrese el id del estudiante: {RESET}")
        json_file=JsonFile('File/estudiantes.json')
        student_buscando=json_file.find('id',id)
        if student_buscando:
            student=student_buscando[0]
            print(BLUE,'='*120,RESET)
            gotoxy(50,6);print('Estos son los datos encontrados')
            print(BLUE,'='*120,RESET)
            print(GREEN+'Nombre: '+BLUE+f"{student['nombre']}")
            print(GREEN+'Apellido: '+BLUE+f"{student['apellido']}")
            print(GREEN+'Estado: '+BLUE+f"{student['activo']}")
            print(GREEN,'Fecha de creacion: ',BLUE,str(student['fecha_creacion']))
            print ( RESET)
        else:
            print(f"❌{RED}Estudiante no encontrado{RESET}❌")
        input(BLUE+ "Presione una tecla para continuar...")

