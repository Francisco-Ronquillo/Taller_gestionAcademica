from datetime import datetime
from clsJson import JsonFile
class Detalle_tesis:
    next=0
    def __init__(self,estudiante,nota,observacion):
        json_file=JsonFile('File/id.json')
        id_detalle_tesis=json_file.read()
        Detalle_tesis.next=id_detalle_tesis[ "id_detall_tesis"]
        Detalle_tesis.next+=1
        self.__id=('D0' if id_detalle_tesis['id_detall_tesis']<10 else 'D')+str(Detalle_tesis.next)
        self.estudiante=estudiante
        self.nota=nota
        self.observacion=observacion
        id_detalle_tesis[ "id_detall_tesis"]=Detalle_tesis.next
        json_file.save(id_detalle_tesis)
    @property
    def id(self):
        return self.__id
    def __str__(self):
        return (f"ID:{self.id}Nota: {self.nota}, Estudiante: {self.estudiante}, Observacion:{self.observacion}")
    def to_dict(self):
        return {
            "id": self.id,
            "nota": self.nota,
            "estudiante":self.estudiante,
            "observacion":self.observacion
        }
class Tema_tesis:
    next=0
    def __init__(self,tema,tutor,fecha_sustentacion):
        json_file=JsonFile('File/id.json')
        id_tema_tesis=json_file.read()
        Tema_tesis.next=id_tema_tesis['id_tesis']
        Tema_tesis.next+=1
        self.__id=('T0' if id_tema_tesis['id_tesis']<10 else 'T')+str(Tema_tesis.next)
        self.tema=tema
        self.profesor=tutor
        self.fecha_creacion=datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        self.activo=True
        self.detalle_tesis=[]
        self.fecha_sustentacion=fecha_sustentacion
        id_tema_tesis['id_tesis']=Tema_tesis.next
        json_file.save(id_tema_tesis)
    @property
    def id(self):
        return self.__id
    def addDetalleTesis(self,estudiante,nota):
        observacion="Aprobado" if nota>=70 else "Reprobado"
        self.detalle_tesis.append(Detalle_tesis(estudiante,nota,observacion))
    def getJson(self):
        notas={"id":self.id,"fecha_creacion":self.fecha_creacion,"tutor":self.profesor,'detalle_tesis':[detalle.to_dict() for detalle in self.detalle_tesis]}
        return notas

