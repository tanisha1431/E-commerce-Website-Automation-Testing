import pytest
from selenium import webdriver
from Test_Project.src.pages.locators.CheckoutpageLocator import CheckoutpageLocator
from Test_Project.src.SeleniumExtended import SeleniumExtended
from Test_Project.src.helpers.generic_helper import generate_username_email


class Checkoutpage(CheckoutpageLocator):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def input_first_name(self,firstname=None):
        first_name=firstname if firstname else "Test_user"
        self.sl.wait_until_element_located_send_text(self.CHECKOUT_NAME, first_name)

    def input_last_name(self,lastname=None):
        last_name=lastname if lastname else "Test_user_lastname"
        self.sl.wait_until_element_located_send_text(self.CHECKOUT_LAST_NAME, last_name)

    def input_street_address(self,streetaddress=None):
        streetaddress=streetaddress if streetaddress else "Test_user_address"
        self.sl.wait_until_element_located_send_text(self.CHECKOUT_STREET_ADDRESS_1, streetaddress)

    def input_city(self,city=None):
        city=city if city else "Pune"
        self.sl.wait_until_element_located_send_text(self.CHECKOUT_CITY, city)

    def input_pincode(self,pincode=None):
        pincode=pincode if pincode else "411052"
        self.sl.wait_until_element_located_send_text(self.CHECKOUT_PINCODE, pincode)

    def input_phone(self,phone=None):
        phone=phone if phone else "8511784432"
        self.sl.wait_until_element_located_send_text(self.CHECKOUT_PHONE, phone)

    def input_email(self,email=None):
        
        generated=generate_username_email()
        e_mail=generated["new_email"]
        test_email=email if email else e_mail
        self.sl.wait_until_element_located_send_text(self.CHECKOUT_EMAIL,test_email)


    def click_proceed(self):
        
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)


    





    


    




