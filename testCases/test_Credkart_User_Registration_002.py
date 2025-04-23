import time

import faker
import pytest

from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities.ReadConfig import ReadConfigClass


class Test_User_Registration_Class_001:
    registerurl = ReadConfigClass.get_register_pagr_url()
    @pytest.mark.sanity
    @pytest.mark.group1
    def test_CredKart_User_Registration_003(self, driver_setup, faker):
        self.driver = driver_setup
        self.rp = Registration_Page_Class(self.driver)
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.registerurl)
        random_name = faker.name()
        random_email = faker.email()

        self.rp.Enter_Name(random_name)
        self.lp.Enter_Email(random_email)
        self.lp.Enter_Password("Credence@123")
        self.rp.Enter_Confirm_Password("Credence@123")
        self.lp.Click_Login_Button()


        if self.rp.Verify_User_Register() == "Registration_pass":
            print("User is register")
            assert True
        else:
            print("User in not register")
            self.driver.save_screenshot("..\\Screenshots\\test_CredKart_User_Registration_003.png")
            assert False
