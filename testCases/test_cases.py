import pytest
from selenium import webdriver
from ProjectObjects.loginPage import Login
from Utilities.readProperties import ReadConfig
from testCases.conf_test import setup
from Utilities.customLogger import LogGen

class Test_001_login:
    
    baseURL = ReadConfig.get_app_url()
    clinic = ReadConfig.get_clinic_data()
    username = ReadConfig.get_username_data()
    password = ReadConfig.get_password_data()
    
    logger_obj = LogGen.logger()

    def test_homepage(self, setup):
        self.driver = setup
        self.logger_obj.info('Test Started')
        self.driver.get(self.baseURL)     
        act_title = self.driver.title

        if act_title == 'DrCatalystEHR':
            assert True
        else:
            self.driver.save_screenshot('.\\screenshots\\'+'homepage_title.png')
            self.driver.close()
            assert False
            
            
    def test_login(self, setup):
        self.driver = setup
        self.login_obj = Login(self.driver)
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.login_obj.set_login_clinic(self.clinic)
        self.login_obj.set_login_username(self.username)
        self.login_obj.set_login_password(self.password)

        self.login_obj.click_login_button()
        message = self.login_obj.failed_login_message()
        if message == 'Invalid username or password':
            assert True
        else:
            self.driver.save_screenshot('.\\screenshots\\'+'login_failed_message.png')
            self.driver.close()
            assert False
            