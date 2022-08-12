package Rozdzialy;

public class Metody {
    public static void main(String[] args) {
        String name = "Jakub";
        int age = 19;

        hello(name,age);
    }

    //static - może być uzyta w innym obiekcie w klasie
    static void hello(String name, int age) {
        System.out.println("Hello "+name);
        System.out.println("Masz "+age+" lat");
    }
}


