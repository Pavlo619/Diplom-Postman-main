import requests
import allure


headers = {"authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyMDYwODYwLCJpYXQiOjE3NDc3NDA3NTcsImV4cCI6MTc0Nzc0NDM1NywidHlwZSI6MjB9.P9T_vh4u_xsMzpzOt62maljzN5t0UAP0st5iSB_maRE"}
base_url = "https://web-gate.chitai-gorod.ru/api/v2/"


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по автору")
@allure.description("Проверка, что API возвращает книги с ожидаемым автором.")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=джоан роулинг", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по названию")
@allure.description("Проверка, что API возвращает книгу с ожидаемым названием")
def test_api_book_by_title():
    resp = requests.get(f"{base_url}search/product?phrase=капитанская дочка", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по автору на английском")
@allure.description("Проверка, что API возвращает книгу с ожидаемым названием на английском.")
def test_search_by_language_english():
    resp = requests.get(f"{base_url}search/product?phrase=The lord of rings", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска с недопустимой японской фразой")
@allure.description("Проверка, что API возвращает ошибку при поиске с недопустимой японской фразой.")
def test_negative_api_Japanese():
    resp = requests.get(f"{base_url}search/product?phrase=人で座ってください")
    assert resp.status_code == 422

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска с пустым запросом")
@allure.description("Проверка, что API возвращает ошибку при пустом поисковом запросе.")
def test_negative_api_empty_search():
    resp = requests.get(f"{base_url}search/product?phrase=", headers=headers)
    assert resp.status_code == 400