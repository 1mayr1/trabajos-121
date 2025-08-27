//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        System.out.print("Ingrese a, b, c, d, e, f: ");
        double a= sc.nextDouble();
        double b= sc.nextDouble();
        double c= sc.nextDouble();
        double d= sc.nextDouble();
        double e= sc.nextDouble();
        double f= sc.nextDouble();

        EcuacionLineal ecuacion= new EcuacionLineal(a ,b ,c ,d ,e ,f);
        if (ecuacion.tieneSolucion()){
            System.out.println("X= "+ ecuacion.getX());
            System.out.println("Y= "+ecuacion.getY());
        }else{
            System.out.println("no tiene solucion");
        }
    }
}