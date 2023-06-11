import java.util.Scanner;

import Fabrica_abstracta.VehicleAbstractFactory;
import Producto.Vehicle;

public class Main {
    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);

        System.out.print("Digite el tipo de Fábrica: 1=carro, 2=moto: ");
        int typeAbstract = t.nextInt();
        VehicleAbstractFactory abstractFactory = VehicleAbstractFactory.getFactory(typeAbstract);
        
        System.out.print("Digite el tipo de vehículo: ");
        int typeVehicle = t.nextInt();
        Vehicle vehicle = abstractFactory.getVehicle(typeVehicle);
        System.out.println("Llantas: " + vehicle.getWheels());
        System.out.println("Asientos: " + vehicle.getSeats());
    }
}