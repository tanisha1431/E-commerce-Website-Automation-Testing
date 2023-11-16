import pytest
from Test_Project.src.pages.MyAccountSignedOut import MyAccountSignedOut
from Test_Project.src.helpers.generic_helper import generate_username_email
from Test_Project.src.pages.MyAccountSignedIn import MyAccountSignedIn

@pytest.mark.usefixtures("init_driver")
class TestNewRegister:
    @pytest.mark.tc2
    def test_new_register(self):
        new_acc=MyAccountSignedOut(self.driver)
        new_acc_in=MyAccountSignedIn(self.driver)
        new_acc.go_to_account()
        new_cred=generate_username_email()
        new_acc.input_new_username(new_cred["new_username"])
        new_acc.input_new_email(new_cred["new_email"])
        new_acc.click_register()
        new_acc_in.logout_btn_visible()


