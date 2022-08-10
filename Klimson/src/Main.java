
import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        ArrayList<String> food = new ArrayList<String>();
        ArrayList<String> guests = new ArrayList<String>();

        //FOOD
        food.add("Void space for new ArrayList element!");
        food.add("Pizza"); //Pierwszy element listy
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

        while(stillWorking==true){

        System.out.println("Choose option:");
        System.out.println("1. Display food list");
        System.out.println("2. Display food from the list");
        System.out.println("3. Display guests list");
        System.out.println("4. Display guest from the list");
        System.out.println("5. Finish interaction with program");
        System.out.println("");
        int listOptions = scanner.nextInt();

        if (listOptions==1){
            System.out.println("Food list: ");
            System.out.println(food);
        }

        if (listOptions==2){
            System.out.println("Choose number from list: ");
            int foodNumber = scanner.nextInt();
            System.out.println("Chosen food from the list: "+food.get(foodNumber));
        }

            if (listOptions==3) {
                System.out.println("Guests list: ");
                System.out.println(guests);
            }

            if (listOptions==4) {
                System.out.println("Choose guest from the list: ");
                int guestNumber = scanner.nextInt();
                System.out.println("Chosen guest from the list: "+ guests.get(guestNumber));
            }

        if (listOptions==5){
            stillWorking = false;
            System.out.println("Thanks for using my java program!");
          }

        }
    }
}