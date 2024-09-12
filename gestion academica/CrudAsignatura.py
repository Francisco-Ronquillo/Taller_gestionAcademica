from Crud import ICrud
import time
from Asignatura import Asignatura
from Utilidades import limpiarPantalla,gotoxy,dibujarCabeza,Validar,BLUE,RESET,GREEN,RED
from clsJson import JsonFile

class menuAsignatura(ICrud):
    def create():
        limpiarPantalla()
        dibujarCabeza('Registrar Asignatura')
        descripcion=Validar.letras(f"{BLUE}Ingrese el nombre de la asignatura:{RESET}  ",1,5)
        nivel=Validar.nivel(f"{BLUE}Ingrese el id del nivel:{RESET}  ",1,6)
        while True:
            gotoxy(1,12);option=input('¿Esta seguro de crear la Asignatura?(s/n): ')
            if option.lower()=='s':
                asignatura=Asignatura(descripcion,nivel)
                json_file=JsonFile('File/Asignaturas.json')
                subject=json_file.read()
                subject.append(asignatura.getJson())
                json_file.save(subject)
                gotoxy(50,15);print(f"{GREEN}Asignatura creado con exito{RESET}👍 ")
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
        dibujarCabeza('Actualizar Asignatura')
        id=input(f"{BLUE}Ingrese el id del Asignatura: {RESET}")
        json_file=JsonFile('File/Asignaturas.json')
        json_file2=JsonFile('File/nivel.json')
        subjects=json_file.read()
        levels=json_file2.read()
        update_subjects=[]
        found=False
        for subject in subjects:
            if subject['id']==id:
                for level in levels:
                    if subject['nivel']== level['id']:
                        descripcion_level=level['nivel']
                found=True
                print('Asignatura encontrado')
                print(BLUE,'='*120,RESET)
                gotoxy(50,7);print(GREEN,'Datos del Asignatura',RESET)
                print(GREEN,'Descripcion: ',BLUE,subject['descripcion'],RESET)
                print(GREEN,'Nivel: ',BLUE,descripcion_level,RESET)
                print(GREEN,'Estado: ',BLUE,str(subject['activo']))
                print(BLUE,'='*120,RESET)
                nombre=Validar.letras(f"{BLUE}Ingrese el nuevo nombre del Asignatura: {RESET}",1,13)
                Nivel=Validar.nivel(f"{BLUE}Ingrese el nuevo id nivel: {RESET}",1,14)
                while True:
                    gotoxy(1,15);option=input('¿Desea actualizar el estado del Asignatura?(s/n): ')
                    if option.lower()=='s':
                        subject["activo"] = not subject["activo"]
                        break
                    elif option.lower()=='n':
                        break
                    else:
                        gotoxy(50,15);print(' '*20)
                        gotoxy(50,15);print('Opcion no valida')
                        time.sleep(2)
                        gotoxy(50,15);print(' '*20)
                subject['descripcion']=nombre
                subject['nivel']=Nivel
            update_subjects.append(subject)
        if found:
            gotoxy(1,16);print(f"{GREEN}Actualizado con exito 👍{RESET}")
            json_file.save(update_subjects)
        else:
            print(f"❌{RED}Asignatura no encontrado{RESET}❌")
        input('Presione una tecla para continuar...')
    def delete():
        limpiarPantalla()
        dibujarCabeza('Eliminar Asignatura')
        id=input(f"{BLUE}Ingrese el id del Asignatura: {RESET}")
        json_file=JsonFile('File/Asignaturas.json')
        json_file2=JsonFile('File/nivel.json')
        subjects=json_file.read()
        levels=json_file2.read()
        update_subjects=[]
        found=False
        for subject in subjects:
            if subject['id'] ==id:
                for level in levels:
                    if subject['nivel']== level['id']:
                        descripcion_level=level['nivel']
                found=True
                gotoxy(1,6);print(('Asignatura encontrado'))
                print(BLUE,'='*120,RESET)
                gotoxy(50,8);print(GREEN,'Datos del Asignatura',RESET)
                print(GREEN,'Descripcion: ',BLUE,subject['descripcion'],RESET)
                print(GREEN,'Nivel: ',BLUE,subject['nivel'],RESET)
                print(GREEN,'Nivel: ',BLUE,descripcion_level,RESET)
                print(GREEN,'Estado: ',BLUE,str(subject['activo']))
                print(BLUE,'='*120,RESET)
            
            
        if found:
            while True:
                gotoxy(1,13);decision=input('Esta seguro de eliminar los datos?(s/n): ')
                if decision.lower()=='s':
                    for subject in subjects:
                        if subject['id']!=id:
                            update_subjects.append(subject)
                    gotoxy(50,14);print(f"{GREEN}Datos eliminado  con exito 👍{RESET}")
                    json_file.save(update_subjects)
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
            gotoxy(1,5);print(f"❌{RED}Asignatura no encontrado{RESET}❌")
            time.sleep(2)
        input('Presiona una tecla para continuar')
    def consult():
        limpiarPantalla()
        dibujarCabeza('Consultar Asignatura')
        id=input(f"{BLUE}Ingrese el id del Asignatura: {RESET}")
        json_file=JsonFile('File/Asignaturas.json')
        json_file2=JsonFile('File/nivel.json')
        subject_buscando=json_file.find('id',id)
        levels=json_file2.read()
        if subject_buscando:
            for level in levels:
                    if subject_buscando['nivel']== level['id']:
                        descripcion_level=level['nivel']
            subject=subject_buscando[0]
            print(BLUE,'='*120,RESET)
            gotoxy(50,6);print('Estos son los datos encontrados')
            print(BLUE,'='*120,RESET)
            print(GREEN+'Descripcion: '+BLUE+f"{subject['descripcion']}")
            print(GREEN,'Nivel: ',BLUE,descripcion_level,RESET)
            print(GREEN+'Estado: '+BLUE+f"{subject['activo']}")
            print(GREEN,'Fecha de creacion: ',BLUE,str(subject['fecha_creacion']))
            print ( RESET)
        else:
            print(f"❌{RED}Asignatura no encontrado{RESET}❌")
        input(BLUE+ "Presione una tecla para continuar...")
