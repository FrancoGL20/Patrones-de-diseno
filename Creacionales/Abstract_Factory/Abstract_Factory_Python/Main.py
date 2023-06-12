from Abstract.Fabricas_concretas.AutoFactory import AutoFactory
from Abstract.Fabricas_concretas.MotoFactory import MotoFactory

# Cliente
def client(factory):
    vehicle = factory.create_vehicle()
    
    engine = factory.create_engine()
    wheel = factory.create_wheel()
    light = factory.create_light()

    result = vehicle.assemble(engine, wheel, light)
    return result

# Uso del patrón Abstract Factory
auto_factory = AutoFactory()
result_auto = client(auto_factory)
print(result_auto)  # Salida: Ensamblando un auto con Motor global, Rueda global, y Luz de auto

moto_factory = MotoFactory()
result_moto = client(moto_factory)
print(result_moto)  # Salida: Ensamblando una moto con Motor global, Rueda global, y Luz de moto