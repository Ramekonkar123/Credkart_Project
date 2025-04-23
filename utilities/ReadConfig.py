import configparser

config = configparser.RawConfigParser()
config.read(r"D:\A Credence Testing\Practice\Credkart_Project\Configurations\config.ini")


class ReadConfigClass:
    @staticmethod
    def get_data_for_email():
        email = config.get('login data', 'email')
        return email

    @staticmethod
    def get_data_for_password():
        password = config.get('login data', 'password')
        return

    @staticmethod
    def get_home_page_url():
        homepageurl = config.get('Application url','home_page')
        return homepageurl

    @staticmethod
    def get_login_pagr_url():
        loginpageurl = config.get('Application url','login_page')
        return loginpageurl

    @staticmethod
    def get_register_pagr_url():
        registerpageurl = config.get('Application url', 'register_page')
        return registerpageurl







