from builder.builder import Builder

def main(): #* Dentro del patrón de diseño, este es el director
    # Se crea el builder
    builder:Builder = Builder()
    
    # Se crea un ejecutor de tipo WorkFlow
    builder.setExecuter(1)
    
    # Se agregan las acciones que se quieren ejecutar
    builder.addAction(1)
    builder.addAction(2)
    builder.addAction(3)
    builder.addAction(4)
    builder.addAction(5)
    
    # Se ejecuta el builder
    builder.setActions()
    
    # Se ejecuta el workflow
    builder.exec.work()

if __name__ == '__main__':
    main()