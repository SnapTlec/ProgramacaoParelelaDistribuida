package calculadora.server;

import java.rmi.*;
import java.net.*;
import calculadora.Interfaces.*;

public class CalculadoraServer
{
    public static void main(String[] args) throws RemoteException, MalformedURLException
    {
        java.rmi.registry.LocateRegistry.createRegistry(1099);
        System.out.println("RMI registry ready.");
        
        ICalculadora calculadora = new CalculadoraImp();
        Naming.rebind("calculadora", calculadora);
        System.out.println("Servidor no ar. Nome do recurso: calculadora");
    }
}