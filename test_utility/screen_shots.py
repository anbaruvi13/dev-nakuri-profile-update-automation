import datetime
from test_utility import create_log

class ScreenShot(object):
    @staticmethod
    def capture_screen_shot(driver, test_case_name):
        direcotry = "screen_shots/"
        path = direcotry + test_case_name + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")) + ".png"
        driver.get_screenshot_as_file(path)
        create_log.create_log("Screen Shot has been captured...")
