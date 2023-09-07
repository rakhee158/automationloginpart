import pytest
from Monaltechwebsite.page.signin_page import signinpage

@pytest.mark.usefixtures("setup")
class Testsigninpage:
    # with invalid credential
    def test_signin(self):
        self.signinmonaltech=signinpage(self.driver)
        self.signinmonaltech.go_signin_page()
        self.signinmonaltech.enter_credentialrequired_page("errakhimandal123@gmail.com","rakhi123")
     # with valid email and invalid password
    def test_valid(self):
        self.validemail = signinpage(self.driver)
        self.validemail.go_signin_page()
        self.validemail.enter_credentialrequired_page("errakhimandal.com", "ddfd")
    # with invalid email and valid password
    def test_invalid(self):
        self.invalidemail = signinpage(self.driver)
        self.invalidemail.go_signin_page()
        self.invalidemail.enter_credentialrequired_page("errawaed", "rakhi123@")


    # with blank email and password
    def test_blank(self):
        self.blank = signinpage(self.driver)
        self.blank.go_signin_page()
        self.blank.enter_credentialrequired_page("", "")











