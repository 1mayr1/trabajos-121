
public class Estadistica {
    private double[] numeros;
    public Estadistica(double[] numeros) {
        this.numeros = numeros;
    }

    public double promedio() {
        double suma = 0;
        for (int i = 0; i < numeros.length; i++) {
            suma += numeros[i];
        }
        return suma / numeros.length;
    }

    public double desviacion() {
        double prom = promedio();
        double sumaCuadrados = 0;

        for (int i = 0; i < numeros.length; i++) {
            double diferencia = numeros[i] - prom;
            sumaCuadrados += diferencia * diferencia;
        }
        return Math.sqrt(sumaCuadrados / (numeros.length - 1));
    }
}
