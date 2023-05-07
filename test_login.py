import pytest
from selenium import webdriver
from page_object.Login_page import Login


class Test_001_Login:
    baseURL="https://www.nopcommerce.com/en/demo"
    username="admin@yourstore.com"
    password="admin"



    def test_homepagetitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()

        if act_title=="Your store. Login":
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots"+"test_homepagetitle.png")
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.SetUSername(self.username)
        self.lp.setpassword(self.password)
        self.lp.Login()
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots"+"test_login.png")
            self.driver.close()

            assert  False











