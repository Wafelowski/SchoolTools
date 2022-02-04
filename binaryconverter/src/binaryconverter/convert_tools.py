import re

class Tools():
    def Convert(self, number, number_type, mode):
        print(f"Konwertowanie {number} z {number_type.upper()} na {mode.upper()}")
        if number_type == mode:
            self.main_window.info_dialog(
                    'Błąd!',
                    'Co próbujesz osiągnąć w ten sposób?'
                )
            return False
        if number_type == "binarny":
            if not re.fullmatch('[01]+$', number):
                self.main_window.info_dialog(
                        'Błąd!',
                        'Wprowadzona liczba nie jest binarną!'
                    )
                return False
            if mode == "szesnastkowy":
                x = '%0*X' % ((len(number) + 3) // 4, int(number, 2))
                return " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            elif mode == "dziesiętny":
                x = int(number, 2)
                x = str(x)
                return " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            elif mode == "ósemkowy":
                x = oct(int(number, 2))[2::] # Zmieniamy na dziesiętny i konwertujemy na ósemkowy
                return " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
        elif number_type == "ósemkowy":
            if not re.fullmatch('[0-7]+$', number):
                self.main_window.info_dialog(
                        'Błąd!',
                        'Wprowadzona liczba nie jest ósemkowa!'
                    )
                return False
            if mode == "szesnastkowy":
                number = int(number, 8) # Zmieniamy na dziesiętny i konwertujemy na szesnastkowy
                x = hex(number)[2::].upper()
                return " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
            elif mode == "dziesiętny":
                x = int(number, 8)
                x = str(x)
                return " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            elif mode == "binarny":
                x = int(number, 8) # Zmieniamy na dziesiętny, i dopiero na binarny
                x = "{0:b}".format(x)
                return " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
        elif number_type == "dziesiętny":
            if not re.fullmatch('[0-9]+$', number):
                self.main_window.info_dialog(
                        'Błąd!',
                        'Wprowadzona liczba nie jest dziesiętna!'
                    )
                return False
            if mode == "szesnastkowy":
                number = int(number)
                x = hex(number)[2::].upper()
                return " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
            elif mode == "ósemkowy":
                x = oct(int(number))[2::] # Korzystamy z funkcji oct i usuwamy dwa pierwsze znaki
                return " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            elif mode == "binarny":
                x = int(number)
                # lub możemy użyć bin(x) ale po co, maszyna wytrzyma
                x = "{0:b}".format(x)
                return " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
        elif number_type == "szesnastkowy":
            if not re.fullmatch('[A-F0-9]+$', number):
                self.main_window.info_dialog(
                        'Błąd!',
                        'Wprowadzona wartość nie jest szesnastkowa!'
                    )
                return False
            if mode == "dziesiętny":
                x = int(number, 16)
                x = str(x)
                return " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            elif mode == "ósemkowy":
                x = oct(int(number, 16))[2::] # Korzystamy z funkcji oct i usuwamy dwa pierwsze znaki
                return " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            elif mode == "binarny":
                x = int(number, 16)
                # lub możemy użyć bin(x) ale po co v2
                temp = ''
                while x > 0:
                    temp = str(x % 2) + temp
                    x = x >> 1    
                x = temp
                return " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
        else:
            self.main_window.info_dialog(
                        'Błąd!',
                        'Wystąpił nieoczekiwany błąd, zamykanie pgoramu!'
                    )
            exit()

    def TypeCheck(self, number):
        if re.fullmatch('[0-1]+$', number):
            return "binarna"
        elif re.fullmatch('[0-7]+$', number):
            return "ósemkowa"
        elif re.fullmatch('[0-9]+$', number):
            return "dziesiętna"
        elif re.fullmatch('[A-F0-9]+$', number):
            return "szesnastkowa"
        else:
            self.main_window.info_dialog(
                'Błąd!',
                'Wprowadzona wartość nie jest binarna, dziesiętna, ósemkowa lub szesnastkowa!'
            )
            return False