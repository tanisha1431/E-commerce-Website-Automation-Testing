from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Project.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Test_Project.src.SeleniumExtended import SeleniumExtended
from Test_Project.src.helpers.config_helper import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint='/my-account/'



    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def go_to_account(self):
        base_url=get_base_url()
        
        account_url=base_url+self.endpoint
        logger.info(f"Going to{account_url}")
        self.driver.get(account_url)
        

    def input_username(self,username):
        self.sl.wait_until_element_located_send_text(self.LOGIN_USERNAME,username)
       
    def input_password(self,password):
        self.sl.wait_until_element_located_send_text(self.LOGIN_PASSWORD, password)
        
    def click_login(self):
        self.sl.wait_until_element_located_click(self.LOGIN_BTN)

    def err_message_displayed(self,err_message):
        self.sl.wait_until_text_displayed(self.ERR_UL,err_message,20)

    def input_new_username(self,new_username):
        self.sl.wait_until_element_located_send_text(self.REG_USERNAME, new_username)

    def input_new_email(self,new_email):
        self.sl.wait_until_element_located_send_text(self.REG_EMAIL,new_email)

    def click_register(self):
        self.sl.wait_until_element_located_click(self.REG_BTN)

        

