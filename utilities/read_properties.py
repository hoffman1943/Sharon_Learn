import configparser
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url
    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username
    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password
    @staticmethod
    def get_invalid_user_name():
        invalid_user_name = config.get('admin login info', 'invalid_user_name')
        return invalid_user_name
