from selenium.webdriver.chrome import webdriver

from page_objects.pages.web_page.home_page import Home
from page_objects.pages.web_page.login_page import LoginPage
from test_environment.environment_setup import EnvironmentSetup
import time
from test_utility import create_log, screen_shots
from test_utility.utility_methods import UtilMethods


class TestHomePage(EnvironmentSetup):

    def setUp(self):
        driver = self.driver
        self.startTime = time.time()
        self.util_obj = UtilMethods(self.driver)
        self.home_page_obj = Home(self.driver)
        self.page_obj = LoginPage(self.driver)
        self.result = None
        create_log.create_log(self.id() + ' ' + 'Started...')

    def tearDown(self):
        test_method_name = self._testMethodName
        if self.result is not True:
            screen_shots.ScreenShot.capture_screen_shot(self.driver, test_method_name)
        t = float(time.time() - self.startTime)
        execution_time = self.util_obj.execution_time(t)
        create_log.create_log(self.id() + ' ' + 'completed' + str(create_log.logic_for_pass_fail_error(self.result)))

    def test_001_login(self):
        self.page_obj = LoginPage(self.driver)
        self.page_obj.login_1()
        self.result = True
        self.assertTrue(self.result)

    def test_002_crm_dashboard_page(self):
        self.result = self.home_page_obj.home_page_login()
        self.assertTrue(self.result)
