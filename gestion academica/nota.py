from calculos import ICalculo
from datetime import datetime
from clsJson import JsonFile
import os

class NotaDetail:
    def __init__(self,nota1,nota2,exam,remedial):
        self.nota1=nota1
        self.nota2=nota2
        self.examen=exam
        self.remedial=remedial
    def __str__(self):
        return (f"Nota1: {self.nota1}, Nota2: {self.nota2}, Examen: {self.examen}, Remedial: {self.remedial}")
    def to_dict(self):
        return {
            "nota1": self.nota1,
            "nota2": self.nota2,
            "examen": self.examen,
            "remedial": self.remedial
        }

class Nota(ICalculo):
    next=0
    def __init__(self,estudiante,profesor,asignatura,periodo,nivel):
        json_file=JsonFile('File/id.json')
        id_nota=json_file.read()
        Nota.next=id_nota['id_nota']
        Nota.next+=1
        self.__id=('N0' if id_nota['id_nota']<10 else 'N')+str(Nota.next)
        self.estudiante=estudiante
        self.profesor=profesor
        self.nivel=nivel
        self.periodo=periodo
        self.asignatura=asignatura
        self.promedio=0
        self.observacion=""
        self.fecha_creacion=datetime.now().strftime("%d-%b-%Y %H:%M:%S") 
        self.notas_detalle=[]
        id_nota['id_nota']=Nota.next
        json_file.save(id_nota)
    @property
    def id(self):
        return self.__id
    def cal_promedio(self, nota1, nota2, exam):
        return round(nota1+nota2+exam)
    def cal_remedial(self, nota1,nota2,exam, remedial):
        return round((nota1+nota2+exam+remedial)/2)
    def add_nota(self,nota1,nota2,exam,remedial):
        detalle=NotaDetail(nota1,nota2,exam,remedial)
        self.promedio=self.cal_promedio(nota1,nota2,exam) if remedial==0 else self.cal_remedial(nota1,nota2,exam,remedial)
        self.observacion='Aprobado' if self.promedio >=70 else 'Reprobado'
        self.notas_detalle.append(detalle)
    def getJson(self):
        notas={"id":self.id,"fecha_creacion":self.fecha_creacion,"periodo":self.periodo,"nivel":self.nivel,"asignatura":self.asignatura,"estudiante":self.estudiante,"profesor":self.profesor,"promedio":self.promedio,'Observacion':self.observacion,'Notas':[detalle.to_dict() for detalle in self.notas_detalle]}
        return notas
