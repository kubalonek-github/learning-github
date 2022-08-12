package Rozdzialy;

import java.util.Scanner;

public class StringMethods {
    public static void main (String[] args){

        Scanner scanner = new Scanner(System.in);

        System.out.println("Wybierz String method: ");
        int choiceNumber = scanner.nextInt();
        String text = "Jakub";

        //NOWY SWITCH

        switch(choiceNumber) {
            case 1 ->{
                boolean commandOutput = text.equals("Jakub");
                System.out.println("equals: ");
                System.out.println(commandOutput);}
            }
        }
    }

