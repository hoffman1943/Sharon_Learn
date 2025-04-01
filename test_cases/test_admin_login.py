import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_admin_login:
    admin_page_url = Read_Config.get_admin_page_url()
    user_name = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_user_name = Read_Config.get_invalid_user_name()
    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup):
        self.logger.info("***************test_title_verification_started***************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            self.logger.info("***************test_title_verification_title_match***************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\screenshots\\test_title.png')
            self.logger.info("***************test_title_verification_title_not_match***************")
            self.driver.close()
            assert False

    def test_valid_admin_login(self, setup):
        self.logger.info("***************test_valid_admin_login_started***************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.user_name)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_login_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//h1'))
        ).text
        if act_login_text == 'admin-demo.nopcommerce.com':
            self.logger.info("***************test_valid_admin_login-login_text_has_found***************")
            assert True
            self.driver.close()
        else:
            self.logger.info("***************test_valid_admin_login-login_text_not_found***************")
            self.driver.save_screenshot('.\\screenshots\\test_valid_admin_login.png')
            self.driver.close()
            assert False

    # def test_invalid_admin_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.admin_page_url)
    #     self.admin_lp = Login_Admin_Page(self.driver)
    #     self.admin_lp.enter_username(self.invalid_user_name)
    #     self.admin_lp.enter_password(self.password)
    #     self.admin_lp.click_login()
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, "//li"))
    #     )
    #     if error_message == "No customer account found":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot('.\\screenshots\\test_invalid_admin_login.png')
    #         self.driver.close()
    #         assert False
