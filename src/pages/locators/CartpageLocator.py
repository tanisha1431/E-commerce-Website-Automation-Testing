from selenium.webdriver.common.by import By

class CartpageLocator:
    CART_LINK=(By.CSS_SELECTOR,".nav-menu > li:nth-child(2) > a:nth-child(1)")
    ALL_PRODUCTS=(By.CSS_SELECTOR,"tr.cart_item td.product-name")
    COUPON_INPUT=(By.ID,"coupon_code")
    COUPON_BTN=(By.CSS_SELECTOR,"button.button:nth-child(3)")
    COUPON_ALERT=(By.CSS_SELECTOR,".woocommerce-message")
    CHECKOUT_BTN=(By.CSS_SELECTOR,".checkout-button")
