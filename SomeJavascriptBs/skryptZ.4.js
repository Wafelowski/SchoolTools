// Trzeba się uczyć Szanowna Pani, zamiast prosić kolegów 
// Polecam https://wafelowski.pl/good_luck/


// Dlaczego "const" and "let" zamiast "var" ? 
// "const" to stała - jej się nie da zmienić
// "let" to zmienna - ją już możemy zmieniać


function DuzeLitery() {
    let imie = document.getElementById("Imie");
    let nazwisko = document.getElementById("Nazwisko");

    imie.value = imie.value.toUpperCase();
    nazwisko.value = nazwisko.value.toUpperCase();
}

function Przywitanie() {
    const imie = document.getElementById("Imie").value;
    const nazwisko = document.getElementById("Nazwisko").value;

    document.getElementById("wynik").innerHTML = `Witaj ${imie} ${nazwisko}`; //Javascript pozwala na używanie zmiennej w stringu, pod warunkiem że zaczyna się on od "`" (przycisk tyldy), a zmienna to "${zmienna}". Inną wersję budowania stringa znajdziesz w funkcji Dane().
}

function Liczba() {
    let liczba = document.getElementById("Liczba");
    if ((liczba == null) || (!liczba.value) || (liczba.value == null) || (liczba.value == "")) { //Sprawdzamy czy pole nie jest puste i czy istnieje (pole może nie istnieć bo nic w nim nie ma).
        document.getElementById("wynik2").innerHTML = "Wprowadź liczbę";
        return
    }

    if ((liczba.value % 2 == 0) || (liczba.value <= 1))  {
        document.getElementById("wynik2").innerHTML = `Liczba ${liczba.value} nie jest liczbą pierwszą`;
    }
    else if (liczba.value > 1) {
        let jestPierwsza = true; //Zakładamy że jest to liczba pierwsza, po czym to sprawdzimy.
        for (let i = 2; i < liczba.value; i++) { //Tu się dzieje nudna matematyka, której mi się nie chce tłumaczyć.
            if (liczba.value % i == 0) {
                jestPierwsza = false;
                break; //Jeśli jednak nie jest to liczba pierwsza, czyt. dzielenie nie wyszło tak jak powinno to przerywamy pętle i zapisujemy werdykt.
            }
        }
        if (jestPierwsza) {
            document.getElementById("wynik2").innerHTML = `Liczba ${liczba.value} jest liczbą pierwszą`;
        }
        else {
            document.getElementById("wynik2").innerHTML = `Liczba ${liczba.value} nie jest liczbą pierwszą`;
        }
    }
    else { //To jest tutaj w przypadku gdybyśmy podali jakąś stringa lub kompletnie dziwną liczbę, np. -1.
        document.getElementById("wynik2").innerHTML = `Liczba ${liczba.value} nie jest liczbą pierwszą`;
    }
    document.getElementById("Drukuj").hidden=false;
    return
}

function Dane() {
    const imie = document.getElementById("Imie2").value;
    const nazwisko = document.getElementById("Nazwisko2").value;
    let pesel = document.getElementById("Pesel").value;

    if (pesel.length != 11) { //Logiczne, nie?
        document.getElementById("wynik3").innerHTML = "Pesel musi mieć 11 cyfr!";
        return
    }
    
    pesel = Array.from(pesel.toString()).map(Number); //Tutaj dzielimy pesel po jednej cyfrze do listy.
    //Array.from pozwoli nam na stworzenie liczby z danej wartości
    //toString() pozwala na stworzenie stringa z liczby
    //map(Number) zmieni nam poprzednio stworzone stringi na liczby
    //Dlaczego wpierw string i później spowrotem na liczbę? Bo tak działa JS, chyba.

    switch (pesel[2]) { //Ten switch nam określa zarówno miesiąc i rok na bazie trzeciej liczby w peselu. Tak jak jest to w tym wytłumaczeniu które ci wysłałem
        case 0: //Warto zapamiętać ze ten array jest od 0 do 10, a nie od 1 do 11. Dlatego 3 pozycja w peselu, ma pozycję 2 w arrayu
            miesiac = `0${pesel[3]}`;
            rok = `19${pesel[0]}${pesel[1]}`;
            break;
        case 1:
            miesiac = `1${pesel[3]}`;
            rok = `19${pesel[0]}${pesel[1]}`;
            break;
        case 2:
            miesiac = `0${pesel[3]}`;
            rok = `20${pesel[0]}${pesel[1]}`;
            break;
        case 3:
            miesiac = `1${pesel[3]}`;
            rok = `20${pesel[0]}${pesel[1]}`;
            break;
        case 4:
            miesiac = `0${pesel[3]}`;
            rok = `21${pesel[0]}${pesel[1]}`;
            break;
        case 5:
            miesiac = `1${pesel[3]}`;
            rok = `21${pesel[0]}${pesel[1]}`;
            break;
        case 6:
            miesiac = `0${pesel[3]}`;
            rok = `22${pesel[0]}${pesel[1]}`;
            break;
        case 7:
            miesiac = `1${pesel[3]}`;
            rok = `22${pesel[0]}${pesel[1]}`;
            break;
        case 8:
            miesiac = `0${pesel[3]}`;
            rok = `18${pesel[0]}${pesel[1]}`;
            break;
        case 9:
            miesiac = `1${pesel[3]}`;
            rok = `18${pesel[0]}${pesel[1]}`;
            break;
        default: //Switch musi mieć default case to raz, dwa to zabezpieczenie w przypadku gdyby ktoś wpisał coś niepożądanego.
            alert("Pesel jest niepoprawny!");
            break;
    }

    const dzien = `${pesel[4]}${pesel[5]}`; //na 100% jest inny sposób by połączyć te dwa obiekty bez ich dodawania do siebie ale js to ustrojstwo
    const data = new Date(rok,miesiac,dzien); //układamy sobie tutaj datę w kolejności rok-miesiąc-dzień
    const dzisiejszaData = new Date(); //new Date() bez parametrów zwróci nam aktualną datę i godzinę, alias do Date.now()
    const Roznica = Math.floor(((dzisiejszaData - data) / (1000 * 60 * 60 * 24)) / 365); // Robimy różnice dwóch dwat po czym przekształcamy w kolejności (ms -> s -> min -> h -> d -> y)

    alert(imie + ", " + nazwisko + ", " + Roznica + " lat"); //Prosty string builder
}

function Data() {
    const dzisiejszaData = new Date();
    let przyszlaData = document.getElementById("przyszlaData").value;
    przyszlaData = przyszlaData.replace(",", ".").replace("-", ".").replace("/", ".").replace(" ", ".").split("."); //W razie wpisania daty z myślnikami/przecinkami/slashami zamienimy je na kropki. Po czym datę dzielimy na części, kropka jest wyznacznikiem przerwy.
    przyszlaData = new Date(`${przyszlaData[2]}.${przyszlaData[1]}.${przyszlaData[0]} ${dzisiejszaData.getHours()}:${dzisiejszaData.getMinutes()}:${dzisiejszaData.getSeconds()}`);
    //Tworzymy datę w kolejności roku, miesiąca i dnia, po spacji dodajemy godzinę, minuty i sekundy.
    const Roznica = przyszlaData - dzisiejszaData; //Obliczamy różnicę znowu

    document.getElementById("wynik4").innerHTML = `<br>Rożnica sekund: ${Math.floor(Roznica / 1000)} <br>Różnica minut: ${Math.floor(Roznica / (1000 * 60))} <br>Roznica dni: ${Math.floor(Roznica / (1000 * 3600 * 24))}`;
    //Wyświetlamy wynik w kolejności sekund, minut, dni.
    //Warto pamiętać że różnicę otrzymujemy w milisekundach, co należy przekształcić na bardziej normalne liczby, dzieląc ją.
    //Dzielimy przez (1000 (sekundy) * 60 (minuty) * 60 (godziny) * 24 (dni) * 365 (lata))
}