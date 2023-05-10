import os
import time
from PIL import Image

if not os.path.exists("modified"):
    os.makedirs("modified")

directory = os.getcwd()
folders = []
def listdirs(folder):
    for file in os.listdir(folder):
        d = os.path.join(folder, file)
        if os.path.isdir(d):
            folders.append(d)
            listdirs(d)

folder = os.getcwd()
listdirs(os.getcwd())

files = []
for folder in folders:
    current = []
    for file in os.listdir(folder):
        d = os.path.join(folder, file)
        if os.path.isfile(d):
            current.append(d)

    if current != []:
        files.append(current)


def count_items(nested_list):
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

count = count_items(files)
files = flatten_list(files)
print(f"Lista Plików ({count}):")
for file in files:
    print(file)

temp = input(f"Czy lista plików {count} się zgadza? (t/n): ")
if temp.lower() != "t":
    print("\nPamietaj ze program wyszukuje pliki w folderze z plikiem wykonywalnym!")
    print("Anuluje...")
    time.sleep(5)
    exit()

size = input("Podaj wybrana dlugosc dluzszej strony: ")
if size.isdigit() == False:
    print("To nie jest liczba!")
    exit()
size = int(size)
if int(size) < 1:
    print("Podana liczba jest mniejsza od 1!")
    exit()


for file in files:
    if (file.lower().endswith(".jpeg") or file.lower().endswith(".jpg") or file.lower().endswith(".png")):
        print(f"Obraz - {file}")
        img = Image.open(f"{file}")
        width, height = img.size
        print(f"Stare rozmiary - {img.size}")
        if width >= height:
            longer = "width"
        else:
            longer = "height"
        if longer == "width":
            xx = width / size
            height = height / xx
            width = width / xx
        elif longer == "height":
            xx = height / size
            height = height / xx
            width = width / xx
        
        dir_path, file_name = os.path.split(file)
        dir_path = dir_path.replace(f"{directory}", f"{directory}\\modified")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_name = file.replace(f"{directory}", f"{directory}\\modified")
        img = img.resize((round(width), round(height)), Image.ANTIALIAS)
        img.save(f"{file_name}")
        img2 = Image.open(f"{file_name}")
        print(f"Dluzsza strona - {longer}")
        print(f"Nowe rozmiary: {img2.size}")
        print("------------------")

