from builder.builder import Builder
import json

def loadProcess():
    with open('process.json') as json_file:
        data = json.load(json_file)
    
    return data

def main(): #* Dentro del patrón de diseño, este es el director
    # Se cargan los datos del proceso y el ejecutor desde el archivo json
    process=loadProcess()
    executer=process['executer']
    process=process['process']
        
    # Se crea el builder
    builder:Builder = Builder()
    
    # Se crea un ejecutor de tipo WorkFlow
    builder.setExecuter(executer)
    
    # Se agregan las acciones que se quieren ejecutar
    for action in process:
        builder.addAction(action)
    
    # Se ejecuta el builder
    builder.setActions()
    
    # Se ejecuta el workflow
    builder.exec.work()

if __name__ == '__main__':
    main()