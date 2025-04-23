import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Page_Class
from utilities.Logger import log_generator_class
from utilities.ReadConfig import ReadConfigClass


class Test_User_Profile_Class_001:
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    homeurl = ReadConfigClass.get_home_page_url()
    loginurl = ReadConfigClass.get_login_pagr_url()
    log = log_generator_class.loggen_method()


    @pytest.mark.sanity
    @pytest.mark.group1
    def test_verify_CredKart_Url_001(self, driver_setup):
         self.driver = driver_setup
         self.driver.maximize_window()
         # self.log.debug("this is debuge")
         # self.log.info("this is info")
         # self.log.warning("this is warning")
         # self.log.error("this is error")
        # self.log.critical("this is critical")
         self.log.info("\nTestcase test_verify_CredKart_Url_001 is started ")
         self.driver.get(self.homeurl)
         print(self.driver.title)
         self.log.info("opening browser ")
         self.log.info("Going to credkart url--> https://automation.credence.in/ ")
         self.log.info("Checking page title ")
         if self.driver.title == "CredKart":
            self.log.info("page title matches with expected title")
            print("Test pass")
            self.log.info("taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002.png")
            self.log.info("test_verify_CredKart_Url_001 is passes")
            assert True
         else:
            print("Test failed")
            self.log.info("test_verify_CredKart_Url_001 is failed")
            assert False
         self.log.info("test_case is completed")

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_CredKart_User_Login_002(self, driver_setup):
        self.driver = driver_setup
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.loginurl)
        # username= self.driver.find_element(By.XPATH,"//input[@id='email']")
        # username.send_keys("credencetest@test.com")
        self.lp.Enter_Email(self.email)

        # password= self.driver.find_element(By.XPATH,"//input[@id='password']")
        # password.send_keys("Credence@123")
        self.lp.Enter_Password(self.password)


        # login_button= self.driver.find_element(By.XPATH,"//button[@type='submit']")
        # login_button.click()
        self.lp.Click_Login_Button()

        # try:
        #     menuBotton= self.driver.find_element(By.XPATH,"//a[@role='button']")
        #     assert menuBotton.is_displayed()
        #     print("user is logged in")
        # except:
        #     print("user is not logged in")
        if self.lp.Verify_Login_User() == "login_pass":
            print("User is logged in")
            assert True
        else:
            print("User in not logged in")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002.png")
            assert False



# pytest -v  -s  -n auto  --html=Reports/my_report.html  --browser=chrome
# pytest -v -n auto  --html=Reports/my_report.html  --browser=chrome















