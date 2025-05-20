import time
import allure
import pytest
from selenium import webdriver  # импорт драйвера для взаимодействия с браузером
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver()-> WebDriver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги по заголовку")
@allure.description("Тест проверяет возможность поиска книги по заголовку 'капитанская'.")
def test_by_name(driver: WebDriver):
    with allure.step("Откройте сайт Читай-Город"):
        driver.get("https://www.chitai-gorod.ru")
        time.sleep(2)
    with allure.step("Введите запрос на поиск книги"):
        driver.find_element(By.NAME, "search").send_keys("капитанская")
    with allure.step("Нажмите кнопку поиска"):
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "капитанская"))
    with allure.step("Получите заголовки продуктов"):
        assert "Показываем результаты по запросу «капитанская», найдено:" in driver.find_element(By.CLASS_NAME, "search-title").text


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск автора")
@allure.description("Тест проверяет возможность поиска автора 'пушкин'.")
def test_by_name_author(driver: WebDriver):
    with allure.step("Откройте сайт Читай-Город"):
        driver.get("https://www.chitai-gorod.ru")
        time.sleep(2)
    with allure.step("Введите запрос на поиск книги"):
        driver.find_element(By.NAME, "search").send_keys("пушкин")
    with allure.step("Нажмите кнопку поиска"):
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "пушкин"))
    with allure.step("Получите заголовки продуктов"):
        assert "Показываем результаты по запросу «пушкин», найдено:" in driver.find_element(By.CLASS_NAME, "search-title").text


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги на английском")
@allure.description("Тест проверяет поиск книги с использование английского названия")
def test_by_name_language_english(driver: WebDriver):
    with allure.step("Откройте сайт Читай-Город"):
        driver.get("https://www.chitai-gorod.ru")
        time.sleep(2)
    with allure.step("Введите запрос на поиск книги"):
        driver.find_element(By.NAME, "search").send_keys("house")
    with allure.step("Нажмите кнопку поиска"):
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "house"))
    with allure.step("Получите заголовки продуктов"):
        assert "Показываем результаты по запросу «house», найдено:" in driver.find_element(By.CLASS_NAME, "search-title").text


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги с символами вместо названия")
@allure.description("Тест проверяет поиск книги с использование символов вместо названия")
def test_negative_by_symbols(driver: WebDriver):
    with allure.step("Откройте сайт Читай-Город"):
        driver.get("https://www.chitai-gorod.ru")
        time.sleep(2)
    with allure.step("Введите запрос на поиск книги с использованием символов"):
        driver.find_element(By.NAME, "search").send_keys("#$%")
    with allure.step("Нажмите кнопку поиска"):
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "#$%"))
    with allure.step("Получение результата запроса"):
        assert "Поиск по запросу «#$%» не принёс результатов" in driver.find_element(By.CLASS_NAME, "search-title").text


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги на тайском языке")
@allure.description("Тест проверяет поиск книги с использование тайских символов в названии")
def test_negative_by_language_thai(driver: WebDriver):
    with allure.step("Откройте сайт Читай-Город"):
        driver.get("https://www.chitai-gorod.ru")
        time.sleep(2)
    with allure.step("Введите запрос на поиск книги с использованием тайских символов"):
        driver.find_element(By.NAME, "search").send_keys("เกาะมหาสมบัต")
    with allure.step("Нажмите кнопку поиска"):
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
    WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "เกาะมหาสมบัต"))
    with allure.step("Получение результата запроса"):
        assert "Поиск по запросу «เกาะมหาสมบัต» не принёс результатов" in driver.find_element(By.CLASS_NAME, "search-title").text
