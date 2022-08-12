package Nauka;

public class Table {
    public static void main (String[] args) {

        //TABLICE DO ZADAŃ
        int[] tablica1 = {1, 2, 3, 4};
        int[] tablica2 = {1, 2, 3, 4};


        //ZADANIE1: ZAMIEŃ ZE SOBA PIERWSZY I OSTATNI ELEMENT W TABLICY

        System.out.println("Zadanie 1: ");
        System.out.println("");

        int first = tablica1[0];
        int last = tablica1[3];

        tablica1[0] = last;
        tablica1[3] = first;


        for (int number1 : tablica1) {
            System.out.println(number1);}
        System.out.println("");

        //ZADANIE2: ZAMIEŃ ZE SOBA PIERWSZY i OSTATNI ELEMENT W TABLICY (PRZY POMOCY JEDNEJ ZMIENNEJ!)

        System.out.println("Zadanie 2: ");
        System.out.println("");

        int temp = tablica2[3]; //1
        tablica2[3] = tablica2[0];
        tablica2[0] = temp;
        for (int number2 : tablica2
        ) {
            System.out.println(number2);
        }
        System.out.println("");
    }
    }

