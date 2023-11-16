from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator():
    LOGIN_USERNAME=(By.ID,"username")
    LOGIN_PASSWORD=(By.ID,"password")
    LOGIN_BTN=(By.CSS_SELECTOR,"#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
    ERR_UL=(By.CSS_SELECTOR,"#content > div:nth-child(1) > div:nth-child(1)")
    REG_USERNAME=(By.ID,"reg_username")
    REG_EMAIL=(By.ID,"reg_email")
    REG_BTN=(By.CSS_SELECTOR,".woocommerce-Button")
    

