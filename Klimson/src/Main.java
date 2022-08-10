

import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        ArrayList<String> food = new ArrayList<String>();
        ArrayList<String> guests = new ArrayList<String>();

        //INT KEYS
        int foodList = 1;
        int foodFromList = 2;
        int guestsList = 3;
        int guestFromList = 4;
        int author = 5;
        int endProgram = 6;

        //FOOD
        food.add("Void space for new ArrayList element!");
        food.add("Pizza");
        food.add("Hamburger");
        food.add("HotDog");
        food.add("Spaghetti");

        //GUESTS
        guests.add("Tom");
        guests.add("Jack");
        guests.add("Michael");
        guests.add("Max");
        guests.add("Brock");

        food.set(0, "Sandwich");

        Scanner scanner = new Scanner(System.in);

        boolean stillWorking = true;

        while(stillWorking){

        System.out.println("Choose option:");
        System.out.println("1. Display food list");
        System.out.println("2. Display food from the list");
        System.out.println("3. Display guests list");
        System.out.println("4. Display guest from the list");
        System.out.println("5. Author");
        System.out.println("6. Finish interaction with program");
        System.out.println("");
        int listOptions = scanner.nextInt();

        if (listOptions==foodList){
            System.out.println("");
            System.out.println("Food list: ");
            System.out.println(food);
            System.out.println("");
        }

        if (listOptions==foodFromList){
            System.out.println("");
            System.out.println("Items in list: "+food.size());
            System.out.println("Choose number from list: ");
            int foodNumber = scanner.nextInt();
            foodNumber--;
            System.out.println("");
            System.out.println("Chosen food from the list: "+food.get(foodNumber));
            System.out.println("");
        }

            if (listOptions==guestsList) {
                System.out.println("");
                System.out.println("Guests list: ");
                System.out.println("");
                System.out.println(guests);
                System.out.println("");
            }

            if (listOptions==guestFromList) {
                System.out.println("");
                System.out.println("Items in list:"+guests.size());
                System.out.println("Choose guest from the list: ");
                System.out.println("");
                int guestNumber = scanner.nextInt();
                guestNumber--;
                System.out.println("Chosen guest from the list: "+ guests.get(guestNumber));
            }

        if (listOptions==endProgram){
            stillWorking = false;
            System.out.println("");
            System.out.println("Thanks for using my java program!");
            System.out.println("");
          }

        if(listOptions==author){
            System.out.println("");
            System.out.println("Program builded by Jakub");
            System.out.println("");
          }

        }
    }
}
