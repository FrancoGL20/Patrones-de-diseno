from .executer import Executer

class Vehicle(Executer): #* Dentro del patrón de diseño, este es un ConcreteBuilder
    actions:list = []
    
    def compraMateriaPrima(self):
        print("Estoy comprando materia prima")
        
    def ensamblar(self):
        print("Estoy ensamblando el vehiculo")
                
    def pintar(self):
        print("Estoy pintando el vehiculo")
    
    def pruebas(self):
        print("Estoy haciendo pruebas al vehiculo")
        
        
    def loadActions(self, actions:list):
        self.actions = actions
    
    def work(self):
        for action in self.actions:
            if action == 1:
                self.compraMateriaPrima()
            elif action == 2:
                self.ensamblar()
            elif action == 3:
                self.pintar()
            elif action == 4:
                self.pruebas()
            else:
                print("No se reconoce la accion")