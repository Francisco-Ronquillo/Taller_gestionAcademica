from abc import ABC,abstractmethod

class ICalculo(ABC):
    @abstractmethod
    def cal_promedio(self,nota1,nota2,exam):
        
        pass
    def cal_remedial(self,nota1,nota2,exam,remedial):
        pass