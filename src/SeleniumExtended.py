from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException , StaleElementReferenceException
import time

class SeleniumExtended:
    def __init__(self,driver):
        self.driver=driver
        self.defaultTimeout=10

    def wait_until_element_located_send_text(self,locator,text,timeout=None):
        timeout=timeout if timeout else self.defaultTimeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_until_element_located_click(self,locator,timeout=None):
        timeout=timeout if timeout else self.defaultTimeout
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()


        

    def wait_until_text_displayed(self,locator,text,timeout=None):
        timeout=timeout if timeout else self.defaultTimeout
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator,text))
        #alert_text=self.driver.find_element(locator).text
        #print(alert_text)
        # alert_element=WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        # alert_text=alert_element.text
        # print(alert_text)

    def wait_until_element_is_visible(self,locator,timeout=None):
        timeout=timeout if timeout else self.defaultTimeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_and_get_all_elements(self,locator,timeout=None,err=None):
        err=err if err else f"Unable to find any products in the cart."
        timeout=timeout if timeout else self.defaultTimeout
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            raise TimeoutException(err)


    def wait_and_get_element_text(self,locator,timeout=None):
        timeout=timeout if timeout else self.defaultTimeout
        alert_text=WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text
        return alert_text

    def wait_and_click(self,locator,timeout=None):
        timeout=timeout if timeout else self.defaultTimeout
        try:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
        except StaleElementReferenceException:
            time.sleep(5)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()

            







