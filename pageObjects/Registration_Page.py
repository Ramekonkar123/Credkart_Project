from selenium import webdriver
from selenium.webdriver.common.by import By


class Registration_Page_Class():
    text_name_id = "name"
    text_email_xpath = "//input[@id='email']"
    text_password_xpath = "//input[@id='password']"
    text_confirm_password_xpath = "//input[@id='password-confirm']"
    button_register_linkText = "Register"
    button_menubutton_class = "dropdown-toggle"
    button_logout_xpath = "//a[normalize-space()='Logout']"


    def __init__(self, driver):
        self.driver = driver

    def Enter_Name(self, name):
        self.driver.find_element(By.ID, self.text_name_id).send_keys(name)

    def Enter_Email(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath)

    def Enter_Confirm_Password(self, password):
        self.driver.find_element(By.XPATH, self.text_confirm_password_xpath).send_keys(password)

    def Click_Register_Button(self):
        self.driver.find_element(By.LINK_TEXT, self.button_register_linkText)

    def Click_Logout_Button(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def Verify_User_Register(self):
        try:
            menuBotton= self.driver.find_element(By.CLASS_NAME, self.button_menubutton_class)
            menuBotton.click()
            self.Click_Logout_Button()
            return "Registration_pass"

        except:
            return "Registration_fail"








