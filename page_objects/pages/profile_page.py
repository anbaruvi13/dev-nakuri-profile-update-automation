from time import sleep

from test_utility.utility_methods import UtilMethods
from page_objects.locators.profile_page_locator import ProfilePageLocator


class ProfilePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.util_obj = UtilMethods(self.driver)
        self.resume_headline_button_xpath = ProfilePageLocator.resume_headline_button_xpath
        self.resume_headline_edit_button_xpath = ProfilePageLocator.resume_headline_edit_button_xpath
        self.resume_headline_text_box_xpath = ProfilePageLocator.resume_headline_text_box_xpath
        self.resume_updated_button_xpath = ProfilePageLocator.resume_updated_button_xpath
        self.resume_headline_save_button_xpath = ProfilePageLocator.resume_headline_save_button_xpath
        self.resume_headline_cancel_button_xpath = ProfilePageLocator.resume_headline_cancel_button_xpath
        self.view_profile_button_xpath = ProfilePageLocator.view_profile_button_xpath
        self.view_profile_logout_xpath = ProfilePageLocator.view_profile_logout_xpath
        self.view_profile_in_home_page_button_xpath = ProfilePageLocator.view_profile_in_home_page_button_xpath

    def change_profile_head_line(self):
        self.util_obj.click_on_element(self.view_profile_in_home_page_button_xpath)
        value = "Automation Test Engineer Driving Quality and Efficiency through Test Automation Solutions"
        self.util_obj.click_on_element(self.resume_headline_edit_button_xpath)
        sleep(10)
        self.util_obj.send_keys_with_clear_text(self.resume_headline_text_box_xpath, value)
        self.util_obj.click_on_element(self.resume_headline_save_button_xpath)
        self.util_obj.click_on_element(self.view_profile_button_xpath)
        sleep(10)
        self.util_obj.click_on_element(self.view_profile_logout_xpath)
        home_page_url = "https://www.naukri.com/"
        if self.driver.current_url == home_page_url:
            result = True
            print("Logged Out Successfully....")

        else:
            result = False
            print("Logged Out Failed....")

        return result
