from Crud import ICrud
from datetime import datetime
import  time
from Utilidades import limpiarPantalla,gotoxy,dibujarCabeza,Validar,BLUE,RESET,GREEN,RED
from clsJson import JsonFile
from tesis import Detalle_tesis,Tema_tesis
from Profesor import Teacher
from Estudiante import Student
class menuTesis(ICrud):
    def create():
        limpiarPantalla()
        #Cabeza de tesis
        dibujarCabeza('UNEMI')
        gotoxy(1,4);print('Tema: ')
        gotoxy(9,4);tema=Validar.letras('',9,4)
        gotoxy(25,4);print('Tutor: ')
        gotoxy(31,4);id_profesor=input()
        json_file4=JsonFile('File/profesor.json')
        profesores=json_file4.find('id',id_profesor)
        if not profesores:
            gotoxy(31,4);print(' '*20)
            gotoxy(31,4);print('Profesor no existe')
            time.sleep(2)
            return
        profesor=profesores[0]
        if not profesor['activo']:
            gotoxy(31,4);print(' '*20)
            gotoxy(31,4);print('Profesor no activo') 
            time.sleep(2)
            return
        else:
            prof=Teacher(profesor['nombre'],profesor['apellido'])
            gotoxy(31,4);print(' '*20)
            gotoxy(31,4);print(prof.fullName())
        gotoxy(74,4);print('Fecha de sustentacion: ')
        fecha_sustentacion=datetime.now().strftime("%d-%b-%Y")
        gotoxy(95,4);print(fecha_sustentacion)
        tesis=Tema_tesis(tema,prof.fullName(),fecha_sustentacion)
        #Detalle de tesis
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
            gotoxy(1,6);print('='*150)
            gotoxy(1,7);print('Nota')
            gotoxy(85,7);print('Observacion')
            nota=Validar.valida_nota('remedial',3,8)
            if nota<70:
                gotoxy(87,8);print('Reprobado')
            else:
                gotoxy(87,8);print('Aprovado')
            tesis.addDetalleTesis(estu.fullName(),nota)
            while True:
                gotoxy(1,10);print('Desea agregar otro estudiante a la tesis?(s/n)')
                gotoxy(80,10);option=input()
                if option=='s':
                    break
                elif option=='n':
                    break
                else:
                    print('opcion no valida')
            if option=='n':
                break
        gotoxy(15,11);print("Tesis Grabada satisfactoriamente"+RESET)
        json_file6=JsonFile('File/tesis.json')
        tesi=json_file6.read()
        tesi=tesis.getJson()
        json_file6.save(tesi)
    def update():
        pass
    def delete():
        pass
    def consult():
        pass