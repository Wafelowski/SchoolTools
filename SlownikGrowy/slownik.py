from asyncore import write
from datetime import datetime
import mmap

# Text file from https://sjp.pl/slownik/growy/

alf = {
    "a": "1",
    "ą": "2",
    "b": "3",
    "c": "1",
    "ć": "3",
    "d": "3",
    "e": "1",
    "ę": "2",
    "f": "4",
    "g": "2",
    "h": "3",
    "i": "3",
    "j": "2",
    "k": "3",
    "l": "3",
    "ł": "3",
    "m": "1",
    "n": "1",
    "ń": "3",
    "o": "1",
    "ó": "3",
    "p": "2",
    "q": "2",
    "r": "1",
    "s": "1",
    "ś": "3",
    "t": "3",
    "u": "1",
    "v": "1",
    "w": "1",
    "x": "1",
    "y": "2",
    "z": "1",
    "ź": "3",
    "ż": "3",
}

slownik = {}
for dlugosc in range (5,16):
    slownik[dlugosc] = {}

first = datetime.now()
print(f"First checkpoint - {first}")

with open('slowa.txt', "r+b") as wfile, mmap.mmap(wfile.fileno(), 0, access=mmap.ACCESS_READ) as s:
    a = "."
    while a:
        a = s.readline().decode("utf-8")
        a = a.replace('\r', '').replace('\n', '')
        if (len(a)) < 5:
            continue
            
        code = ""
        for letter in a:
            code += alf[letter]
        if not (code in slownik[len(a)]):
            slownik[len(a)][code] = []
        slownik[len(a)][code].append(a)

second = datetime.now()
print(f"Second checkpoint - {second}")

with open("slowa-result.txt", "w") as file:
    print(str(slownik), file=file)

third = datetime.now()
print(f"Third checkpoint - {third}")

print(slownik)

final = datetime.now()
difference = final - first
print(f"\n-----------\nFirst -{first}, \nSecond - {second}, \nThird - {third}, \nFinal - {final}\nDifference - {difference}\n-----------")

input("Kliknij Enter by zakonczyc program.")