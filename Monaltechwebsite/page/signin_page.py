from selenium.webdriver.common.by import By

from Monaltechwebsite.page.base_page import Monaltechmainpage



class signinpage(Monaltechmainpage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    clickonsign= ( By.XPATH,"//a[normalize-space()='Sign in']")
    emailforsignin= (By.XPATH,"//input[@id='login']")
    passwordforsign=(By.CSS_SELECTOR,"#password")
    clickonlogin=(By.XPATH,"//div[@class='clearfix oe_login_buttons text-center mb-1 pt-3']/button")



    def go_signin_page(self):
        self.click(self.clickonsign)

    def enter_credentialrequired_page(self,email,password):
        self.send_keys(self.emailforsignin,email)
        self.send_keys(self.passwordforsign,password)
        self.wait_for(self.clickonlogin)
        self.click(self.clickonlogin)









