from test_utility.utility_methods import UtilMethods
from page_objects.locators.login_page_locator import LoginPageLocator


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.util_obj = UtilMethods(self.driver)
        self.user_name_text_box_xpath = LoginPageLocator.user_name_text_box_xpath
        self.user_password_text_box_xpath = LoginPageLocator.user_password_text_box_xpath
        self.login_button_xpath = LoginPageLocator.login_button_xpath
        self.home_screen_login_button_xpath = LoginPageLocator.home_screen_login_button_xpath