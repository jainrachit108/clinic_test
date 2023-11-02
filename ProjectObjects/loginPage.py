from selenium.webdriver.common.by import By

class Login:
    
    textbox_clinic_xpath =   "//*[@id='clinic']/span/input"
    textbox_username_xpath = "//*[@id='username']/span/input"
    textbox_password_xpath = "//*[@id='password']/span/input"
    button_login_xpath = "//button[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']"
    message_failed_login_xpath = "//span[@class='mtab-login-error-message']"
    

    def __init__(self, driver):
        self.driver = driver
        
    def set_login_clinic(self, clinic):
        self.driver.find_element(By.XPATH, self.textbox_clinic_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_clinic_xpath).send_keys(clinic)
        
        
    def set_login_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)
        
    def set_login_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        
    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


    def failed_login_message(self):
        message = self.driver.find_element(By.XPATH, self.message_failed_login_xpath).text
        
        return message