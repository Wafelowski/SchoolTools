
monety = input("Podaj posiadane monety, dzieląc je przecinkiem: ")
monety = monety.replace(" ", "")
monety = monety.split(",")
monety = list(map(int, monety))

ilosc = len(monety)
reszta = int(input("Jaką reszte chcesz wydać? "))

licznik = 0
historia = []

while reszta > 0:
    if licznik >= ilosc:
        print("Nie udało się wydać pełnej reszty. Można wydać tylko " + str(sum(monety)) + " zł.")
        exit()
    else:
        nominal = 0
        for i in range(ilosc):
            if (monety[i] <= reszta) and (monety[i] > nominal):
                nominal = monety[i]
        reszta = reszta - nominal
        historia.append(nominal)
        licznik += 1

historia = str(historia).replace("[", "").replace("]", "")
if licznik != 1:
    print("Użyto " + str(licznik) + " monet(y): " + str(historia))
else:
    print("Resztę można wydać monetą: " + str(historia) + " zł")





############################
# Wersja 1:1 do wersji C++ #
############################

# ilosc = 3
# monety = [1, 2, 5]
# reszta = int(input("Jaka reszte chcesz wydac? "))

# licznik = 0
# historia = []

# while reszta > 0:
#     nominal = 0
#     for i in range(ilosc):
#         if (monety[i] <= reszta) and (monety[i] > nominal):
#             nominal = monety[i]
#     reszta = reszta - nominal
#     historia.append(nominal)
#     licznik += 1

# print("Resztę mozna wydać " + str(licznik) + " monetami")
# print("Użyte monety: " + str(historia))

