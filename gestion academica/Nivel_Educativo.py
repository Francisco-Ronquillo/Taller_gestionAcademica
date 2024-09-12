from datetime import datetime
from clsJson import JsonFile
class Nivel:
    next=0
    def __init__(self,nivel):
        json_file=JsonFile('File/id.json')
        id_nivel=json_file.read()
        Nivel.next=id_nivel['id_nivel']
        Nivel.next+=1
        self.id=('L0' if id_nivel['id_nivel']<10 else 'L')+str(Nivel.next)
        self.activo=True
        self.fecha_creacion=datetime.now().strftime("%d-%b-%Y %H:%M:%S") 
        self.nivel=nivel
        id_nivel['id_nivel']=Nivel.next
        json_file.save(id_nivel)

    def id(self):
        return self.__id
    def __str__(self):
        # Método especial para representar la clase Cliente como una cadena
        return f'Cliente: {self.first_name} {self.last_name}'  
    
    def show(self):
        # Método para imprimir los detalles del cliente VIP en la consola
        print(f'Nivel: ID:{self.id} Nivel:{self.nivel} Activo: {self.activo} Fecha de creacion:{self.fecha_creacion}')     
    def getJson(self):
        # Método para imprimir los detalles del cliente VIP en la consola
        return {"id":self.id,"nivel":self.nivel,"activo":self.activo,"fecha_creacion":self.fecha_creacion}    