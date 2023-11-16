import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Foptions
import os

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browser=['ff','firefox','headlessfirefox']
    browser=os.environ.get('BROWSER',None)
    if not browser:
        raise Exception("The browser must be set.")
    browser=browser.lower()
    if browser not in supported_browser:
        raise Exception("The browser must be supported.")

    if browser in ('ff','firefox'):
        driver=webdriver.Firefox()
    elif browser in ('headlessfirefox'):
        ff_options=Foptions()
        ff_options.add_argument("--disable-gpu")
        ff_options.add_argument("--no-sandbox")
        ff_options.add_argument("--headless")
        driver=webdriver.Firefox(options=ff_options)




    request.cls.driver=driver
    yield
    #driver.quit()
