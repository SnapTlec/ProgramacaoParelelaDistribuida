package calculadora.server;

import java.rmi.server.*;
import java.rmi.*;
import calculadora.Interfaces.ICalculadora;

public class CalculadoraImp extends UnicastRemoteObject implements ICalculadora {
    private float resultado = 0;
    public CalculadoraImp() throws RemoteException{};

    public float somar(float t1, float t2) throws RemoteException
    {
        float soma = t1 + t2;
        this.resultado = soma;
        return soma;
    }

    public float subtrair(float t1, float t2) throws RemoteException
    {
        float subtracao = t1 - t2;
        this.resultado = subtracao;
        return subtracao;
    }

    public float recuperarResultado()
    {
        return this.resultado;
    }

}
