from Test_Project.src.SeleniumExtended import SeleniumExtended
from Test_Project.src.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocator

class MyAccountSignedIn(MyAccountSignedInLocator):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def logout_btn_visible(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT)


    
    
    
