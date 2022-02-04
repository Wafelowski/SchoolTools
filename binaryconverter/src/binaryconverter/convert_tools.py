import re

class Tools():
    def Convert(self, number):
        number_type = Tools.TypeCheck(self, number)
        if number_type == False:
            return False
        print(f"Konwertowanie {number_type.upper()}: {number}")
        if number_type == "binarna":
            binarna = number
            # Liczba szesnastkowa
            x = '%0*X' % ((len(number) + 3) // 4, int(number, 2))
            szesnastkowa = " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]

            # Liczba dziesiętna
            x = int(number, 2)
            x = str(x)
            dziesietna = " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]

            # Liczba ósemkowa
            x = oct(int(number, 2))[2::] # Zmieniamy na dziesiętna i konwertujemy na ósemkowa
            osemkowa =  " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            return [binarna, osemkowa, dziesietna, szesnastkowa]

        elif number_type == "ósemkowa":
            osemkowa = number
            # Liczba szesnastkowa
            number = int(number, 8) # Zmieniamy na dziesiętna i konwertujemy na szesnastkowy
            x = hex(number)[2::].upper()
            szesnastkowa = " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
            print("31 works")

            # Liczba dziesiętna
            x = str(number)
            dziesietna = " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            print("36 works")

            # Liczba binarna
            x = "{0:b}".format(number)
            binarna = " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
            print("43 works")
            return [binarna, osemkowa, dziesietna, szesnastkowa]

        elif number_type == "dziesiętna":
            dziesietna = number
            # Liczba szesnastkowa
            number = int(number)
            x = hex(number)[2::].upper()
            szesnastkowa = " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]

            # Liczba ósemkowa
            x = oct(int(number))[2::] # Korzystamy z funkcji oct i usuwamy dwa pierwsze znaki
            osemkowa = " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]
            
            # Liczba binarna
            x = int(number)
            # lub możemy użyć bin(x) ale po co, maszyna wytrzyma
            x = "{0:b}".format(x)
            binarna = " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
            return [binarna, osemkowa, dziesietna, szesnastkowa]

        elif number_type == "szesnastkowa":
            szesnastkowa = number
            # Liczba dziesiętna
            x = int(number, 16)
            x = str(x)
            dziesietna = " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]

            # Liczba ósemkowa
            x = oct(int(number, 16))[2::] # Korzystamy z funkcji oct i usuwamy dwa pierwsze znaki
            osemkowa = " ".join([x[::-1][i:i+3] for i in range(0, len(x), 3)])[::-1]

            # Liczba binarna
            x = int(number, 16)
            # lub możemy użyć bin(x) ale po co v2
            temp = ''
            while x > 0:
                temp = str(x % 2) + temp
                x = x >> 1    
            x = temp
            binarna = " ".join([x[::-1][i:i+4] for i in range(0, len(x), 4)])[::-1]
            return [binarna, osemkowa, dziesietna, szesnastkowa]

        else:
            self.main_window.info_dialog(
                        'Błąd!',
                        'Wystąpił nieoczekiwany błąd, zamykanie programu!'
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
            return False