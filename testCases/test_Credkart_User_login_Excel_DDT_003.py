import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Page_Class
from utilities import XLutils
from utilities.Logger import log_generator_class
from utilities.ReadConfig import ReadConfigClass


class Test_User_Login_Excel_DDT_Class_003:
    # email = ReadConfigClass.get_data_for_email()
    # password = ReadConfigClass.get_data_for_password()
    loginurl = ReadConfigClass.get_login_pagr_url()
    Excel_File_Path = r'D:\A Credence Testing\Practice\Credkart_Project\Test_Data\TestData.xlsx'

    @pytest.mark.regression
    @pytest.mark.group1
    def test_CredKart_User_Login_Excel_DDT_004(self, driver_setup):
        self.driver = driver_setup
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.loginurl)

        excel_row_count = XLutils.RowCount(self.Excel_File_Path,"Sheet1")
        for i in range(2, excel_row_count+1):
            self.email = XLutils.ReadData(self.Excel_File_Path,"Sheet1", i, 1)
            self.password = XLutils.ReadData(self.Excel_File_Path,"Sheet1", i, 2)
            self.expected_result = XLutils.ReadData(self.Excel_File_Path,"Sheet1",i,3)

            self.lp.Enter_Email(self.email)
            self.lp.Enter_Password(self.password)
            self.lp.Click_Login_Button()

            if self.lp.Verify_Login_User() == "login_pass":
                actual_result = "login_pass"
                print("User is logged in")

            else:
                actual_result = "login_fail"
                print("User in not logged in")
                self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002.png")

            if self.expected_result == actual_result:
                test_case_status = "pass"

            else:
                test_case_status = "fail"

            XLutils.WritData(self.Excel_File_Path,"Sheet1",i, 4, actual_result)
            XLutils.WritData(self.Excel_File_Path, "Sheet1", i, 5, test_case_status)
            self.driver.get(self.loginurl)




# pytest -v  -s  -n auto  --html=Reports/my_report.html  --browser=chrome
# pytest -v -n auto  --html=Reports/my_report.html  --browser=chrome
# pytest -v --alluredir="AllureReports"















