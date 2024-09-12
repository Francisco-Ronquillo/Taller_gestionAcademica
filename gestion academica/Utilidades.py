import os
import re
import time
from clsJson import JsonFile
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m" 
class Utilidades():
    def __init__(self,title="",option=[]):
        self.title=title
        self.option=option

    def menu(self):
        fila=0
        gotoxy(50,5);print(self.title)
        for option in self.option:
            fila+=1
            gotoxy(50,5+fila);print(f"{fila}){option}")
        gotoxy(50,6+fila);option=input('Escoja una opcion 1...'+str(fila)+': ' )
        return option
def dibujarCabeza(title=''):
        limpiarPantalla()
        print(GREEN,'='*150,RESET)
        gotoxy(70,2)
        print(BLUE,title,RESET)
        print(GREEN,'='*150,RESET)
        
def limpiarPantalla():
        os.system("cls")
def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")
class Validar():
    def letras(text,fila,columna):
        while True:
            gotoxy(fila,columna);cadena=input(text)
            if cadena.replace(" ", "").isalpha() and not re.search(r"[^a-zA-Z0-9 ]", cadena):
                return cadena
            else:
                gotoxy(fila+len(text),columna);print(' '*20)
                gotoxy(fila+len(text),columna);print('Solo letras')
                time.sleep(2)
                gotoxy(fila+len(text),columna);print(' '*20)

    def Dni(text,fila,columna):
        while True:
            gotoxy(fila,columna);cedula=input(text)
            if len(cedula)==10 and cedula.isdigit:
                coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
                suma = 0
                
                for i in range(9):
                    digito = int(cedula[i]) * coeficientes[i]
                    if digito > 9:
                        digito -= 9
                    suma += digito
            
                total = suma % 10
                if total != 0:
                    total = 10 - total                
                if total == int(cedula[9]):
                    return cedula
                else:
                    gotoxy(len(text),columna);print(' '*22)
                    gotoxy(len(text),columna);print('No es una cedula real')
                    time.sleep(2)
                    gotoxy(len(text),columna);print(' '*22)
                    
            else:
                    gotoxy(len(text),columna);print(' '*22)
                    gotoxy(len(text),columna);print('No es una cedula real')
                    time.sleep(2)
                    gotoxy(len(text),columna);print(' '*22)
                    
    def numerosEnteros(text,fila,columna):
        while True:
            try:
                gotoxy(fila,columna);number=float(input(text))
                if number.is_integer():
                    number=int(number)
                    return number
                else:
                    print('Solo numeros enteros')        
            except ValueError:
                gotoxy(fila+len(text),columna);print(' '*20)
                gotoxy(fila+len(text),columna);print('Solo numeros')
                time.sleep(2)
                gotoxy(fila+len(text),columna);print(' '*20)
    def numerosDecimales(text,fila,columna):
        while True:
            try:
                gotoxy(fila,columna);number=float(input(text))
                number_fort=round(number,2)
                return number_fort
            except ValueError:
                gotoxy(fila+len(text),columna);print(' '*20)
                gotoxy(fila+len(text),columna);print('Solo numeros')
                time.sleep(2)
                gotoxy(fila+len(text),columna);print(' '*20)
    def formato_periodo(text,fila,columna):
        while True:
            gotoxy(fila,columna);cadena=input(text)
            patron = r"^\d{4}-\d{4}$"
            if re.match(patron,cadena):
                return cadena
            else:
                gotoxy(fila+len(text),columna);print(' '*40)
                gotoxy(fila+len(text),columna);print('Formato incorrecto')
                time.sleep(2)
                gotoxy(fila+len(text),columna);print(' '*40)
    def nivel(text,fila,columna):
        while True:
            gotoxy(fila,columna);nivel=input(text)
            json_file=JsonFile('File/nivel.json')
            level_buscando=json_file.find('id',nivel)
            if level_buscando:
                return nivel
            else:
                gotoxy(fila+len(text),columna);print(' '*20)
                gotoxy(fila+len(text),columna);print('Nivel no existe')
                time.sleep(2)
                gotoxy(fila+len(text),columna);print(' '*20)
    def valida_nota(text,fila,columna):
        while True:
            try:
                gotoxy(fila,columna);nota=float(input())
                nota=round(nota)
                if text=='nota':
                    if nota>=0 and nota<=20:
                        return nota
                elif text=='examen':
                    if nota>=0 and nota<=60:
                        return nota
                else:
                    if nota>=0 and nota<=100:
                        return nota
                gotoxy(fila,columna);print(' '*20)
            except:
                gotoxy(fila,columna);print(' '*20)
                gotoxy(fila,columna);print('Solo numeros')
                gotoxy(fila,columna);print(' '*20)