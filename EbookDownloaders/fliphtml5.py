import os
import time
from io import BytesIO
from PIL import Image

import img2pdf, re, json, requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

pause = input("Podaj tryb programu. \n1 - Pobieranie plikow \n2 - Pakowanie w PDF. \n\nWybór: ")

if str(pause) == "1":
    with open("ebook-config.json", "r") as config: 
        data = json.load(config)
        email = data["oficynaEmail"]
        password = data["oficynaPassword"]
        manual = data["manual"]
    
    s=Service(ChromeDriverManager().install())

    if manual:
        pause = input("\nPotwierdz pobranie sterownika.")

    chrome_options = Options()
    # chrome_options.add_argument(r"--user-data-dir=C:\Users\Wafel\AppData\Local\Google\Chrome\User Data") 
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=s, options=chrome_options)

    # driver.get("https://fliphtml5.com/ztdza/exhn/Entorno_laboral_A1-B1_%28nueva_edición%29/")
    driver.get("https://online.fliphtml5.com/ztdza/exhn/#p=1")
    time.sleep(2)

    # W tym miejscu wklej XPATH do książki. Jak to zrobić?
    # 1. Kliknij prawym na tytuł książki
    # 2. Zbadaj element
    # 3. Znajdź linijkę zaczynającą się od tagu <a> z parametrem "href"
    # 3.1 np. "<a class="bookPane_book-pane__3Il8m" href="/app/book/68fff0f7-72a9-47bf-84ab-8941caf892e6"> bla bla bla..."
    # 4. Kliknij na nią prawym
    # 5. Copy -> Full XPATH
    # 6. Wklej go w poniższą ścieżkę
    
    if manual:
        pause = input("Kliknij Enter by rozpoczac pobieranie plikow, jak książka się załaduje... \n!!! Upewnij się że zamknięto cookies i reklamy !!!")
    else:
        time.sleep(2)

    # Full screen
    try:
        button = driver.find_element("xpath", '//*[@id="bottomRightBar"]/div[4]')
    except:
        print("Element not found")
    
    button.click()
    time.sleep(2)

    # Tutaj podaj ilość stron w książce
    for x in range(1, 226+1):
        current_page_box = driver.find_element(By.XPATH, '//*[@id="currentPageIndexTextField"]')
        # put x in input
        current_page_box.clear()
        time.sleep(0.5)
        current_page_box.send_keys(x)
        time.sleep(0.5)
        current_page_box.send_keys(Keys.ENTER)
        time.sleep(1)

        if x == 1 or x == 226:
            page = driver.find_element(By.XPATH, f'//*[@id="page{x}"]/div[1]/div/img')
            src = page.get_attribute("src")
            response = requests.get(src)
            if response.status_code == 200:
                with open(f'strony/fliphtml5/Strona_{x}.webp', "wb") as file:
                    file.write(response.content)
                print(f"Image saved as Strona_{x}.webp")
            else:
                print(f"Failed to download image - {x} | {src}")
            continue
        

        if x % 2 == 0:
            page = driver.find_element(By.XPATH, f'//*[@id="page{x}"]/div[1]/div/img')
        else:
            page = driver.find_element(By.XPATH, f'//*[@id="page{x}"]/div[1]/div/img')
        src = page.get_attribute("src")
        response = requests.get(src)
        if response.status_code == 200:
            with open(f'strony/fliphtml5/Strona_{x}.webp', "wb") as file:
                file.write(response.content)
            print(f"Image saved as Strona_{x}.webp")
        else:
            print(f"Failed to download image - {x} | {src}")
        continue
    if manual:
        pause = input("Kliknij Enter by zakonczyc program...")
        exit()

    print("Done")
    

if str(pause) == "2":
    folder_path = './strony/fliphtml5/'
    imgList = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.webp')]

    for index, img in enumerate(imgList):
        if "Strona" not in imgList[index]:
            imgList.pop(index)
    
    imgList.sort(key=lambda f: int(re.sub(pattern='\D', repl='', string=f)))
    converted_images = []

    for img in imgList:
        img_path = os.path.join(folder_path, img)
        with Image.open(img_path) as im:
            temp_path = img_path.replace('.webp', '.png')
            im.save(temp_path, format='PNG')
            converted_images.append(temp_path)

    with open("Fliphtml5.pdf", "wb") as f:
        f.write(img2pdf.convert(converted_images))

    # Clean up temporary PNG files
    for temp_img in converted_images:
        os.remove(temp_img)

    print("Gotowe!")
