from Test_Project.src.pages.MyAccountSignedOut import MyAccountSignedOut
import pytest


@pytest.mark.usefixtures("init_driver")
class Test_login_negative:

    @pytest.mark.tc1
    def test_login_negative(self):
        my_account=MyAccountSignedOut(self.driver)
        my_account.go_to_account()
        my_account.input_username("abjhbkbbb")
        my_account.input_password("liashoahs")
        my_account.click_login()

        error_message="Error: The username abjhbkbbb is not registered on this site. If you are unsure of your username, try your email address instead."
        my_account.err_message_displayed(error_message)




