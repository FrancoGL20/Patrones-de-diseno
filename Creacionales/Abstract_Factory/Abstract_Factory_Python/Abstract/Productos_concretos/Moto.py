from Abstract.Producto.Vehicle import Vehicle

# Concrete Product: Moto
class Moto(Vehicle):
    def assemble(self, engine, wheel, light):
        return f"Ensamblando una moto con {engine}, {wheel}, y {light}"