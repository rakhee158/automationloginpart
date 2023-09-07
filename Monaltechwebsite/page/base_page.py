from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Monaltechmainpage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def send_keys(self, by_locator, value):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)

    def click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()
    def wait_for(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator))



