import configparser


config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    
    @staticmethod
    def get_app_url():
        url = config.get('common info', 'baseURL')
        return url
    
    @staticmethod
    def get_clinic_data():
        clinic = config.get('common info', 'clinic')
        return clinic
    
    @staticmethod
    def get_username_data():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password_data():
        password = config.get('common info', 'password')
        return password
    
    

        
        