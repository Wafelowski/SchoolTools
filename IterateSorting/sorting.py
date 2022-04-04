from dataclasses import dataclass
import string


@dataclass
class Student:
    nazwisko: str
    srednia: float
    
studenci = [
    Student("Kowalski",  3.12),
    Student("Kasprowicz",  4.40),
    Student("Nowak",    6.00),
    Student("Kosak",    5.44),
    Student("Nasiadka",  5.32),
    Student("Nowicki",    3.44),
    Student("Kanigowski",  4.00),
    Student("Danusiak",  4.00),
    Student("Dworznik",  4.20),
    Student("Kaspro",    3.00),
    Student("Kasprowicz",  4.00),
    Student("Kasprowicz",  3.10),
    Student("Danusiak",  2.00),
    Student("Danusiak",  2.14)
    ]

sorted = studenci.sort(key=lambda student: student.nazwisko + str(student.srednia))

for student in studenci:
    print(student.nazwisko, student.srednia)
