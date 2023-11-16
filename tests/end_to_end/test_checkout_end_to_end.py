import pytest

from Test_Project.src.pages.HomePage import HomePage
from Test_Project.src.pages.CartPage import CartPage
from Test_Project.src.pages.Checkoutpage import Checkoutpage
import time
from Test_Project.src.configs.generic_config import Generic_configs

@pytest.mark.usefixtures("init_driver")
class Test_checkout_end_to_end:
    @pytest.mark.tc4
    def test_checkout_end_to_end(self):
        pass
        
