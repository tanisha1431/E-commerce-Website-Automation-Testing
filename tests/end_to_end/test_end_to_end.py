import pytest
from Test_Project.src.pages.HomePage import HomePage
from Test_Project.src.pages.CartPage import CartPage
import time
from Test_Project.src.configs.generic_config import Generic_configs
from Test_Project.src.pages.Checkoutpage import Checkoutpage
from Test_Project.src.pages.OrderRecievedPage import OrderRecievedPage
from Test_Project.src.helpers.database_helper import get_order_number

@pytest.mark.usefixtures("init_driver")
class Test_end_to_end:
    @pytest.mark.tc3
    def test_end_to_end(self):
        #go to home page
        home=HomePage(self.driver)
        home.go_to_homepage()
        home.click_on_item()
        time.sleep(5)
        cart=CartPage(self.driver)

        cart.go_to_cart()
        product=cart.get_all_product_names()
        assert len(product)==1 , f"Expected 1 product in cart but found {len(product)}"

        alert_text=cart.apply_coupon(Generic_configs.COUPON_CODE)
        assert alert_text=="Coupon code applied successfully.",f"You have entered the wrong coupon code"

        cart.checkout()
        checkout=Checkoutpage(self.driver)
        checkout.input_first_name()
        checkout.input_last_name()
        checkout.input_street_address()
        checkout.input_city()
        checkout.input_pincode()
        checkout.input_phone()
        checkout.input_email()
        checkout.click_proceed()
        order=OrderRecievedPage(self.driver)
        order.get_order_text()
        oder_no=order.get_order_no()
        print(oder_no)
        db_order_no=get_order_number(oder_no)
        assert db_order_no,f'after checking with frontend,no such order number exists'
       




        
