"""
Projekcik
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import tabulate
from .convert_tools import Tools

class BinaryConverter(toga.App):

    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        number_type_box = toga.Box(style=Pack(direction=ROW, padding=5))
        number_type_label = toga.Label(
            'Konwertuj z: ',
            style=Pack(padding=(5, 0, 0, 5))
        )
        self.number_type_selection = toga.Selection(items=['binarny', 'ósemkowy', 'dziesiętny', 'szesnastkowy'], style=Pack(direction=ROW, width=120, padding=(2, 0, 0, 6)))

        number_type_box.add(number_type_label)
        number_type_box.add(self.number_type_selection)
        help_button = toga.Button(
            'Jaki to typ?',
            on_press=self.help_button_func,
            style=Pack(padding_left=50, width=120)
        )
        number_type_box.add(help_button)
        self.main_box.add(number_type_box)

        mode_box = toga.Box(style=Pack(direction=ROW, padding=5))
        mode_label = toga.Label(
            'Konwertuj na: ',
            style=Pack(padding=(5, 0, 0, 5))
        )
        self.mode_selection = toga.Selection(items=['binarny', 'ósemkowy', 'dziesiętny', 'szesnastkowy'], style=Pack(direction=ROW, width=120, padding=(2, 0, 0, 0)))

        mode_box.add(mode_label)
        mode_box.add(self.mode_selection)
        self.main_box.add(mode_box)

        number_label = toga.Label(
            'Liczba do zmiany: ',
            style=Pack(padding=(5, 0, 0, 5))
        )
        self.number_input = toga.TextInput(style=Pack(flex=1, padding=(2, 0, 0, 0)))

        number_box = toga.Box(style=Pack(direction=ROW, padding=5))
        number_box.add(number_label)
        number_box.add(self.number_input)

        convert_button = toga.Button(
            'Przekonwertuj!',
            on_press=self.convert_button_func,
            style=Pack(padding=5)
        )
    
        self.main_box.add(number_box)
        self.main_box.add(convert_button)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(400, 400), resizeable=False)
        self.main_window.content = self.main_box
        self.main_window.show()

    #def convert(self, number, mode, number_type):
    def convert_button_func(self, widget):
        number = self.number_input.value
        mode = self.mode_selection.value
        number_type = self.number_type_selection.value
        if number == "":
            self.main_window.info_dialog(
                'Błąd!',
                'Musisz podać liczbę do przemiany!'
            )
            return
        number = str(number).replace(" ", "")
        number = number.replace(" ", "") # Invisible character, used by Windows calculator
        result = Tools.Convert(self, number, number_type, mode)
        if result == False:
            return
        result_box = toga.Box(style=Pack(direction=ROW, padding=5))
        string = tabulate.tabulate([[number_type, number],[mode, result], ["============", "============"]], headers="firstrow") #, tablefmt="github")
        print(string)
        result_label = toga.Label(
            #"%s -> %s \n%s -> %s" % (number, result, number_type, mode),
            string,
            style=Pack(font_weight="bold", font_size=10)
        )
        result_box.remove(result_label)
        result_box.add(result_label)
        self.main_box.add(result_box)

    def help_button_func(self, widget):
        number = self.number_input.value
        if number == "":
            self.main_window.info_dialog(
                'Błąd!',
                'Musisz podać liczbę do rozpoznania!'
            )
            return
        number = str(number).replace(" ", "")
        number = number.replace(" ", "") # Invisible character, used by Windows calculator
        number_type = Tools.TypeCheck(self, number.upper())
        if number_type == False:
            return
        self.main_window.info_dialog(
            'Rozpoznano wartość',
            'Jest to liczba %s.' % number_type
        )
        return


def main():
    return BinaryConverter()
