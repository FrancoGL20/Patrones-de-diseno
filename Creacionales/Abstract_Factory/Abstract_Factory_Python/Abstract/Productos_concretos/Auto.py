from abc import ABC, abstractmethod
from Abstract.Producto.Vehicle import Vehicle

# Concrete Product: Auto
class Auto(Vehicle):
    def assemble(self, engine, wheel, light):
        return f"Ensamblando un auto con {engine}, {wheel}, y {light}"