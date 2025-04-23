from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_Page_Class:
    text_email_id = "email"
    text_password_id = "password"
    button_login_class = "btn"
    button_menubutton_class = "dropdown-toggle"
    button_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self,email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(By.CLASS_NAME, self.button_login_class).click()

    def Click_Menu_Button(self):
        self.driver.find_element(By.CLASS_NAME, self.button_menubutton_class).click()

    def Click_Logout_Button(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def Verify_Login_User(self):
        try:
            menuBotton= self.driver.find_element(By.CLASS_NAME, self.button_menubutton_class)
            menuBotton.click()
            self.Click_Logout_Button()
            return "login_pass"

        except:
            return "login_fail"











