from datetime import datetime
from clsJson import JsonFile
class Periodo:
    next=0
    def __init__(self,descripcion) :
        json_file=JsonFile('File/id.json')
        id_periodo=json_file.read()
        Periodo.next=id_periodo['id_periodo']
        Periodo.next+=1
        self.__id=('P0' if id_periodo['id_periodo']<10 else 'P')+str(Periodo.next)
        self.periodo=descripcion
        self.fecha_creacion=datetime.now().strftime("%d-%b-%Y %H:%M:%S")  
        self.activo=True
        id_periodo['id_periodo']=Periodo.next
        json_file.save(id_periodo)
    @property
    def id(self):
        return self.__id
    def __str__(self):
        # Método especial para representar la clase Cliente como una cadena
        return f'Periodo: {self.periodo} '  
    
    def show(self):
        print(f'Periodo: ID:{self.id} Periodo:{self.periodo} Activo: {self.activo} Fecha de creacion:{self.fecha_creacion}')     
    def getJson(self):
        return {"id":self.id,"periodo":self.periodo,"activo":self.activo,"fecha_creacion":self.fecha_creacion}
