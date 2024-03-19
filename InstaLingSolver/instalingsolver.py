import random
import re
import time
import json
import requests
import os
from alive_progress import alive_bar
from deep_translator import GoogleTranslator

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

script_dir = os.path.dirname(__file__)
config_path = os.path.join(script_dir, 'instaling-config.json')

# SECTION Config
with open(f"{config_path}", "r") as config: 
    data = json.load(config)
    login = data["login"]
    password = data["password"]
    manual = data["manual"]
    browser = data["browser"]
    webhookUrl = data["webhook_url"]
    max_good_ans = data["max_good_answers"]

# create a file to store translations
try:
    with open("translations.json", "r") as translations:
        pass
except:
    with open("translations.json", "w") as translations:
        translations.write("{}")

# SECTION Functions
def sendWebhook(message, error = False):
    url = webhookUrl

    if error:
        message = f"**ERROR:** <@273904398261026817>: ```\n{message}\n```"
    data = {
        "content" : message,
        "username" : "InstaLingSolver",
    }

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        if manual:
            print("Webhook wysłany, response code {}.".format(result.status_code))

def getElement(driver, by, value, fail = True):
    """
    Find and return a web element using the specified locator strategy and value.

    Args:
        driver: WebDriver instance.
        by: Locator strategy (e.g., "xpath", "id", "class").
        value: Locator value.

    Returns:
        WebElement: The web element if found, None otherwise.
    """
    attempts = 0
    while attempts < 5:
        try:
            if by == "xpath":
                el = driver.find_element(By.XPATH, value)
            elif by == "id":
                el = driver.find_element(By.ID, value)
            elif by == "class":
                el = driver.find_element(By.CLASS_NAME, value)

            if el is not None:
                return el
        except:
            attempts += 1
            time.sleep(1)
    if attempts >= 5:
        print(f"Nie udało się znaleźć elementu przez '{by}': {value}.")
        if fail:
            stop_app()
        return None
    
def solveWord(translator, word):
    """
    Solves a word by looking up its translation in a JSON file or using a translator.

    Args:
        translator: The translator object used to translate the word.
        word: The word to be solved.

    Returns:
        The translated word if found in the JSON file, otherwise the translated word from the translator.
    """
    with open("translations.json", "r") as translations:
        data = json.load(translations)
        if word in data:
            if data[word] == "False" or data[word] == False or data[word] == None:
                return "aa"
            return data[word]

    translated = translator.translate(word)
    return translated

def saveTranslation(word, translated, fullword = None):
    """
    Saves the translation of a word to a JSON file.

    Args:
        word (str): The word to be translated.
        translated (str): The translated word.

    Returns:
        None
    """
    if translated is None:
        translated = "False"

    with open("translations.json", "r") as translations:
        data = json.load(translations)
        if fullword is not None:
            data[fullword] = translated
        else:
            data[word] = translated
    with open("translations.json", "w") as translations:
        json.dump(data, translations, indent=4)

def printSummary(driver):
    grade = getElement(driver, "id", "session_result")
    grade = grade.get_attribute("innerHTML")

    pattern = r'Dni pracy w tym tygodniu: \d+'
    match = re.search(pattern, grade)
    if match:
        days = match.group()

    pattern = r'Powtórzyłeś \d+ słówek, \d+ bezbłędnie\.'
    match = re.search(pattern, grade)
    if match:
        grade = match.group()
    
    print(f"Gratulacje, zakończono rozwiązywanie. {grade} {days}")
    sendWebhook(f"Gratulacje, zakończono rozwiązywanie. {grade} {days}")
    driver.quit()
    exit()

# SECTION App
def stop_app():
    print("Zakończono program.")
    sendWebhook("Zakończono program.")
    input("Kliknij Enter aby zakończyć...")
    exit()

def run_app(max_good_ans = [7, 11]):
    if browser == "chrome":
        serv = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")

        driver = webdriver.Chrome(service=serv, options=chrome_options)
    elif browser == "safari":
        driver = webdriver.Safari()
    elif browser == "edge":
        driver = webdriver.Edge()

    # SECTION Sign in
    attempts = 0
    while "https://instaling.pl/student/pages/mainPage.php?student_id" not in driver.current_url:
        if attempts > 5:
            print("Nie udało się zalogować.")
            sendWebhook("Nie udało się zalogować.", True)
            return False
        else:
            attempts += 1

        driver.get("https://instaling.pl/login.php")
        time.sleep(2)

        try: # Close cookies dialog
            dialog = getElement(driver, "xpath", "/html/body/div[2]/div[2]/div[1]")
            if (dialog is None) or ("fc-dialog" not in dialog.get_attribute("class")) or (dialog.get_attribute("role") != "dialog"):
                print("Nie znaleziono okna z informacją o ciasteczkach.")
                sendWebhook("Nie znaleziono okna z informacją o ciasteczkach.")
                pass
            else:
                button = getElement(driver, "xpath", "/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]")
                if button and button.get_attribute("aria-label") == "Zgadzam się": 
                    button.click()
                    print("Zamknięto okno z informacją o ciasteczkach.")
        except:
            print("Nie znaleziono okna z informacją o ciasteczkach.")
            sendWebhook("Nie znaleziono okna z informacją o ciasteczkach.")
            pass

        if manual:
            input("Kliknij Enter by przejść do logowania.")
        else:
            time.sleep(2)

        textbox = getElement(driver, "xpath", "/html/body/div[1]/div[3]/form/div/div[1]/div[1]/input")
        textbox.send_keys(login)

        textbox = getElement(driver, "xpath", "/html/body/div[1]/div[3]/form/div/div[1]/div[2]/input")
        textbox.send_keys(password)

        time.sleep(3) # Cooldown to get text entered properly 
        button = getElement(driver, "xpath", "//button[text()='ZALOGUJ']")
        if button.get_attribute("type") == "submit":
            button.click()
        else:
            print("Nie znaleziono przycisku do zalogowania. Kliknij go sam.")
            sendWebhook("Nie znaleziono przycisku do zalogowania.", True)


        time.sleep(2)

    print("Zalogowano.")

    # SECTION Main page
    if manual:
        pause = input("Kliknij Enter by przejść do rozwiązywania.")

    finishedToday = getElement(driver, "xpath", '//h4[text()="Dzisiejsza sesja wykonana"]', fail=False)
    if (finishedToday is not None) and (finishedToday.is_displayed()) and (input("Sesja była już dziś wykonana. Czy kontynuować? [T/N]: ").lower() == "n"):
        print("Zakończono program.")
        return False


    time.sleep(2)
    button = getElement(driver, "xpath", "/html/body/div[1]/div[2]/div/p[1]/a")

    if button.get_attribute("innerHTML") not in ("Dokończ sesję", "Zacznij codzienną sesję"):
        print("Nie znaleziono przycisku do rozpoczęcia rozwiązywania.")
        sendWebhook("Nie znaleziono przycisku do rozpoczęcia rozwiązywania.", True)
        return False

    button.click()
    time.sleep(3)

    # SECTION Words
    attempts = 0
    while "https://instaling.pl/ling2/html_app/app.php?child_id" not in driver.current_url:
        if attempts > 5:
            print("Nie udało się przejść do słówek.")
            sendWebhook("Nie udało się przejść do słówek.")
            return False
        else:
            attempts += 1
            time.sleep(3)

    text = getElement(driver, "id", "continue_session_page")
    if text.is_displayed():
        if "Sesja została rozpoczęta, ale nie została jeszcze dokończona" in text.get_attribute("innerHTML"):
            button = getElement(driver, "id", "continue_session_button")
        else:
            button = getElement(driver, "xpath", "/html/body/div/div[5]/div[2]")
    else:
        text = getElement(driver, "id", "start_session_page")
        button = getElement(driver, "id", "start_session_button")

        if (not text.is_displayed()) and (not button.is_displayed()):
            print("Nie znaleziono przycisku do rozpoczęcia sesji.")
            sendWebhook("Nie znaleziono przycisku do rozpoczęcia sesji.", True)
            stop_app()

    button.click()
    time.sleep(2)

    translator = GoogleTranslator(source='pl', target='de')


    attempts = 0
    good_ans = 0
    failed_words = [] # Words were skipped due to the limit of good answers being reached, will be answered properly again

    if (max_good_ans != "None") and (max_good_ans is not None):
        max_good_ans = random.randint(max_good_ans[0], max_good_ans[1])
        
    while "https://instaling.pl/ling2/html_app/app.php?child_id" in driver.current_url:
        if manual:
            input("Kliknij Enter by rozwiązać słówko...")

        summary = getElement(driver, "id", "summary")
        session_result = getElement(driver, "id", "session_result")
        if summary.is_displayed() and (session_result.is_displayed()):
            printSummary(driver)

        word = getElement(driver, "class", "translations")
        textbox = getElement(driver, "id", "answer")
        checkAnswer = getElement(driver, "id", "check")

        if (not textbox.is_displayed()) and (not textbox.is_enabled()):
            print("Nie można wpisać słówka do formularza.")
            sendWebhook("Nie można wpisać słówka do formularza.", True)
            stop_app()


        if (not checkAnswer.is_displayed()) and (not checkAnswer.is_enabled()):
            print("Nie znaleziono przycisku do sprawdzenia rozwiązania.")
            sendWebhook("Nie znaleziono przycisku do sprawdzenia rozwiązania.", True)
            stop_app()

        word = word.get_attribute("innerHTML")
        translated = solveWord(translator, word)

        if (good_ans >= max_good_ans) and (word not in failed_words):
            if good_ans == max_good_ans:
                print(f"Osiągnięto maksymalną ilość dobrych odpowiedzi: {good_ans}.")
                sendWebhook(f"Osiągnięto maksymalną ilość dobrych odpowiedzi: {good_ans}.")
            translated = ""
            failed_words.append(word)

        attempts = 0
        while not textbox.is_displayed():
            summary = getElement(driver, "id", "summary")
            if summary.is_displayed() and ("Gratulacje" in summary.get_attribute("innerHTML")):
                printSummary(driver)
            
            if attempts > 5:
                print("Nie udało się znaleźć textboxa. Możliwe że program zakończył swoje działania.")
                sendWebhook("Nie udało się znaleźć textboxa.", True)
                stop_app()

            time.sleep(2)
            textbox = getElement(driver, "id", "answer")
            nextWord = getElement(driver, "id", "nextword")
            if nextWord.is_displayed():
                nextWord.click()
                time.sleep(2)
                textbox = getElement(driver, "id", "answer")
                # if not textbox.is_displayed():
                #     sendWebhook(f"Textbox się nie wyświetlił po kliknięciu przycisku do następnego słówka. \n[Textbox displayed: `{textbox.is_displayed()}`] \n[Nextword displayed: `{nextWord.is_displayed()}`]")

                word = getElement(driver, "class", "translations")
                word = word.get_attribute("innerHTML")
                checkAnswer = getElement(driver, "id", "check")
                translated = solveWord(translator, word)
            print("")
            attempts += 1
            if textbox.is_displayed():
                break
            else: # Sometimes there's a "I know this word" / "I don't know this word" button
                know_section = getElement(driver, "id", "new_word_form")
                if know_section.is_displayed():
                    know_button = getElement(driver, "id", "know_new")
                    dont_know_button = getElement(driver, "id", "dont_know_new")
                    if know_button.is_displayed() and dont_know_button.is_displayed():
                        dont_know_button.click()
                        know_section = getElement(driver, "id", "possible_word_page")
                        skip_button = getElement(driver, "id", "skip")
                        if know_section.is_displayed() and skip_button.is_displayed():
                            skip_button.click()
                            time.sleep(2)
                            del know_section, know_button, dont_know_button, skip_button
                            # textbox = getElement(driver, "id", "answer")
                            # word = getElement(driver, "class", "translations")
                            # word = word.get_attribute("innerHTML")
                            # checkAnswer = getElement(driver, "id", "check")
                            # translated = solveWord(translator, word)
                            # break
                            

        if (word is None) or (word == "None") or (translated == None):
            print(f"Nie udało się przetłumaczyć słówka: {word}.")
            sendWebhook(f"Nie udało się przetłumaczyć słówka: `{word}` / `{translated}`.", True)
            stop_app()

        # There are some words described like "hasło, slogan" and we need to split them
        fullWord = None
        if ", " in word:
            fullWord = word
            word = word.split(", ")[0]
        if ", " in translated:
            translated = translated.split(", ")[0]



        print(f"{word} -> {translated}")
        with alive_bar(100, title='5 sekund...', bar='brackets', spinner='flowers', stats=False) as bar:
            for i in range(100):
                if i == 70:
                    textbox.send_keys(translated)
                if i == 99:
                    checkAnswer.click()
                time.sleep(.05)
                bar()

        answer = getElement(driver, "id", "word")
        answer = answer.get_attribute("innerHTML")
        result = getElement(driver, "id", "answer_result")
        nextWord = getElement(driver, "id", "nextword")

        if (not nextWord.is_displayed()) and (not nextWord.is_enabled()):
            print("Nie znaleziono przycisku do przejścia do następnego słówka.")
            sendWebhook("Nie znaleziono przycisku do przejścia do następnego słówka.", True)
            stop_app()
            

        # TODO: If word was failed the first time, but then answered properly. Do not count it as good answer

        if "Niepoprawnie" in result.get_attribute("innerHTML"):
            if answer == translated:
                sendWebhook(f"Odpowiedzi są identyczne, ale jednak złe. `{word}` -> `{answer}` zamiast `{translated}`.", True)
            print(f"Zła odpowiedź: {word} -> {answer} zamiast {translated}.")
            failed_words.append(word)
        elif "Literówka" in result.get_attribute("innerHTML"):
            print(f"Literówka: {word} -> {translated}.")
            answer = None
            failed_words.append(word)
        elif "Dobrze" in result.get_attribute("innerHTML"):
            print(f"Dobra odpowiedź: {word} -> {answer}.")
            if word not in failed_words:
                good_ans += 1

        

        saveTranslation(word, answer, fullWord)

        with alive_bar(100, title='3 sekundy...', bar='brackets', spinner='flowers', stats=False) as bar:
            for i in range(100):
                if i == 199:
                    nextWord.click()
                time.sleep(.03)
                bar()

    if manual:
        pause = input("Kliknij Enter by zakonczyc program...")
    driver.quit()

run_app(max_good_ans)
input("Kliknij Enter aby zakończyć...")
exit()

# TODO: Progress bar for properly answered words, and failed words. Terminal being cleared and progress bars being updated each word