package Fabricas_concretas;

import Fabrica_abstracta.VehicleAbstractFactory;
import Producto.Vehicle;
import Producto_concreto.CruiseMotorbike;
import Producto_concreto.SportMotorbike;

// Fabrica Concreta
public class MotorbikeFactory extends VehicleAbstractFactory {
    public final int SPORT = 1;
    public final int CRUISE = 2;

    @Override
    public Vehicle getVehicle(int t) {
        switch (t) {
            case SPORT:
                return new SportMotorbike();
            case CRUISE:
                return new CruiseMotorbike();
        }

        return null;
    }
}