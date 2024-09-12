from datetime import datetime
from clsJson import JsonFile
class Asignatura:
    next=0
    def __init__(self, descripcion,nivel):
        json_file=JsonFile('File/id.json')
        id_asignatura=json_file.read()
        Asignatura.next=id_asignatura['id_asignatura']
        Asignatura.next+=1
        self.__id=('A0' if id_asignatura['id_asignatura']<10 else 'A')+str(Asignatura.next)
        self.descripcion=descripcion
        self.nivel=nivel
        self.activo=True
        self.fecha_creacion=datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        id_asignatura['id_asignatura']= Asignatura.next
        json_file.save(id_asignatura)
    @property
    def id(self):
        return self.__id
    def __str__(self):
        return f'Asignatura: {self.descripcion}'
    
    def show(self):
        
        print(f'Asignatura: ID:{self.id} Descripcion: {self.descripcion}  Activo: {self.activo} Fecha de creacion:{self.fecha_creacion}')     
    def getJson(self):
        return {"id":self.id,"descripcion":self.descripcion,"nivel":self.nivel,"activo":self.activo,"fecha_creacion":self.fecha_creacion}