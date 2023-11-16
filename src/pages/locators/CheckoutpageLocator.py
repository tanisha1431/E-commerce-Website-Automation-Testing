
from selenium.webdriver.common.by import By

class CheckoutpageLocator:
    CHECKOUT_NAME=(By.CSS_SELECTOR,"#billing_first_name")
    CHECKOUT_LAST_NAME=(By.CSS_SELECTOR,"#billing_last_name")
    CHECKOUT_STREET_ADDRESS_1=(By.CSS_SELECTOR,"#billing_address_1")
    CHECKOUT_CITY=(By.CSS_SELECTOR,"#billing_city")
    CHECKOUT_PINCODE=(By.CSS_SELECTOR,"#billing_postcode")
    CHECKOUT_PHONE=(By.CSS_SELECTOR,"#billing_phone")
    CHECKOUT_EMAIL=(By.CSS_SELECTOR,"#billing_email")
    PLACE_ORDER_BTN=(By.CSS_SELECTOR,"#place_order")


