package calculadora.client;

import java.rmi.*;
import calculadora.Interfaces.*;
public class CalculadoraClient {
    public static void main(String[] args) throws Exception
    {
        String hostname = args[0];
        String objeto = args[1];
        float t1 = Float.parseFloat(args[2]);
        float t2 = Float.parseFloat(args[3]);

        Object obj = Naming.lookup("rmi://" + hostname + "/" + objeto);

        ICalculadora calculadora = (ICalculadora) obj;
        
        calculadora.somar(t1,t2);

        System.out.println("Valor da operação: " + calculadora.recuperarResultado());
    }
}
