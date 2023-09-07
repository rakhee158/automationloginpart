import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver


@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 5)
    driver.maximize_window()
    driver.get("https://monaltech.com/")
    request.cls.driver = driver

    yield
    driver. close()











