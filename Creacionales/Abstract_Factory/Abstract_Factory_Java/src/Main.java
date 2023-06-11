import java.util.Scanner;

import Fabrica_abstracta.VehicleAbstractFactory;
import Producto.Vehicle;

public class Main {
    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        
        // Se crea un objeto de tipo VehicleAbstractFactory y se le asigna el valor de la fabrica concreta (CarFactory o MotorbikeFactory) dependiendo del tipo de vehículo que se quiera crear
        System.out.print("Digite el tipo de Fábrica: 1=carro, 2=moto: ");
        int typeAbstract = t.nextInt();
        VehicleAbstractFactory abstractFactory = VehicleAbstractFactory.getFactory(typeAbstract);
        
        // Se crea un objeto de tipo Vehicle y se le asigna el valor del vehículo concreto (LuxuryCar, FamilyCar, SportMotorbike o CruiseMotorbike) dependiendo del tipo de vehículo que se quiera crear
        System.out.print("Digite el tipo de vehículo: ");
        int typeVehicle = t.nextInt();
        Vehicle vehicle = abstractFactory.getVehicle(typeVehicle);

        // Se imprimen los datos del vehículo concreto creado
        System.out.println("Llantas: " + vehicle.getWheels());
        System.out.println("Asientos: " + vehicle.getSeats());

        t.close();
    }
}