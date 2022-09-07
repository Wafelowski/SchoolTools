import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

pause = input("Podaj tryb programu. \n1 - Pobieranie plikow \n2 - Pakowanie w PDF. \n\nWybór: ")

if str(pause) == "1":
    s=Service(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument(r"--user-data-dir=C:\Users\Wafel\AppData\Local\Google\Chrome\User Data") 
    #chrome_options.add_argument("--user-data-dir=C:\Users\Wafel\AppData\Local\Google\Chrome\User Data") 



    driver = webdriver.Chrome(service=s, options=chrome_options)

    driver.split()

    #driver.get("https://app.wsipnet.pl/e-podreczniki/podglad/534/index.html")
    driver.get("https://www.wsipnet.pl")
    time.sleep(5)
    print(driver.title)

    pause = input("Kliknij Enter by wcisnac przycisk \"Zaloguj\"...")

    buttons = driver.find_element(By.XPATH, "//*[contains(text(), 'Zaloguj się')]")
    print(buttons)

    buttons.click()
    print("Kliknieto przycisk \"Zaloguj się\"")

    time.sleep(2)
    print("Przystępuje do próby zalogowania przez Google.")
    buttons = driver.find_element(By.XPATH, '//*[@title="Google"]')

    buttons.click()
    print("Kliknieto przycisk \"Google\"")
    time.sleep(5)
    print(driver.title)

    pause = input("Kliknij Enter by przejsc do podrecznika...")

    driver.get("https://app.wsipnet.pl/e-podreczniki/podglad/534/index.html")
    print(driver.title)

    pause = input("Kliknij Enter by rozpoczac pobieranie plikow...")

    for x in range(285, 363):
        driver.get(f"https://app.wsipnet.pl/e-podreczniki/podglad/534/files/mobile/{x}.jpg?210710212023")
        print(f'Obrazek {x} - {driver.title}')
        html = driver.page_source
        #print(html)
        driver.save_screenshot(f"C:/Programowanie/Projekty/Python/WsipDownloader/images/{x}.png")
        print(f'Zapisano obrazek {x} z url {driver.title}')

    pause = input("Kliknij Enter by zakonczyc program...")

    print("Done")

if str(pause) == "2":
    import glob
    import img2pdf
    imgList = os.listdir('C:/Programowanie/Projekty/Python/WsipDownloader/images/')
    #lsorted = sorted(imgList, key=lambda x: int(os.path.splitext(x)[0]))
    import re
    def numericalSort(value):
        numbers = re.compile(r'(\d+)')
        parts = numbers.split(value)
        parts[1::2] = map(int, parts[1::2])
        return parts
    lsorted=sorted(glob.glob('C:/Programowanie/Projekty/Python/WsipDownloader/images/*.png'), key=numericalSort)
    print(lsorted)
    with open("Fizyka.pdf","wb") as f:
        f.write(img2pdf.convert(lsorted))
        #f.write(img2pdf.convert(glob.glob("C:/Programowanie/Projekty/Python/WsipDownloader/images/*.png")))