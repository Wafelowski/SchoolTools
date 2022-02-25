temp = input("Co chcesz sprawdzić? \n1 - Palindrom \n2 - Anagram \n\n")

while (temp != "1") and (temp != "2"):
    temp = input("------\nCo chcesz sprawdzić? \n1 - Palindrom \n2 - Anagram \n\n")

if temp == "1":
    word = input("Podaj słowo: ")

    if word == word[::-1]:
        print("Słowo jest palindromem.")
    else:
        print("Słowo nie jest palindromem.")


if temp == "2":
    word1 = input("Podaj pierwsze słowo: ")
    word2 = input("Podaj drugie słowo: ")

    if word1 == word2:
        print("Słowa są takie same.")
        exit
    elif (word1 == None) or (word1 == "") or (word2 == None) or (word2 == ""):
        print("Nie podano poprawnych słów.")
        exit

    if len(word1) != len(word2):
        print("Słowa nie sa tej samej długości. Anagramy tego wymagają.")
    else:
        word1 = sorted(word1)
        word2 = sorted(word2)

        if word1 != word2:
            print("Slowa nie sa anagramami.")
        else:
            print("Slowa sa anagramami.")