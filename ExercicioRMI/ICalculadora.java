package calculadora.Interfaces;

import java.rmi.*;
public interface ICalculadora extends Remote {
    public float somar(float t1, float t2) throws RemoteException;
    public float subtrair(float t1, float t2) throws RemoteException;
    public float recuperarResultado() throws RemoteException;
}
