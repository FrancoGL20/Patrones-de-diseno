package Producto_concreto;
// Producto Concreto

import Producto_especifico.Car;

public class FamilyCar implements Car {

    @Override
    public int getDoors() {
        return 5;
    }

    @Override
    public int getWheels() {
        return 4;
    }

    @Override
    public int getSeats() {
        return 5;
    }
}