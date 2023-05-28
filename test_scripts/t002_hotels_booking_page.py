from page_objects.pages.login_page import LoginPage
from page_objects.pages.search_hotels_page import SearchHotelPage
from test_environment.environment_setup import EnvironmentSetup
import time
from test_utility import create_log, screen_shots
from test_utility.utility_methods import UtilMethods


class TestHotelPage(EnvironmentSetup):

    def setUp(self):
        self.startTime = time.time()
        self.util_obj = UtilMethods(self.driver)
        self.login_page_obj = LoginPage(self.driver)
        self.hotel_page_obj = SearchHotelPage(self.driver)
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
        self.login_page_obj.login_user_1()
        self.result = True
        self.assertTrue(self.result)

    def test_002_search_for_hotels_and_book_in_sydney(self):
        self.result = self.hotel_page_obj.search_for_hotels_and_book_in_sydney()
        self.assertTrue(self.result)
