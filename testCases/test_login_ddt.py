from ProjectObjects.loginPage import Login
from Utilities.readProperties import ReadConfig
from testCases.conf_test import setup
from Utilities.customLogger import LogGen
from  Utilities import excel_utils 
import time

class Test_002_login:
    
    baseURL = ReadConfig.get_app_url()
    path = './/TestData/LoginData.xlsx'
    
    # logger_obj = LogGen.logger()
    

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)     
        rows = excel_utils.getRowCount(filepath=self.path, sheet_no='Sheet1')
        
        self.login_obj = Login(self.driver)
        for i in range(2, rows+1):
            self.clinic = excel_utils.readData(self.path, 'Sheet1',row=i, col=1)
            self.username = excel_utils.readData(self.path, 'Sheet1', row=i, col=2)
            self.password = excel_utils.readData(self.path, 'Sheet1', row=i, col=3)
            
            self.login_obj.set_login_clinic(self.clinic)
            self.login_obj.set_login_username(self.username)
            self.login_obj.set_login_password(self.password)
                                
            
            self.login_obj.click_login_button()
            time.sleep(3)
            message = self.login_obj.failed_login_message()
            if message == 'Invalid username or password':
                excel_utils.writeData(filepath=self.path, sheet_no='Sheet1', row=i, col=5, data='Passed')
                assert True
                
            else:
                excel_utils.writeData(self.path, 'Sheet1', row=i, col=4, data='Passed')
                self.driver.save_screenshot('.\\screenshots\\'+'homepage_title.png')
                self.driver.close()
                assert False
                     
            
            








            
    # def test_login(self, setup):
    #     self.driver = setup
    #     self.login_obj = Login(self.driver)
    #     self.driver.get(self.baseURL)
    #     self.driver.implicitly_wait(5)
    #     self.login_obj.set_login_clinic(self.clinic)
    #     self.login_obj.set_login_username(self.username)
    #     self.login_obj.set_login_password(self.password)

    #     self.login_obj.click_login_button()
    #     message = self.login_obj.failed_login_message()
    #     if message == 'Invalid username or password':
    #         assert True
    #     else:
    #         self.driver.save_screenshot('.\\screenshots\\'+'login_failed_message.png')
    #         self.driver.close()
    #         assert False
            