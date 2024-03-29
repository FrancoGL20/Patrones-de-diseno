package Fabrica_abstracta;

import Fabricas_concretas.CarFactory;
import Fabricas_concretas.MotorbikeFactory;
import Producto.Vehicle;

// Fabrica Abstracta
public abstract class VehicleAbstractFactory {
    public static final int CarFactory = 1;
    public static final int MotorbikeFactory = 2;

    public abstract Vehicle getVehicle(int t);

    public static VehicleAbstractFactory getFactory(int t) {
        switch (t) {
            case CarFactory:
                return new CarFactory();
            case MotorbikeFactory:
                return new MotorbikeFactory();
        }
        return null;
    }
}