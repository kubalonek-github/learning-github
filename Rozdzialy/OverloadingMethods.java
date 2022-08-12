package Rozdzialy;

import java.util.Scanner;

public class OverloadingMethods {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int number1;
        int number2;
        int number3;
        int number4;

        System.out.println("Wybierz opcje");
        System.out.println("1. Dodaj trzy liczby");
        System.out.println("2. Dodaj cztery liczby");
        int choice = scanner.nextInt();

        switch(choice) {
            case 1-> {System.out.println("Wpisz 3 liczby");
            number1 = scanner.nextInt();
            number2 = scanner.nextInt();
            number3 = scanner.nextInt();
            int x = add(number1, number2, number3);
                System.out.println(x);}
            case 2 -> {
                System.out.println("Wpisz 4 liczby");
                number1 = scanner.nextInt();
                number2 = scanner.nextInt();
                number3 = scanner.nextInt();
                number4 = scanner.nextInt();
                int y = add(number1, number2, number3, number4);
                System.out.println(y);
            }

                //OVERLOADING METHODS

            }
    }

        static int add (int a, int b, int c, int d){
            return a + b + c + d;
        }

        static int add ( int a, int b, int c){
            return a + b + c;
        }
    }

