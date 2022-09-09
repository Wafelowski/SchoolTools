import os
import time
from io import BytesIO
from PIL import Image

import img2pdf, re, json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

pause = input("Podaj tryb programu. \n1 - Pobieranie plikow \n2 - Pakowanie w PDF. \n\nWybór: ")

if str(pause) == "1":
    with open("ebook-config.json", "r") as config: 
        data = json.load(config)
        email = data["oficynaEmail"]
        password = data["oficynaPassword"]
    
    s=Service(ChromeDriverManager().install())
    pause = input("\nPotwierdz pobranie sterownika.")

    chrome_options = Options()
    chrome_options.add_argument(r"--user-data-dir=C:\Users\Wafel\AppData\Local\Google\Chrome\User Data") 
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=s, options=chrome_options)

    driver.get("https://ebook.pazdro.com.pl/auth/login")
    time.sleep(2)

    pause = input("Kliknij Enter by przejść do logowania.")

    button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/section/div[2]/div/div[1]")
    button.click()

    textbox = driver.find_element(By.XPATH, "/html/body/div/div/main/div/section/div[1]/div[2]/form/div[1]/div[2]/input")
    textbox.send_keys(email)

    textbox = driver.find_element(By.XPATH, "/html/body/div/div/main/div/section/div[1]/div[2]/form/div[2]/div[2]/input")
    textbox.send_keys(password)

    button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/section/div[1]/div[2]/form/div[3]/button")
    button.click()

    time.sleep(5)
    while driver.current_url != "https://ebook.pazdro.com.pl/app":
        time.sleep(2)

    # W tym miejscu wklej XPATH do książki. Jak to zrobić?
    # 1. Kliknij prawym na tytuł książki
    # 2. Zbadaj element
    # 3. Znajdź linijkę zaczynającą się od tagu <a> z parametrem "href"
    # 4. Kliknij na nią prawym
    # 5. Copy -> Full XPATH

    button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/a")
    button.click()

    time.sleep(2)

    button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/article/div/div/div[2]/div[2]/div[1]/button")
    button.click()

    print(f"{driver.title} - {driver.current_url}")

    pause = input("Kliknij Enter by rozpoczac pobieranie plikow, jak książka się załaduje...")

    for x in range(1, 259):
        
        current_page2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div[1]/div[2]/input')
        current_page = int(current_page2.get_attribute("value"))
        time.sleep(3)

        both = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div')

        location = both.location
        size = both.size
        png = driver.get_screenshot_as_png() # saves screenshot of entire page
        im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
        # credits to https://stackoverflow.com/a/15870708 

        left = location['x']
        left = int(left)+280
        top = location['y']
        right = location['x'] + int(size['width'])-300
        bottom = location['y'] + size['height']


        im = im.crop((left, top, right, bottom)) # defines crop points
        if current_page == 1:
            im.save(f'strony/oficyna/Strona {int(current_page)}.png')
            print(f'Zapisano obrazek ze strony {current_page}, url {driver.current_url} \n')
            next_button = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/button')
        else:
            im.save(f'strony/oficyna/Strony {int(current_page)-1} - {int(current_page)}.png')
            print(f'Zapisano obrazek ze strony {int(current_page)-1} - {current_page}, url {driver.current_url} \n')
            next_button = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/button[2]')
        
        if current_page != 515:
            next_button.click()
        time.sleep(2)
        
    pause = input("Kliknij Enter by zakonczyc program...")

    print("Done")

if str(pause) == "2":
    imgList = os.listdir('./strony/oficyna/')
    print(imgList)
    
    imgList.sort(key=lambda f: int(re.sub('\D', '', f)))
    for index, img in enumerate(imgList):
        imgList[index] = "./strony/oficyna/" + img
    print(imgList)

    with open("Oficyna.pdf","wb") as f:
        f.write(img2pdf.convert(imgList))

    print("Gotowe!")