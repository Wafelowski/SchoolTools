import os
import time
from PIL import Image

original_path = "./original/"
modified_path = "./modified/"
if os.path.exists(original_path) == False:
    os.mkdir(original_path)
if os.path.exists(modified_path) == False:
    os.mkdir(modified_path)

original = os.listdir(original_path) # get the list of files in folder with unchanged (original) images
print(f"Lista Plików ({len(original)}): \n{original}\n")

temp = input("Czy lista plików się zgadza? (t/n): ")
if temp.lower() != "t":
    print("\nPamietaj ze program wyszukuje pliki w folderze original, ktory znajduje sie w tym samym folderze co plik wykonywalny!")
    print("Anuluje...")
    time.sleep(10)
    exit()

size = input("Podaj wybrana dlugosc dluzszej strony: ")
if size.isdigit() == False:
    print("To nie jest liczba!")
    exit()
size = int(size)
if int(size) < 1:
    print("Podana liczba jest mniejsza od 1!")
    exit()

for x in original:
    if (x.endswith(".jpeg") or x.endswith(".jpg") or x.endswith(".png")):
        print(f"Obraz - {x}")
        img = Image.open(f"{original_path}/{x}")
        width, height = img.size
        print(f"Stare rozmiary - {img.size}")
        if width >= height:
            longer = "width"
        else:
            longer = "height"
        if longer == "width":
            xx = width / size
            # print(xx)
            height = height / xx
            width = width / xx
            # print(height)
            # print(width)
        elif longer == "height":
            xx = height / size
            # print(xx)
            height = height / xx
            width = width / xx
            # print(height)
            # print(width)
        img = img.resize((round(width), round(height)), Image.ANTIALIAS)
        img.save(f"{modified_path}/{x}")
        img2 = Image.open(f"{modified_path}/{x}")
        print(f"Dluzsza strona - {longer}")
        print(f"Nowe rozmiary: {img2.size}")
        print("------------------")

