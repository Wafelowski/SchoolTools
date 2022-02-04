"""
Projekcik
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import tabulate
from .convert_tools import Tools

class BinaryConverter(toga.App):

    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        number_label = toga.Label(
            'Liczba do zmiany: ',
            style=Pack(padding=(5, 0, 0, 5))
        )
        self.used = False
        self.number_input = toga.TextInput(placeholder='Podaj wartość', on_change=self.convert,style=Pack(flex=1, padding=5))

        number_box = toga.Box(style=Pack(direction=ROW, padding=5))
        number_box.add(number_label)
        number_box.add(self.number_input)
        self.main_box.add(number_box)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(500, 500))
        self.main_window.content = self.main_box
        self.main_window.show()

    def convert(self, widget):
        number = self.number_input.value
        if len(self.main_box.children) > 1:
            self.main_box.remove(self.main_box.children[1])
        if number == "":
            print("Textbox empty")
            return
        number = str(number).replace(" ", "")
        number = number.replace(" ", "") # Invisible character, used by Windows calculator
        number_type = Tools.TypeCheck(self, number)
        if number_type == False:
            number_type = "Błąd!"
        else:
            number_type = "Jest to liczba %s" % number_type

        result_box = toga.Box(style=Pack(direction=COLUMN, padding=5, alignment=CENTER))
        type_label = toga.Label(
            number_type,
            style=Pack(font_weight="bold", font_size=10, padding_bottom=10)
        )

        result = Tools.Convert(self, number)
        if result == False:
            string = "Wprowadzona wartość nie jest binarna, dziesiętna, ósemkowa lub szesnastkowa!"
        else:
            string = tabulate.tabulate([["Typ", "Liczba"], ["Binarny", result[0]], ["Ósemkowy", result[1]], ["Dziesiętny", result[2]], ["Szesnastkowy", result[3]], ["============", "============"]], headers="firstrow") #, tablefmt="github")
        print(string)
        result_label = toga.Label(
            #"%s -> %s \n%s -> %s" % (number, result, number_type, mode),
            string,
            style=Pack(font_weight="bold", font_size=10)
        )

        result_box.add(type_label)
        result_box.add(result_label)
        self.main_box.add(result_box)
        self.used = True


def main():
    return BinaryConverter()
