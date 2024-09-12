from Crud import ICrud
import time
from Periodo import Periodo
from Utilidades import limpiarPantalla,gotoxy,dibujarCabeza,Validar,BLUE,RESET,GREEN,RED
from clsJson import JsonFile
class menuPeriodo(ICrud):
    def create():
        limpiarPantalla()
        dibujarCabeza('Registrar periodo')
        descripcion=Validar.formato_periodo(f"{BLUE}Ingrese el nombre  del periodo:{RESET}  ",1,5)
        while True:
            gotoxy(1,12);option=input('¿Esta seguro de crear el periodo?(s/n): ')
            if option.lower()=='s':
                periodo=Periodo(descripcion)
                json_file=JsonFile('File/periodo.json')
                periodos=json_file.read()
                periodos.append(periodo.getJson())
                json_file.save(periodos)
                gotoxy(50,15);print(f"{GREEN}Periodo creado con exito{RESET}👍 ")
                break
            if option.lower()=='n':
                gotoxy(50,15);print(f"❌{RED}Operacion cancelada{RESET}❌")
                break
            else:
                gotoxy(40,12);print(' '*20)
                gotoxy(40,12);print('Opcion no valida')
                time.sleep(2)
                gotoxy(40,12);print(' '*20)
        input('Presiona una tecla para continuar....')
    def update():
        limpiarPantalla()
        dibujarCabeza('Actualizar periodo')
        id=input(f"{BLUE}Ingrese el id del periodo: {RESET}")
        json_file=JsonFile('File/periodo.json')
        periodos=json_file.read()
        update_periodo=[]
        found=False
        for periodo in periodos:
            if periodo['id']==id:
                found=True
                print('Periodo encontrado')
                print(BLUE,'='*120,RESET)
                gotoxy(50,7);print(GREEN,'Datos del periodo',RESET)
                print(GREEN,'Descripcion: ',BLUE,periodo['periodo'],RESET)
                print(GREEN,'Estado: ',BLUE,str(periodo['activo']))
                print(BLUE,'='*120,RESET)
                descripcion=Validar.formato_periodo(f"{BLUE}Ingrese las descripcion del periodo: {RESET}",1,13)
                while True:
                    gotoxy(1,15);option=input('¿Desea actualizar el estado del periodo?(s/n): ')
                    if option.lower()=='s':
                        periodo["activo"] = not periodo["activo"]
                        break
                    elif option.lower()=='n':
                        break
                    else:
                        gotoxy(40,15);print(' '*20)
                        gotoxy(40,15);print('Opcion no valida')
                        time.sleep(2)
                        gotoxy(40,15);print(' '*20)
                periodo['periodo']=descripcion
            update_periodo.append(periodo)
        if found:
            gotoxy(1,16);print(f"{GREEN}Actualizado con exito 👍{RESET}")
            json_file.save(update_periodo)
        else:
            print(f"❌{RED}Periodo no encontrado{RESET}❌")
        input('Presione una tecla para continuar...')
    def delete():
        limpiarPantalla()
        dibujarCabeza('Eliminar periodo')
        id=input(f"{BLUE}Ingrese el id del periodo: {RESET}")
        json_file=JsonFile('File/periodo.json')
        periodos=json_file.read()
        update_periodos=[]
        found=False
        for periodo in periodos:
            if periodo['id'] ==id:
                found=True
                gotoxy(1,6);print(('Periodo encontrado'))
                print(BLUE,'='*120,RESET)
                gotoxy(50,8);print(GREEN,'Datos del periodo',RESET)
                print(GREEN,'Descripcion: ',BLUE,periodo['periodo'],RESET)
                print(GREEN,'Estado: ',BLUE,str(periodo['activo']))
                print(GREEN,'Fecha de creacion: ',BLUE,str(periodo['fecha_creacion']))
                print(BLUE,'='*120,RESET)
            
            
        if found:
            while True:
                gotoxy(1,13);decision=input('Esta seguro de eliminar los datos?(s/n): ')
                decision=decision.strip()
                if decision.lower()=='s':
                    for periodo in periodos:
                        if periodo['id']!=id:
                            update_periodos.append(periodo)
                    gotoxy(50,14);print(f"{GREEN}Datos eliminado  con exito 👍{RESET}")
                    json_file.save(update_periodos)
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
            gotoxy(1,5);print(f"❌{RED}periodo no encontrado{RESET}❌")
            time.sleep(2)
        input('Presiona una tecla para continuar')
    def consult():
        limpiarPantalla()
        dibujarCabeza('Consultar periodo')
        id=input(f"{BLUE}Ingrese el id del periodo: {RESET}")
        json_file=JsonFile('File/periodo.json')
        periodo_buscando=json_file.find('id',id)
        if periodo_buscando:
            periodo=periodo_buscando[0]
            print(BLUE,'='*120,RESET)
            gotoxy(50,6);print('Estos son los datos encontrados')
            print(BLUE,'='*120,RESET)
            print(GREEN+'Descripcion: '+BLUE+f"{periodo['periodo']}")
            print(GREEN+'Estado: '+BLUE+f"{periodo['activo']}")
            print(GREEN,'Fecha de creacion: ',BLUE,str(periodo['fecha_creacion']))
            print (RESET)
        else:
            print(f"❌{RED}Periodo no encontrado{RESET}❌")
        input(BLUE+ "Presione una tecla para continuar...")