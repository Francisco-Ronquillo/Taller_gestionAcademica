from Crud import ICrud
import time
from Utilidades import limpiarPantalla,gotoxy,dibujarCabeza,Validar,BLUE,RESET,GREEN,RED
from clsJson import JsonFile
from Nivel_Educativo import Nivel
class menuNivel(ICrud):
    def create():
        limpiarPantalla()
        dibujarCabeza('Registrar nivel educativo')
        descripcion=Validar.letras(f"{BLUE}Ingrese el nombre  del nivel educativo:{RESET}  ",1,5)
        while True:
            gotoxy(1,12);option=input('¿Esta seguro de crear el nivel eduactivo?(s/n): ')
            if option.lower()=='s':
                nivel=Nivel(descripcion)
                json_file=JsonFile('File/nivel.json')
                level=json_file.read()
                level.append(nivel.getJson())
                json_file.save(level)
                gotoxy(50,15);print(f"{GREEN}Nivel creado con exito{RESET}👍 ")
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
        dibujarCabeza('Actualizar Nivel')
        id=input(f"{BLUE}Ingrese el id del nivel educativo: {RESET}")
        json_file=JsonFile('File/nivel.json')
        levels=json_file.read()
        update_level=[]
        found=False
        for level in levels:
            if level['id']==id:
                found=True
                print('Nivel encontrado')
                print(BLUE,'='*120,RESET)
                gotoxy(50,7);print(GREEN,'Datos del nivel',RESET)
                print(GREEN,'Descripcion: ',BLUE,level['nivel'],RESET)
                print(GREEN,'Estado: ',BLUE,str(level['activo']))
                print(BLUE,'='*120,RESET)
                descripcion=Validar.letras(f"{BLUE}Ingrese las descripcion del nivel: {RESET}",1,13)
                while True:
                    gotoxy(1,15);option=input('¿Desea actualizar el estado del nivel?(s/n): ')
                    if option.lower()=='s':
                        level["activo"] = not level["activo"]
                        break
                    elif option.lower()=='n':
                        break
                    else:
                        gotoxy(40,15);print(' '*20)
                        gotoxy(40,15);print('Opcion no valida')
                        time.sleep(2)
                        gotoxy(40,15);print(' '*20)
                level['nivel']=descripcion
            update_level.append(level)
        if found:
            gotoxy(1,16);print(f"{GREEN}Actualizado con exito 👍{RESET}")
            json_file.save(update_level)
        else:
            print(f"❌{RED}Nivel no encontrado{RESET}❌")
        input('Presione una tecla para continuar...')
    def delete():
        limpiarPantalla()
        dibujarCabeza('Eliminar Nivel')
        id=input(f"{BLUE}Ingrese el id del nivel: {RESET}")
        json_file=JsonFile('File/nivel.json')
        levels=json_file.read()
        update_levels=[]
        found=False
        for level in levels:
            if level['id'] ==id:
                found=True
                gotoxy(1,6);print(('Nivel encontrado'))
                print(BLUE,'='*120,RESET)
                gotoxy(50,8);print(GREEN,'Datos del nivel',RESET)
                print(GREEN,'Descripcion: ',BLUE,level['nivel'],RESET)
                print(GREEN,'Estado: ',BLUE,str(level['activo']))
                print(BLUE,'='*120,RESET)
            
            
        if found:
            while True:
                gotoxy(1,13);decision=input('Esta seguro de eliminar los datos?(s/n): ')
                decision=decision.strip()
                if decision.lower()=='s':
                    for level in levels:
                        if level['id']!=id:
                            update_levels.append(level)
                    gotoxy(50,14);print(f"{GREEN}Datos eliminado  con exito 👍{RESET}")
                    json_file.save(update_levels)
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
            gotoxy(1,5);print(f"❌{RED}Nivel no encontrado{RESET}❌")
            time.sleep(2)
        input('Presiona una tecla para continuar')
    def consult():
        limpiarPantalla()
        dibujarCabeza('Consultar Nivel')
        id=input(f"{BLUE}Ingrese el id del nivel educativo: {RESET}")
        json_file=JsonFile('File/nivel.json')
        level_buscando=json_file.find('id',id)
        if level_buscando:
            level=level_buscando[0]
            print(BLUE,'='*120,RESET)
            gotoxy(50,6);print('Estos son los datos encontrados')
            print(BLUE,'='*120,RESET)
            print(GREEN+'Descripcion: '+BLUE+f"{level['nivel']}")
            print(GREEN+'Estado: '+BLUE+f"{level['activo']}")
            print(GREEN,'Fecha de creacion: ',BLUE,str(level['fecha_creacion']))
            print ( RESET)
        else:
            print(f"❌{RED}Nivel no encontrado{RESET}❌")
        input(BLUE+ "Presione una tecla para continuar...")