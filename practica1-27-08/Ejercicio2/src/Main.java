//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Ingrese a, b, c: ");
        double a= sc.nextDouble();
        double b= sc.nextDouble();
        double c= sc.nextDouble();

        EcuacionLineal ecuacion=new EcuacionLineal(a, b, c);
        double discriminante= ecuacion.getDiscriminante();

        if(discriminante>0){
            System.out.println("La ecuacion tiene dos raices "+ecuacion.getRaiz1()+" y "+ecuacion.getRaiz2());
        }else if (discriminante==0){
            System.out.println("La ecuacion tiene una raiz "+ ecuacion.getRaiz1());
        }else {
            System.out.println("La ecuación no tiene raíces reales");
        }
    }
}