import java.util.Scanner;

public class Test {
    public static void main(String[] args) {

        boolean marked = false;

        while(marked==false) {

            Scanner scanner = new Scanner(System.in);
            System.out.println("Podaj liczbe:");
            int number = scanner.nextInt();
            if (number >= 1 && number < 10) {
                number--;
                System.out.println(number);
                marked = true;
                System.out.println("Zakonczono dzialanie");
            } else {
                System.out.println("Niepoprawna liczba");
            }
        }
    }
}
