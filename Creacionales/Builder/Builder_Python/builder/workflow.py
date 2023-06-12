from .executer import Executer

class WorkFlow(Executer): #* Dentro del patrón de diseño, este es un ConcreteBuilder
    actions:list = []
    
    def getElements(self):
        print("Estoy obteniendo los elementos")
        
    def processElements(self):
        print("Estoy procesando los elementos")
        
    def terminar(self):
        print("Estoy terminando")
        
    def loadActions(self, actions:list):
        self.actions = actions
    
    def work(self):
        for action in self.actions:
            if action == 1:
                self.getElements()
            elif action == 2:
                self.processElements()
            elif action == 3:
                self.terminar()
            else:
                print("No se reconoce la accion")