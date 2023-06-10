class Singleton:

    __instance = None

    # El método __new__ es el primero que se ejecuta al crear un objeto y siempre tiene que devolver una instancia de la clase
    # Sobreescribimos el método __new__ para que devuelva la misma instancia en lugar de crear una nueva cada vez que se llame a la clase
    def __new__(cls, *args, **kwargs):
        # Si no existe una instancia, la creamos
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        else:
            print("Ya existe una instancia")
        # Si ya existe una instancia, devolvemos la que ya existe
        return cls.__instance

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    first_instance = Singleton("Primera instancia")
    second_instance = Singleton("Segunda instancia")

    print("Nombre de la primera instancia:", first_instance.name)
    print("Nombre de la segunda instancia:", second_instance.name)
    print("¿Son la misma instancia?:", first_instance is second_instance)


    ''' Salida:

    Ya existe una instancia
    Nombre de la primera instancia: Segunda instancia
    Nombre de la segunda instancia: Segunda instancia
    ¿Son la misma instancia?: True

    '''