import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\RITUSHREE\\Downloads\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\Users\\RITUSHREE\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise")
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield
    driver.close()






