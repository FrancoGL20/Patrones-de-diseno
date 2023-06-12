from abc import ABC, abstractmethod

class Executer(ABC): #* Dentro del patrón de diseño, este es el Builder
    @abstractmethod
    def loadActions(self, actions:list):
        pass
    
    @abstractmethod
    def work(self):
        pass