<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>hehehe</title>
</head>
<body>

<!-- Stwórz:

a/ stronę, która będzie szablonem na kolejne ćwiczenia. Strona ma posiadać:
- kodowanie polskich znaków,
- styl css w oddzielnym pliku,
- słowa kluczowe, meta tagi, informację o stronie,
- skrypty w języku php.


b/ stopkę, która będzie na każdym ze skryptów a w niej imię i nazwisko, oraz data ostatniej modyfikacji pliku. Skrypt dowolny.
c/ stronę główną (index.php), która będzie posiadać odnośniki do zadań, oraz do opisu czym się różni wysyłanie metodą POST i GET.


Wykonaj następujące skrypty wraz z formularzami w języku PHP.


zad.1
Skrypt obliczający algorytm Euklidesa,

zad. 2
Kalkulator, który wykona +, -, *, / oraz sprawdzi jakie są podane dwie liczby. Parzyste czy nie parzyste. Kalkulator ma mieć możliwość wyboru wykonywanej operacji. Pola nie mogą być puste.

zad. 3
Skrypt wyświetlający ilość obrazków na środku strony. Ilość podajemy w formularzu.

zad. 4
Strona z logowaniem. Login: Admin, Hasło: zaq1@WSX. Po zalogowaniu wyświetli się napis: Witaj Admin, po błędzie brak dostępu i odnośnik do ponownego zalogowania. Dla podwyższenia oceny zastosuj sesję (nie było jeszcze omawiane)

zad. 5
Skrypt sprawdzający czy podana liczba jest liczbą pierwszą.

zad. 6
Skrypt generujący pięć liczb losowych i wyświetlający ich sumę.

zad. 7
Skrypt  wyświetlający losowe liczby z przedziału 0-10 do momentu aż ich suma przekroczy 100. Skrypt ma zliczać liczbę wykonania pętli.

zad. 8
Wgraj na serwer 10 obrazów graficznych o nazwach 1.jpg, 2.jpg,....,9.jpg,10.jpg. Stwórz skrypt, który będzie losowo wyświetlał jeden z plików graficznych.

zad. 9
Napisz program, który wyświetli sumę tablicy dwuwymiarowej 10x10; Liczby do tablicy mają być wpisane losowo z zakresu od 1 do 100.

zad. 10
Stwórz formularz, który ma 10 pól liczbowych. Skrypt ma przyjąć wartości i posortować je za pomocą funkcji sort oraz za pomocą tradycyjnego sortowania bąbelkowego.



Prześlij pliki źródłowe oraz wgraj stronę na serwer zenbox  Prześlij link do strony.
POWODZENIA  -->


<h2>Algorytm Euklidesa</h2>
<p>
<?php
    // $a = $_POST["euklides_a"]; // pobieramy wartość z formularza
    $a = 5;
    $b = 10;
    $c = 0;
    while ($b != 0) {
        $c = $a % $b;
        $a = $b;
        $b = $c;
    }
    echo "NWD = $a";
?>
</p>

<hr>

<h2>Kalkulator</h2>
<p>
    <?php
        $a = 5;
        $b = 10;

        if ($a % 2 == 0) {
            echo "Liczba $a jest parzysta</br>";
        } else {
            echo "Liczba $a jest nieparzysta</br>";
        }

        if ($b % 2 == 0) {
            echo "Liczba $b jest parzysta</br>";
        } else {
            echo "Liczba $b jest nieparzysta</br>";
        }

        $operator = "+";

        echo "Wynik działania $a $operator $b = ";

        if ($operator == "+") {
            echo $a + $b;
        } elseif ($operator == "-") {
            echo $a - $b;
        } elseif ($operator == "*") {
            echo $a * $b;
        } elseif ($operator == "/") {
            echo $a / $b;
        }
            

    ?>
</p>

<hr>

<h2>Ilość obrazków</h2>
<p>
    <?php
        $ilosc = 5;
        for ($i = 0; $i < $ilosc; $i++) {
            echo "<img src='https://place-hold.it/100x100' alt=''>";
        }
    ?>
</p>

<hr>

<h2>Logowanie</h2>
<p>
    <?php
        $login = "Admin"; //$_POST["login"];
        $haslo = "zaq1@WSX"; //$_POST["haslo"]

        if (isset($login) && isset($haslo)) {
            if ($login == $login && $haslo == $haslo) {
                echo "Witaj $login";
            } else {
                echo "Brak dostępu";
                header("Location:logowanie.php"); // przekierowanie do pliku logowanie.php, chyba zadziała?
            }
        }
    ?>
</p>

<hr>

<h2>Liczba pierwsza</h2>
<p>
    <?php
        $liczba = 5;
        $pierwsza = true;

        for ($i = 2; $i < $liczba; $i++) {
            if ($liczba % $i == 0) {
                $pierwsza = false;
                break;
            }
        }

        if ($pierwsza) {
            echo "Liczba $liczba jest pierwsza";
        } else {
            echo "Liczba $liczba nie jest pierwsza";
        }
    ?>
</p>

<hr>

<h2>Suma 5 liczb losowych</h2>
<p>
    <?php
        $suma = 0;
        $liczby = array();
        for ($i = 0; $i < 5; $i++) {
            $losowa = rand(0, 100);
            array_push($liczby, $losowa);
            $suma += $losowa;
        }
        echo "Suma = $suma";
        echo "<br>";
        echo "Liczby: ";
        for ($i = 0; $i < count($liczby); $i++) {
            echo $liczby[$i] . ", ";
        }
    ?>
</p>

<hr>

<h2>Suma liczb losowych do 100</h2>
<p>
    <?php
        $suma = 0;
        $liczby = array();
        $i = 0;
        while ($suma < 100) {
            $losowa = rand(0, 10);
            array_push($liczby, $losowa);
            $suma += $losowa;
            $i++;
        }
        echo "Suma = $suma";
        echo "<br>";
        echo "Liczby: ";
        for ($i = 0; $i < count($liczby); $i++) {
            echo $liczby[$i] . ", ";
        }
        echo "<br>";
        echo "Ilość wykonania pętli: $i"; 
    ?>
</p>

<hr>

<h2>Losowy obrazek graficzny</h2>
<p>
    <!-- Choose a random image from 1.jpg to 10.jpg -->
    <?php
        $losowa = rand(1, 10);
        echo "Obrazek nr $losowa<br>";
        echo "<img src='obrazki/$losowa.jpg' width=200 alt=''>"; 
    ?>
</p>

<hr>

<h2>Suma tablicy dwuwymiarowej</h2>
<p>
    <?php
        $tablica = array(); // główna tablica

        // Tutaj generujemy tablice 
        for ($i = 0; $i < 10; $i++) { // Główna tablica
            $tablica[$i] = array();
            for ($j = 0; $j < 10; $j++) { // Podtablice - np. tablica[0][1], czyli druga podtablica pierwszej głównej
                $tablica[$i][$j] = rand(0, 10);
            }
        }

        $suma = 0;
        for ($i = 0; $i < count($tablica); $i++) { // na każdą główną tablicę
            for ($j = 0; $j < count($tablica[$i]); $j++) { // na każdą podtablicę
                $suma += $tablica[$i][$j];
            }
        }
        echo "Suma = $suma";
    ?>
</p>

<hr>

<h2>Sortowanie bąbelkowe i funkcją</h2>
<p>
    <?php
        $a = 21;
        $b = 2;
        $c = 6;
        $d = 1;
        $e = 9;
        $f = 76;
        $g = 36;
        $h = 98;
        $i = 51;
        $j = 11;

        $tablica1 = array($a, $b, $c, $d, $e, $f, $g, $h, $i, $j);
        $tablica2 = array($a, $b, $c, $d, $e, $f, $g, $h, $i, $j);
        echo "Sortowanie funkcją: ";
        sort($tablica1);
        for ($i = 0; $i < count($tablica1); $i++) {
            echo $tablica1[$i] . ", ";
        }
        echo "<br>";

        echo "Sortowanie bąbelkowe: ";
        for( $i = 0; $i < count($tablica2); $i++ ) {
            for( $j = 0; $j < count($tablica2); $j++ ) {
                if( $tablica2[$j] < $tablica2[$j+1] ) {
                    $x = $tablica2[$j];
                    $tablica2[$j] = $tablica2[$j+1];
                    $tablica2[$j+1] = $x;
                }
            }
        }
        for ($i = 0; $i < count($tablica2); $i++) {
            echo $tablica2[$i] . ", ";
        }
        echo "<br>";
    ?>
</p>


</body>
</html>
