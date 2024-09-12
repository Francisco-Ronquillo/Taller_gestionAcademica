from Crud import ICrud
import time
from nota import Nota,NotaDetail
from Estudiante import Student
from Utilidades import limpiarPantalla,gotoxy,dibujarCabeza,Validar,BLUE,RESET,GREEN,RED
from Periodo import Periodo
from Estudiante import Student
from Profesor import Teacher
from Nivel_Educativo import Nivel
from Asignatura import Asignatura
from Estudiante import Student
from clsJson import JsonFile
class menuNota(ICrud):
    def create():
        limpiarPantalla()
        #Cabeza de notas
        dibujarCabeza('UNEMI')
        gotoxy(1,4);print('Periodo: ')
        gotoxy(9,4);id_periodo=input()
        json_file=JsonFile('File/periodo.json')
        periodos=json_file.find('id',id_periodo)
        if not periodos:
            gotoxy(9,4);print(' '*20)
            gotoxy(9,4);print('Periodo no existe')
            time.sleep(2)
            return
        periodo=periodos[0]
        if not periodo['activo']:
            gotoxy(9,4);print(' '*20)
            gotoxy(9,4);print('Periodo no activo')
            time.sleep(2)
            return
        else:
            per=Periodo(periodo['periodo'])
            gotoxy(9,4);print(' '*20)
            gotoxy(9,4);print(per.periodo)
        gotoxy(25,4);print('Nivel: ')
        gotoxy(31,4);id_nivel=input()
        json_file2=JsonFile('File/nivel.json')
        nivels=json_file2.find('id',id_nivel)
        if not nivels:
            gotoxy(31,4);print(' '*20)
            gotoxy(31,4);print('Nivel no existe')
            time.sleep(2)
            return
        nivel=nivels[0]
        if not nivel['activo']:
            gotoxy(31,4);print(' '*20)
            gotoxy(31,4);print('Nivel no activo')
            time.sleep(2)
            return
        else:
            niv=Nivel(nivel['nivel'])
            gotoxy(31,4);print(' '*20)
            gotoxy(31,4);print(niv.nivel)
        gotoxy(45,4);print('Asignatura: ')
        gotoxy(58,4);id_asignatura=input()
        json_file3=JsonFile('File/Asignaturas.json')
        asignaturas=json_file3.find('id',id_asignatura)
        if not asignaturas:
            gotoxy(57,4);print(' '*20)
            gotoxy(57,4);print('Asignatura no existe')
            time.sleep(2)
            return
        asignatura=asignaturas[0]
        if not nivel['activo'] or nivel['id']!=asignatura['nivel']:
            gotoxy(57,4);print(' '*20)
            gotoxy(57,4);print('Asignatura no activa'if nivel['id']==asignatura['nivel'] else 'Asigantura no pertenece a ese nivel') 
            time.sleep(2)
            return
        else:
            asig=Asignatura(asignatura['descripcion'],nivel['id'])
            gotoxy(57,4);print(' '*20)
            gotoxy(57,4);print(asig.descripcion)
        gotoxy(74,4);print('Profesor: ')
        gotoxy(84,4);id_profesor=input()
        json_file4=JsonFile('File/profesor.json')
        profesores=json_file4.find('id',id_profesor)
        if not profesores:
            gotoxy(84,4);print(' '*20)
            gotoxy(84,4);print('Profesor no existe')
            time.sleep(2)
            return
        profesor=profesores[0]
        if not profesor['activo']:
            gotoxy(84,4);print(' '*20)
            gotoxy(84,4);print('Profesor no activa') 
            time.sleep(2)
            return
        else:
            prof=Teacher(profesor['nombre'],profesor['apellido'])
            gotoxy(84,4);print(' '*20)
            gotoxy(84,4);print(prof.fullName())
        while True:
            gotoxy(1,5);print('Estudiante: ')
            gotoxy(14,5);id_estudiante=input()
            json_file5=JsonFile('File/estudiantes.json')
            estudiantes=json_file5.find('id',id_estudiante)
            if not estudiantes:
                gotoxy(14,5);print(' '*20)
                gotoxy(14,5);print('Estudiante no existe')
                time.sleep(2)
                return
            estudiante=estudiantes[0]
            if not estudiante['activo']:
                gotoxy(14,5);print(' '*20)
                gotoxy(14,5);print('Estudiante no activa') 
                time.sleep(2)
                return
            else:
                estu=Student(estudiante['nombre'],estudiante['apellido'])
                gotoxy(14,5);print(' '*20)
                gotoxy(14,5);print(estu.fullName())
            nota=Nota(estu.fullName(),prof.fullName(),asig.descripcion,per.periodo,niv.nivel)
            gotoxy(1,6);print('='*150)
            gotoxy(1,7);print('Nota 1')
            gotoxy(25,7);print('Nota 2')
            gotoxy(45,7);print('Examen')
            gotoxy(65,7);print('Recuperacion')
            gotoxy(85,7);print('Observacion')
            gotoxy(105,7);print('Promedio')
            #Detalle de nota
            nota1=Validar.valida_nota('nota',3,8)
            nota2=Validar.valida_nota('nota',27,8)
            examen=Validar.valida_nota('examen',47,8)
            prom=nota1+nota2+examen
            gotoxy(107,8);print(prom)
            if prom<70 and prom>39:
                remedial=Validar.valida_nota('remedial',67,8)
                prom=(prom+remedial)/2
            else:
                remedial=0
                gotoxy(67,8);print('N/A')
            if prom<70:
                gotoxy(87,8);print('Reprobado')
            else:
                gotoxy(87,8);print('Aprovado')
            gotoxy(107,8);print(prom)
            nota.add_nota(nota1,nota2,examen,remedial)
            while True:
                gotoxy(15,10);print(RED+'Esta seguro de grabar la nota?(s/n)')
                gotoxy(54,10);procesar=input().lower()
                if procesar=='s':
                    gotoxy(15,11);print("Notas Grabada satisfactoriamente"+RESET)
                    json_file6=JsonFile('File/notas.json')
                    notes=json_file6.read()
                    data=nota.getJson()
                    notes.append(data)
                    json_file6.save(notes)
                    break
                    time.sleep(2)
                elif procesar=='n':
                    gotoxy(20,11);print("Notas Cancelada"+RESET)    
                    time.sleep(2) 
                    break
                else:
                    gotoxy(54,10);print(' '*20)
                    gotoxy(54,10);print('Opcion no valida')
                    time.sleep(2)
                    gotoxy(54,10);print(' '*20)
            if procesar=='n':
                break
            while True:
                gotoxy(15,12);opcion=input('Desea seguir calificando?(s/n): ').lower()
                if opcion=='s':
                    gotoxy(1,5);print(' '*40)
                    gotoxy(1,8);print(' '*120)
                    gotoxy(1,12);print(' '*120)
                    gotoxy(1,10);print(' '*120)
                    gotoxy(1,11);print(' '*120)
                    
                    break
                elif opcion=='n':
                    break
                else:
                    gotoxy(54,12);print(' '*20)
                    print('Opcion no valida')
                    gotoxy(54,12);print(' '*20)
            if opcion=='n':
                break
    def update():
        limpiarPantalla()
        #Cabeza de notas
        dibujarCabeza('Actualizar notas')
        id=input(f"{BLUE}Ingrese el id de las notas: {RESET}")
        json_file=JsonFile('File/notas.json')
        notes=json_file.read()
        update_notes=[]
        found=False
        for note in notes:
            if note['id']==id:
                found=True
                print('Estudiante encontrado')
                print(BLUE,'='*120,RESET)
                gotoxy(50,7);print(GREEN,'Datos del estudiante',RESET)
                gotoxy(0,8);print(GREEN+'Nombre: '+BLUE+f"{note['estudiante']}")
                gotoxy(35,8);print(GREEN+'Apellido: '+BLUE+f"{note['profesor']}")
                gotoxy(70,8);print(GREEN+'Nivel: '+BLUE+f"{note['nivel']}")
                gotoxy(95,8);print(GREEN,'Fecha de creacion: ',BLUE,str(note['fecha_creacion']))
                gotoxy(1,9);print(GREEN+'Periodo: '+BLUE+f"{note['periodo']}")
                gotoxy(35,9);print(GREEN+'Asignatura: '+BLUE+f"{note['asignatura']}")
                gotoxy(70,9);print(GREEN+'Promedio: '+BLUE+f"{note['promedio']}")
                gotoxy(95,9);print(GREEN,'Observacion: ',BLUE,str(note['Observacion']))
                print(BLUE,'='*120,RESET)
                gotoxy(1,11);print('Nota 1')
                gotoxy(25,11);print('Nota 2')
                gotoxy(45,11);print('Examen')
                gotoxy(65,11);print('Recuperacion')
                nota1=Validar.valida_nota('nota',3,12)
                nota2=Validar.valida_nota('nota',27,12)
                examen=Validar.valida_nota('examen',47,12)
                prom=nota1+nota2+examen
                gotoxy(80,9);print(prom)
                if prom<70 and prom>39:
                    remedial=Validar.valida_nota('remedial',67,12)
                    prom=(prom+remedial)/2
                else:
                    remedial=0
                    gotoxy(67,12);print('N/A')
                if prom<70:
                    gotoxy(109,9);print(' '*20)
                    gotoxy(109,9);print('Reprobado')
                    obs='Reprobado'
                else:
                    gotoxy(109,9);print(' '*20)
                    gotoxy(109,9);print('Aprobado')
                    obs='Aprobado'
                while True:
                    gotoxy(1,15);option=input('¿Desea actualizar las notas?(s/n): ').lower()
                    if option=='s':
                        note['promedio']=prom
                        note['Observacion']=obs
                        for nota in note['Notas']:
                            nota['nota1']=nota1
                            nota['nota2']=nota2
                            nota['examen']=examen
                            nota['remedial']=remedial
                            
                        break;
                    elif option=='n':
                        break
                    else:
                        print('Opcion no valida')
            update_notes.append(note)
        if found:
            if option=='s':
                gotoxy(1,16);print(f"{GREEN}Actualizado con exito 👍{RESET}")
                json_file.save(update_notes)
            else:
                print(f"❌{RED}Operacion cancelada{RESET}❌")

        else:
            print(f"❌{RED}Estudiante no encontrado{RESET}❌")
        input('Presione una tecla para continuar...')
    def delete():
        limpiarPantalla()
        #Cabeza de notas
        dibujarCabeza('Eliminar notas')
        id=input(f"{BLUE}Ingrese el id del profesor: {RESET}")
        json_file=JsonFile('File/notas.json')
        notes=json_file.read()
        update_notes=[]
        found=False
        for note in notes:
            if note['id'] ==id:
                found=True
                gotoxy(1,6);print('Notas encontradas')
                print(BLUE,'='*120,RESET)
                gotoxy(50,8);print(GREEN,'Datos del profesor',RESET)
                print(GREEN,'Estudiante: ',BLUE,note['estudiante'],RESET)
                print(GREEN,'Profesor: ',BLUE,note['profesor'],RESET)
                print(GREEN,'Asignatura: ',BLUE,str(note['asignatura']))
                print(BLUE,'='*120,RESET)
            
            
        if found:
            while True:
                gotoxy(1,13);decision=input('Esta seguro de eliminar los datos?(s/n): ')
                decision=decision.strip()
                if decision.lower()=='s':
                    for note in notes:
                        if note['id']!=id:
                            update_notes.append(note)
                    gotoxy(50,14);print(f"{GREEN}Datos eliminado  con exito 👍{RESET}")
                    json_file.save(update_notes)
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
            gotoxy(1,5);print(f"❌{RED}Notas no encontradas{RESET}❌")
            time.sleep(2)
        input('Presiona una tecla para continuar')
    def consult():
        limpiarPantalla()
        #Cabeza de notas
        dibujarCabeza('Consultar notas')
        id=input(f"{BLUE}Ingrese el id del profesor: {RESET}")
        json_file=JsonFile('File/notas.json')
        notes=json_file.find('id',id)
        if notes:
            note=notes[0]
            print(BLUE,'='*120,RESET)
            gotoxy(50,6);print('Estos son los datos encontrados')
            print(BLUE,'='*120,RESET)
            gotoxy(0,8);print(GREEN+'Nombre: '+BLUE+f"{note['estudiante']}")
            gotoxy(35,8);print(GREEN+'Apellido: '+BLUE+f"{note['profesor']}")
            gotoxy(70,8);print(GREEN+'Nivel: '+BLUE+f"{note['nivel']}")
            gotoxy(95,8);print(GREEN,'Fecha de creacion: ',BLUE,str(note['fecha_creacion']))
            gotoxy(1,9);print(GREEN+'Periodo: '+BLUE+f"{note['periodo']}")
            gotoxy(35,9);print(GREEN+'Asignatura: '+BLUE+f"{note['asignatura']}")
            gotoxy(70,9);print(GREEN+'Promedio: '+BLUE+f"{note['promedio']}")
            gotoxy(95,9);print(GREEN,'Observacion: ',BLUE,str(note['Observacion']))
            print(BLUE,'='*120,RESET)
            for nota in note['Notas']:
                gotoxy(0,11);print('Nota 1')
                gotoxy(0,12);print(nota['nota1'])
                gotoxy(35,11);print('Nota 2')
                gotoxy(35,12);print(nota['nota2'])
                gotoxy(70,11);print('Examen')
                gotoxy(70,12);print(nota['examen'])
                gotoxy(95,11);print('Remedial')
                gotoxy(95,12);print(nota['remedial'])
                
        else:
            print(f"❌{RED}Notas no encontradas{RESET}❌")
        
        input('Presiona una tecla para continuar')