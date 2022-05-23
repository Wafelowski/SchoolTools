// Polecam https://wafelowski.pl/good_luck/

// ╔══════════════╦══════════════════════════════════════╗
// ║ Jakość hasła ║                 Opis                 ║
// ╠══════════════╬══════════════════════════════════════╣
// ║ dobre        ║ 7+ znaków, przynajmniej jedna cyfra  ║
// ║ średnie      ║ 4-6 znaków, przynajmniej jedna cyfra ║
// ║ słabe        ║ gorsze przypadki                     ║
// ╚══════════════╩══════════════════════════════════════╝

// "HASŁO JEST PUSTE" czcionką w kolorze czerwonym, jeśli pole jest puste
// "HASŁO JEST SŁABE" czcionką w kolorze żółtym, jeśli hasło spełnia warunki słabego
// "HASŁO JEST ŚREDNIE" czcionką w kolorze niebieskim, jeśli hasło spełnia warunki średniego
// "HASŁO JEST DOBRE" czcionką koloru zielonego, jeśli hasło spełnia warunki hasła dobrego


// Jaka jest najlepsza opcja na ustalenie jakości hasła?
// Mamy dwie opcje:
// 1. Długość, a następnie sprawdzenie pozostałych warunków
// 2. Robimy pełny regex (warto wiedzieć czym jest regex by nie było przypału)

function SprawdzHaslo() {
    let haslo = document.getElementById("haslo");
    let komunikat = document.getElementById("komunikat");
    
    komunikat.innerHTML == ""; //Wyczyśćmy poprzedni wynik.

    var cyfra = false
    for (znak of haslo.value) {
        znak = Number.parseInt(znak); // Wszystko co wpisujemy w formularzu zawsze będzie stringiem, dlatego zamienimy to na liczbę. 
        // W javascripcie skrypt się nie klepnie na plecy, jeśli to będzie litera.
        if (Number.isInteger(znak))
            cyfra = true
    }

    if ((haslo.value.length >= 7) && (cyfra)) {
        komunikat.innerHTML = "HASŁO JEST DOBRE";
        komunikat.style.color = "green";
        return;
    }
    else if ((haslo.value.length >= 4) && (haslo.value.length <= 6) && (cyfra)) {
        komunikat.innerHTML = "HASŁO JEST ŚREDNIE";
        komunikat.style.color = "blue";
        return;
    }
    else if (haslo.value.length > 0) {
        komunikat.innerHTML = "HASŁO JEST SŁABE";
        komunikat.style.color = "red";
        return;
    }
    else {
        
        komunikat.innerHTML = "HASŁO JEST PUSTE";
        komunikat.style.color = "red";
    }
}

function SprawdzHasloRegex1() {
    let haslo = document.getElementById("haslo");
    let komunikat1 = document.getElementById("komunikat1");
    
    komunikat1.innerHTML == ""; //Wyczyśćmy poprzedni wynik.

    switch (true) { // Można również użyć if'ów
        case haslo.value.length <= 0: 
            komunikat1.innerHTML = "HASŁO JEST PUSTE";
            komunikat1.style.color = "red";
            break;
        case haslo.value.length >= 4 && haslo.value.length <= 6 && /\d/.test(haslo.value):
            komunikat1.innerHTML = "HASŁO JEST ŚREDNIE";
            komunikat1.style.color = "blue";
            break;
        case haslo.value.length >= 7 && /\d/.test(haslo.value):
            komunikat1.innerHTML = "HASŁO JEST DOBRE";
            komunikat1.style.color = "green";
            break;
        default:
            komunikat1.innerHTML = "HASŁO JEST SŁABE";
            komunikat1.style.color = "yellow";
            break
    }
    
}

function SprawdzHasloRegex2() {
    let haslo = document.getElementById("haslo");
    let komunikat = document.getElementById("komunikat2");
    
    komunikat2.innerHTML == ""; //Wyczyśćmy poprzedni wynik.

    switch (true) { // Można również użyć if'ów
        case haslo.value.length <= 0:
            komunikat2.innerHTML = "HASŁO JEST PUSTE";
            komunikat2.style.color = "red";
            break;
        case /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{4,6}$/.test(haslo.value):
            komunikat2.innerHTML = "HASŁO JEST ŚREDNIE";
            komunikat2.style.color = "blue";
            break;
        case /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{7,}$/.test(haslo.value):
            komunikat2.innerHTML = "HASŁO JEST DOBRE";
            komunikat2.style.color = "green";
            break;
        default:
            komunikat2.innerHTML = "HASŁO JEST SŁABE";
            komunikat2.style.color = "yellow";
            break
    }
    
}


// Wytłumaczenie regexa w tej sytuacji
// /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{4,6}$/
// /.../ to otwarcie i zakończenie regexa. 

// ^ i $ zamyka nam stringa, czyli upewnia się że całe hasło spełnia warunki.
// Przykład, string "сука_KEKW_блять", przy regexie "/[a-zA-Z]/" spełni warunki tylko "KEKW", czego nie chcemy jeśli nasze hasło ma mieć tylko akceptowalne znaki QWERTY.

// Sekcje (?=...) oznaczają warunki, jakie regex musi mieć, niezależnie od kolejności ich wpisania do regexu.

// "." to obojętnie jaki znak (ASCII), "*" to chociaż jedna sztuka poprzedniego symbolu. 
// W tym przypadku oznacza to, że możemy wpisać liczbę przed literami i na odwrót.

// [A-Za-z] za nim upewni się, że pomimo wpisania czegokolwiek, podaliśmy chociaż jedną literę alfabetu.
// To samo z \d, które oznacza cyfrę.

// Następnie podajemy całą składnię jaką musi zawierać regex
// {#,#} oznacza liczbę znaków. Jeśli podamy tylko jedną cyfrę bez przecinka to wymagamy wtedy równo # znaków.
// Przecinek po pierwszej cyfrze wyznacza minimalną liczbę znaków.
// Podanie drugiej cyfry przed przecinkiem wyznacza maksymalną liczbę znaków. (nawet jeśli pierwszej cyfry nie ma, np. {,3})

// Metoda .test zwróci nam true/false w zależności czy string ją spełnia.