from selenium.webdriver.common.by import By

class OrderRecievedLocator:
    ORDER_RECIEVED_TEXT=(By.CSS_SELECTOR,".woocommerce-notice")
    ORDER_NO=(By.CSS_SELECTOR,".woocommerce-order-overview__order > strong:nth-child(1)")
