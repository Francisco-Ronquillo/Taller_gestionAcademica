from datetime import datetime
from clsJson import JsonFile
class Teacher:
    next=0
    def __init__(self, first_name="Null", last_name="Null"):
        json_file=JsonFile('File/id.json')
        id_teacher=json_file.read()
        Teacher.next=id_teacher["id_teacher"]
        Teacher.next+=1
        self.first_name = first_name
        self.last_name = last_name
        self.__id=('T0' if id_teacher['id_student']<10 else 'T')+str(Teacher.next)
        self.activo=True
        self.fecha_creacion=datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        id_teacher["id_teacher"]=Teacher.next
        json_file.save(id_teacher)    
    @property
    def id(self):
        return self.__id
    def __str__(self):

        return f'Cliente: {self.first_name} {self.last_name}'  
    
    def fullName(self):
        return self.first_name + ' ' + self.last_name
    
    def show(self):
        print(f'Estudainte: ID:{self.id} Nombre: {self.first_name} {self.last_name} Activo: {self.activo} Fecha de creacion:{self.fecha_creacion}')     
    def getJson(self):
        return {"id":self.id,"nombre":self.first_name,"apellido":self.last_name,"activo":self.activo,"Fecha de creacion":self.fecha_creacion}
