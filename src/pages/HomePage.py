from Test_Project.src.helpers.config_helper import get_base_url
from selenium import webdriver
from Test_Project.src.pages.locators.HomepageLocator import HomepageLocator
from Test_Project.src.SeleniumExtended import SeleniumExtended


class HomePage(HomepageLocator):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def go_to_homepage(self):
        home_page_url=get_base_url()
        self.driver.get(home_page_url)
    
    def click_on_item(self):
        self.sl.wait_until_element_located_click(self.FIRST_ITEM)
        

        