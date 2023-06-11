package Producto_concreto;
// Producto Concreto

import Producto_especifico.Motorbike;

public class CruiseMotorbike implements Motorbike {

    @Override
    public String getType() {
        return "Cruise!";
    }

    @Override
    public int getWheels() {
        return 2;
    }

    @Override
    public int getSeats() {
        return 2;
    }
}