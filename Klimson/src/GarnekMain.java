package Nauka;

public class GarnekMain {
    public static void main(String[] args){
        //Garnek garnek = new Garnek();
                            //^Konstruktor
        //garnek.srednica = 7;
        //garnek.wysokosc =  5;
        //garnek.kolor = "Srebrny";

        //System.out.println(garnek.srednica);
        //System.out.println(garnek.wysokosc);
        //System.out.println(garnek.kolor);

        Garnek garnek = new Garnek(7, 5, "srebrny");

        //System.out.println(garnek.srednica);
        //System.out.println(garnek.wysokosc);
        //System.out.println(garnek.kolor);

        String wiadomosc = garnek.gotuj();
        System.out.println(wiadomosc);

        String wiadomosc2 = garnek.gotuj(true);
        System.out.println(wiadomosc2);

        int temperatura = garnek.water();
        System.out.println(temperatura);

    }
}
