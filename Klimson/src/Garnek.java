package Nauka;

public class Garnek {



        //**      public -  modfikator dostępu
        //      np: public, private, protected

        //      class - słowo kluczowe java

        //      Garnek - instancja lub objekt klasy Garnek

        //POLE KLASY GARNEK

        //      final srenica; //--Okrreśla ostateczną zmienna, której nie można zmieniać!
        int srednica; //--pole klasy
        int wysokosc;
        String kolor;

  public Garnek( int srednica, int wysokosc, String kolor){
            this.srednica = srednica; //używa srednicy z linijki 10 aby przpisac typ zmiennej do zmiennej w "Garnek"
            this.wysokosc = wysokosc; //etc
            this.kolor = kolor; //etc
        }

        //wykorzystanie kilku metod z innymi zmiennymi to overloading czyli przeciązanie
        public String gotuj () {
            return "Gotowanie w trakcie";
        }
            public String gotuj (boolean czyDodalismySol) {
                if (czyDodalismySol) {
                    return "Gotowanie z sola";
                } else {
                    return "Gotowanie bez soli";
                }
            }

            public int water() {
                    return 100;}

            }
