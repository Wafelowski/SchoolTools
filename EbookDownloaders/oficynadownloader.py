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
    chrome_options.add_argument(r"--user-data-dir=C:\Users\Wafel\AppData\Local\Google\Chrome\User Data") 
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=s, options=chrome_options)

    driver.get("https://ebook.pazdro.com.pl/auth/login")
    time.sleep(2)
    
    if manual:
        pause = input("Kliknij Enter by przejść do logowania.")
    else:
        time.sleep(2)

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
    # 3.1 np. "<a class="bookPane_book-pane__3Il8m" href="/app/book/68fff0f7-72a9-47bf-84ab-8941caf892e6"> bla bla bla..."
    # 4. Kliknij na nią prawym
    # 5. Copy -> Full XPATH
    # 6. Wklej go w poniższą ścieżkę

    button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[4]/a")
    button.click()

    time.sleep(2)

    button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/article/div/div/div[2]/div[2]/div[1]/button")
    button.click()
    
    if manual:
        pause = input("Kliknij Enter by rozpoczac pobieranie plikow, jak książka się załaduje...")
    else:
        time.sleep(2)

    # Lupka pomniejszenia
    button = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/button[1]")
    button.click()

    # Tutaj podaj ilość stron w książce
    for x in range(1, 384):
        
        current_page_box = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/input')
        current_page = int(current_page_box.get_attribute("value"))
        time.sleep(2)

        both = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]')

        location = both.location
        size = both.size
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        # credits to https://stackoverflow.com/a/15870708 

        left = location['x']
        left = int(left)-50 #-200
        top = location['y']
        right = location['x'] + int(size['width'])-150 #-298
        bottom = location['y'] + int(size['height'])-120 #-249


        im = im.crop((left, top, right, bottom)) # defines crop points
        im.save(f'strony/oficyna/Strona {int(current_page)}.png')
        print(f'Zapisano obrazek ze strony {current_page}, url {driver.current_url} \n')
        
        # if current_page != 515:
        #     next_button.click()
        time.sleep(1)
        current_page_box.clear()
        current_page_box.send_keys(int(current_page)+1)
        time.sleep(0.5)
        current_page_box.send_keys(Keys.ENTER)
    
    if manual:
        pause = input("Kliknij Enter by zakonczyc program...")
        exit()

    print("Done")
    

if str(pause) == "2":
    # imgList = os.listdir('./strony/oficyna/')
    # Ignoruj foldery
    folder_path = './strony/oficyna/'
    imgList = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for index, img in enumerate(imgList):
        if "Strona" not in imgList[index]:
            imgList.pop(index)
    
    imgList.sort(key=lambda f: int(re.sub(pattern='\D', repl='', string=f)))
    for index, img in enumerate(imgList):
        imgList[index] = "./strony/oficyna/" + img
    print(imgList)

    with open("Oficyna.pdf","wb") as f:
        f.write(img2pdf.convert(imgList))

    print("Gotowe!")