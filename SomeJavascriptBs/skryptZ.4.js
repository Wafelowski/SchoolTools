// Trzeba się uczyć Szanowna Pani, zamiast prosić kolegów 
// Polecam https://wafelowski.pl/good_luck/


function DuzeLitery() {
    let imie = document.getElementById("Imie");
    let nazwisko = document.getElementById("Nazwisko");

    imie.value = imie.value.toUpperCase();
    nazwisko.value = nazwisko.value.toUpperCase();
}

function Przywitanie() {
    const imie = document.getElementById("Imie").value;
    const nazwisko = document.getElementById("Nazwisko").value;

    document.getElementById("wynik").innerHTML = `Witaj ${imie} ${nazwisko}`;
}

function Liczba() {
    let liczba = document.getElementById("Liczba");
    if ((liczba == null) || (!liczba.value) || (liczba.value == null) || (liczba.value == "")) {
        document.getElementById("wynik2").innerHTML = "Wprowadź liczbę";
        return
    }

    if ((liczba.value % 2 == 0) || (liczba.value <= 1))  {
        document.getElementById("wynik2").innerHTML = `Liczba ${liczba.value} nie jest liczbą pierwszą`;
    }
    else if (liczba.value > 1) {
        let jestPierwsza = true;
        for (let i = 2; i < liczba.value; i++) {
            if (liczba.value % i == 0) {
                jestPierwsza = false;
                break;
            }
        }
        if (jestPierwsza) {
            document.getElementById("wynik2").innerHTML = `Liczba ${liczba.value} jest liczbą pierwszą`;
        }
        else {
            document.getElementById("wynik2").innerHTML = `Liczba ${liczba.value} nie jest liczbą pierwszą`;
        }
    }
    else {
        document.getElementById("wynik2").innerHTML = `Liczba ${liczba.value} nie jest liczbą pierwszą`;
    }
    return
}

function Dane() {
    const imie = document.getElementById("Imie2").value;
    const nazwisko = document.getElementById("Nazwisko2").value;
    let pesel = document.getElementById("Pesel").value;

    if (pesel.length != 11) {
        document.getElementById("wynik3").innerHTML = "Pesel musi mieć 11 cyfr!";
        return
    }
    
    pesel = Array.from(pesel.toString()).map(Number);

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
        default:
            alert("Pesel jest niepoprawny!");
            break;
    }


    const dzien = `${pesel[4]}${pesel[5]}`; //na 100% jest inny sposób by połączyć te dwa obiekty bez ich dodawania do siebie ale js to ustrojstwo
    const data = new Date(rok,miesiac,dzien); //układamy sobie tutaj datę w kolejności rok-miesiąc-dzień
    const dzisiejszaData = new Date();
    const Roznica = Math.floor(((dzisiejszaData - data) / (1000 * 60 * 60 * 24)) / 365); // Robimy różnice dwóch dwat po czym przekształcamy w kolejności (ms -> s -> min -> h -> d -> y)

    alert(imie + ", " + nazwisko + ", " + Roznica + " lat"); 
}

function Data() {
    const dzisiejszaData = new Date();
    const przyszlaData = new Date(document.getElementById("przyszlaData").value);
    const Roznica = przyszlaData - dzisiejszaData;

    document.getElementById("wynik4").innerHTML = `<br>Rożnica sekund: ${Math.floor(Roznica / 1000)} <br>Różnica minut: ${Math.floor(Roznica / (1000 * 60))} <br>Roznica dni: ${Math.floor(Roznica / (1000 * 3600 * 24))}`;
}