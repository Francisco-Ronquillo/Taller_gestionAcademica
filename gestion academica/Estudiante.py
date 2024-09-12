from datetime import datetime
from clsJson import JsonFile
class Student:
    next=0
    def __init__(self, first_name="Null", last_name="Null"):
        json_file=JsonFile('File/id.json')
        id_student=json_file.read()
        Student.next=id_student['id_student']
        Student.next+=1
        self.first_name = first_name
        self.last_name = last_name
        self.__id=('E0' if id_student['id_student']<10 else 'E')+str(Student.next)
        self.activo=True 
        self.fecha_creacion=datetime.now().strftime("%d-%b-%Y %H:%M:%S")       
        id_student['id_student']=Student.next
        json_file.save(id_student)
    @property
    def id(self):
        
        return self.__id
    def __str__(self):
        return f'Estudiante: {self.first_name} {self.last_name}'  
    
    def fullName(self):
        return self.first_name + ' ' + self.last_name
    
    def show(self):
        
        print(f'Estudainte: ID:{self.id} Nombre: {self.first_name} {self.last_name} Activo: {self.activo} Fecha de creacion:{self.fecha_creacion}')     
    def getJson(self):
        return {"id":self.id,"nombre":self.first_name,"apellido":self.last_name,"activo":self.activo,"fecha_creacion":self.fecha_creacion}