//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] lista = new double[10];
        System.out.println("Ingrese 10 números:");

        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            lista[i] = sc.nextDouble();
        }

        Estadistica est = new Estadistica(lista);
        System.out.printf("El promedio es %.2f%n", est.promedio());
        System.out.printf("La desviación estándar es %.5f%n", est.desviacion());
    }
}

