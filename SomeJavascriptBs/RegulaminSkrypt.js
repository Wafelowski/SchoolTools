function Resetuj() {
    let imie = document.getElementById("imie");
    let nazwisko = document.getElementById("nazwisko");
    let email = document.getElementById("email");
    let usluga = document.getElementById("usluga");
    let regulamin = document.getElementById("regulamin");

    let odpowiedz = document.getElementById("odpowiedz");

    imie.value = "";
    nazwisko.value = "";
    email.value = "";
    usluga.value = "";
    regulamin.checked = false;
    odpowiedz.innerHTML = "";
}

function Przeslij() {
    let imie = document.getElementById("imie").value;
    let nazwisko = document.getElementById("nazwisko").value;
    let email = document.getElementById("email").value;
    let usluga = document.getElementById("usluga").value;
    let regulamin = document.getElementById("regulamin");

    let odpowiedz = document.getElementById("odpowiedz");

    odpowiedz.innerHTML = "";

    if (imie == "" || nazwisko == "" || email == "" || usluga == "") {
        odpowiedz.innerHTML = "Uzupełnij wszystkie pola.";
        return;
    }

    if (regulamin.checked == false) {
        odpowiedz.innerHTML = "Musisz zapoznać się z regulaminem.";
        odpowiedz.style.color = "red";
        return;
    }

    odpowiedz.style.color = "black";
    odpowiedz.innerHTML = `${imie.toUpperCase()} ${nazwisko.toUpperCase()} <br/>Treść twojej sprawy: ${usluga} <br/>Na podany adres e-mail zostanie wysłana oferta.`;
}
