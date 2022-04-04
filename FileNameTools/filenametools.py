import os
import time
from datetime import datetime

results_path = "./results/"
pause = input("Podaj tryb programu. \n1 - Zrób listę plików w .txt \n2 - Zmień masowo nazwę. \n\nWybór: ")
path = input("Podaj ścieżkę do folderu z obrazkami. \nŚcieżka musi uwzględniać również dysk! Na przykład: C:\\Users\\User\\Desktop\\ \n\n")

if pause == "1": # Zrób listę plików w .txt
    files = os.listdir(path) # get the list of files in the folder
    list = ""

    temp = input("Czy lista ma zawierać rozszerzenia plików? \n1 - Tak \n2 - Nie \n\nWybór: ")
    if temp == "1":
        for x in files:
            print(f"Zapisuję: {x}")
            list = list + x + "\n"
        print("Lista: ----------" + list + "----------\n")
    if temp == "2":
        for x in files:
            x = os.path.splitext(x)[0]
            print(f"Zapisuję: {x}")
            list = list + x + "\n"
        print(f"Lista ({len(list)}): ----------" + list + "----------\n")
    
    temp = input("Czy lista plików się zgadza? (t/n): ")
    if temp.lower() != "t":
        print("Zakończono program.")
        time.sleep(2)
        exit()

    now = datetime.now()
    date = now.strftime("%m-%d-%Y %H-%M-%S")
    with open(f"results/list - {date}.txt", "w") as file: 
        file.write(list)

if pause == "2":
    print("Work in progress...")