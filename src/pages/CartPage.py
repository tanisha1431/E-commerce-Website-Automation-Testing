from selenium.webdriver.common.by import By
from Test_Project.src.SeleniumExtended import SeleniumExtended
from Test_Project.src.pages.locators.CartpageLocator import CartpageLocator
import time 


class CartPage(CartpageLocator):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def go_to_cart(self):
        self.sl.wait_until_element_located_click(self.CART_LINK)

    def get_all_product_names(self):
        
        
        products=self.sl.wait_and_get_all_elements(self.ALL_PRODUCTS)
        print (type(products))
        product=[i.text for i in products]
        #print(product)
        return product

    def input_coupon(self,text):
        self.sl.wait_until_element_located_send_text(self.COUPON_INPUT, text)

    def click_submit_coupon(self):
        self.sl.wait_until_element_located_click(self.COUPON_BTN)

    def apply_coupon(self,text):
        self.input_coupon(text)
        self.click_submit_coupon()
        alert_text=self.sl.wait_and_get_element_text(self.COUPON_ALERT)
        return alert_text


    def checkout(self):
        self.sl.wait_and_click(self.CHECKOUT_BTN)
