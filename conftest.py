import pytest
from selenium import webdriver
import time

link_ru = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
link_es = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
link_fr = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru, es or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    if browser_name == "chrome" and browser_language == "ru":
        print("\nstart chrom.ru browser for test..")
        browser = webdriver.Chrome()
        browser.get(link_ru)
        time.sleep(10)
    elif browser_name == "chrome" and browser_language == "es":
        print("\nstart chrom.es browser for test..")
        browser = webdriver.Chrome()
        browser.get(link_es)
        time.sleep(10)
    elif browser_name == "chrome" and browser_language == "fr":
        print("\nstart chrom.fr browser for test..")
        browser = webdriver.Chrome()
        browser.get(link_fr)
        time.sleep(10)
    elif browser_name == "firefox" and browser_language == "ru":
        print("\nstart firefox.ru browser for test..")
        browser = webdriver.Firefox()
        browser.get(link_ru)
        time.sleep(10)
    elif browser_name == "firefox" and browser_language == "es":
        print("\nstart firefox.es browser for test..")
        browser = webdriver.Firefox()
        browser.get(link_es)
        time.sleep(10)
    elif browser_name == "firefox" and browser_language == "fr":
        print("\nstart firefox.fr browser for test..")
        browser = webdriver.Firefox()
        browser.get(link_fr)
        time.sleep(10)
    else:
        raise pytest.UsageError("--choose browser or language")
    yield browser
    print("\nquit browser..")
    browser.quit()
