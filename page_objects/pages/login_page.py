import os

from test_utility.utility_methods import UtilMethods
from page_objects.locators.login_page_locator import LoginPageLocator


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.util_obj = UtilMethods(self.driver)
        self.user_name_text_box_xpath = LoginPageLocator.user_name_text_box_xpath
        self.user_password_text_box_xpath = LoginPageLocator.user_password_text_box_xpath
        self.login_button_xpath = LoginPageLocator.login_button_xpath
        self.home_screen_login_button_xpath = LoginPageLocator.home_screen_login_button_xpath


    def login_user_name(self,user_name):
        self.util_obj.clear_text_box(self.user_name_text_box_xpath)
        self.util_obj.send_keys(self.user_name_text_box_xpath, user_name)

    def login_user_password(self,password):
        self.util_obj.clear_text_box(self.user_password_text_box_xpath)
        self.util_obj.send_keys(self.user_password_text_box_xpath, password)

    # Y1Y4S8

    def login(self,user_name,password):
        print("This test run")
        self.util_obj.click_on_element(self.home_screen_login_button_xpath)
        self.login_user_name(user_name)
        self.login_user_password(password)
        self.util_obj.click_on_element(self.login_button_xpath)
        home_page_url = "https://www.naukri.com/mnjuser/homepage"
        if self.driver.current_url == home_page_url:
            result = True
            print("</br>","Page logged in Successfully..... ","</br>")

        else:
            result = False
            print("</br>","Login Failed....","</br>")

        return result

    def login_user_1(self):
        user_name = os.environ['Nakuri_User_Name']
        password = os.environ['Nakuri_Password']
        self.login(user_name,password)


