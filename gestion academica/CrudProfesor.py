from Crud import ICrud
import time
from Profesor import Teacher
from Utilidades import limpiarPantalla,gotoxy,dibujarCabeza,Validar,BLUE,RESET,GREEN,RED
from clsJson import JsonFile

class menuProfesor(ICrud):
    def create():
        limpiarPantalla()
        dibujarCabeza('Registrar Profesor')
        nombre=Validar.letras(f"{BLUE}Ingrese el nombre del Profesor:{RESET}  ",1,5)
        apellido=Validar.letras(f"{BLUE}Ingrese el apellido del Profesor:{RESET} ",1,6)
        while True:
            gotoxy(1,12);option=input('¿Esta seguro de crear el profesor?(s/n): ')
            option=option.strip()
            if option.lower()=='s':
                profesor=Teacher(nombre,apellido)
                json_file=JsonFile('File/profesor.json')
                teacher=json_file.read()
                teacher.append(profesor.getJson())
                json_file.save(teacher)
                gotoxy(50,15);print(f"{GREEN}Profesor creado con exito{RESET}👍 ")
                break
            if option.lower()=='n':
                gotoxy(50,15);print(f"❌{RED}Operacion cancelada{RESET}❌")
                break
            else:
                gotoxy(45,12);print(' '*20)
                gotoxy(45,12);print('Opcion no valida')
                time.sleep(2)
                gotoxy(45,12);print(' '*20)
        input('Presiona una tecla para continuar....')
    def update():
        limpiarPantalla()
        dibujarCabeza('Actualizar Profesor')
        id=input(f"{BLUE}Ingrese el id del profesor: {RESET}")
        json_file=JsonFile('File/profesor.json')
        teachers=json_file.read()
        update_teacher=[]
        found=False
        for teacher in teachers:
            if teacher['id']==id:
                found=True
                print('Profesor encontrado')
                print(BLUE,'='*120,RESET)
                gotoxy(50,7);print(GREEN,'Datos del Profesor',RESET)
                print(GREEN,'Nombre: ',BLUE,teacher['nombre'],RESET)
                print(GREEN,'Apellido: ',BLUE,teacher['apellido'],RESET)
                print(GREEN,'Estado: ',BLUE,str(teacher['activo']))
                print(BLUE,'='*120,RESET)
                nombre=Validar.letras(f"{BLUE}Ingrese el nuevo nombre del profesor: {RESET}",1,13)
                apellido=Validar.letras(f"{BLUE}Ingrese el nuevo apellido del profesor: {RESET}",1,14)
                while True:
                    gotoxy(1,15);option=input('¿Desea actualizar el estado del profesor?(s/n): ')
                    option=option.strip()
                    if option.lower()=='s':
                        teacher["activo"] = not teacher["activo"]
                        break
                    elif option.lower()=='n':
                        break
                    else:
                        gotoxy(48,15);print(' '*20)
                        gotoxy(48,15);print('Opcion no valida')
                        time.sleep(2)
                        gotoxy(48,15);print(' '*20)
                teacher['nombre']=nombre
                teacher['apellido']=apellido
            update_teacher.append(teacher)
        if found:
            gotoxy(1,16);print(f"{GREEN}Actualizado con exito 👍{RESET}")
            json_file.save(update_teacher)
        else:
            print(f"❌{RED}Profesor no encontrado{RESET}❌")
        input('Presione una tecla para continuar...')
    def delete():
        limpiarPantalla()
        dibujarCabeza('Eliminar Profesor')
        id=input(f"{BLUE}Ingrese el id del profesor: {RESET}")
        json_file=JsonFile('File/profesor.json')
        teachers=json_file.read()
        update_teachers=[]
        found=False
        for teacher in teachers:
            if teacher['id'] ==id:
                found=True
                gotoxy(1,6);print(('Profesor encontrado'))
                print(BLUE,'='*120,RESET)
                gotoxy(50,8);print(GREEN,'Datos del profesor',RESET)
                print(GREEN,'Nombre: ',BLUE,teacher['nombre'],RESET)
                print(GREEN,'Apellido: ',BLUE,teacher['apellido'],RESET)
                print(GREEN,'Estado: ',BLUE,str(teacher['activo']))
                print(BLUE,'='*120,RESET)
            
            
        if found:
            while True:
                gotoxy(1,13);decision=input('Esta seguro de eliminar los datos?(s/n): ')
                decision=decision.strip()
                if decision.lower()=='s':
                    for teacher in teachers:
                        if teacher['id']!=id:
                            update_teachers.append(teacher)
                    gotoxy(50,14);print(f"{GREEN}Datos eliminado  con exito 👍{RESET}")
                    json_file.save(update_teachers)
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
            gotoxy(1,5);print(f"❌{RED}Profesor no encontrado{RESET}❌")
            time.sleep(2)
        input('Presiona una tecla para continuar')
    def consult():
        limpiarPantalla()
        dibujarCabeza('Consultar Profesor')
        id=input(f"{BLUE}Ingrese el id del profesor: {RESET}")
        json_file=JsonFile('File/profesor.json')
        teacher_buscando=json_file.find('id',id)
        if teacher_buscando:
            teacher=teacher_buscando[0]
            print(BLUE,'='*120,RESET)
            gotoxy(50,6);print('Estos son los datos encontrados')
            print(BLUE,'='*120,RESET)
            print(GREEN+'Nombre: '+BLUE+f"{teacher['nombre']}")
            print(GREEN+'Apellido: '+BLUE+f"{teacher['apellido']}")
            print(GREEN+'Estado: '+BLUE+f"{teacher['activo']}")
            print(GREEN,'Fecha de creacion: ',BLUE,str(teacher['fecha_creacion']))
            print ( RESET)
        else:
            print(f"❌{RED}Profesor no encontrado{RESET}❌")
        input(BLUE+ "Presione una tecla para continuar...")