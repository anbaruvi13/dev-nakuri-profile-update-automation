from page_objects.pages.design_status_page import DesignStatusPage
from test_environment.environment_setup import EnvironmentSetup
import time
from test_utility import create_log, screen_shots
from test_utility.utility_methods import UtilMethods


class TestHomePage(EnvironmentSetup):

    def setUp(self):
        self.startTime = time.time()
        self.util_obj = UtilMethods(self.driver)
        self.design_page_obj = DesignStatusPage(self.driver)
        self.result = None
        create_log.create_log(self.id() + ' ' + 'Started...')

    def tearDown(self):
        test_method_name = self._testMethodName
        if self.result is not True:
            screen_shots.ScreenShot.capture_screen_shot(self.driver, test_method_name)
        t = float(time.time() - self.startTime)
        execution_time = self.util_obj.execution_time(t)
        create_log.create_log(self.id() + ' ' + 'completed' + str(create_log.logic_for_pass_fail_error(self.result)))


    def test_001_design_status_check(self):
        self.result = self.design_page_obj.design_status_check()
        self.assertTrue(self.result)
