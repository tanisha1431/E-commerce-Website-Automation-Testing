import pytest
from Test_Project.src.SeleniumExtended import SeleniumExtended
from Test_Project.src.pages.locators.OrderRecievedLocator import OrderRecievedLocator

class OrderRecievedPage(OrderRecievedLocator):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)
        
    def get_order_text(self):
        self.sl.wait_until_text_displayed(self.ORDER_RECIEVED_TEXT, "Thank you. Your order has been received.")

    def get_order_no(self):
        order_number=self.sl.wait_and_get_element_text(self.ORDER_NO)
        return order_number


