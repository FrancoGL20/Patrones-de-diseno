from .executer import Executer
from .workflow import WorkFlow
from .vehicle import Vehicle

class Builder(): #* Dentro del patrón de diseño, este es el Builder
    exec:Executer = None
    actions:list = []
    
    def setExecuter(self, i:int):
        # Se crea el ejecutor dependiendo del tipo de ejecutor que se quiera
        if i == 1:
            self.exec = WorkFlow()
        elif i == 2:
            self.exec = Vehicle()
            
    def addAction(self, action:int):
        # Se agrega una accion a la lista de acciones
        self.actions.append(action)
        
    def setActions(self):
        # Se le pasa la lista de acciones al ejecutor
        self.exec.loadActions(self.actions)