import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from test_utility import create_log
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os


class EnvironmentSetup(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(self):
        use_browser = os.environ.get("BROWSER").lower()
        print("Select browser is " + use_browser)

        if use_browser == 'ie':
            create_log.create_log("Execution started in Internet Explorer...")
            self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            ie_driver = "web_drivers/IEDriverServer.exe"
            self.driver = webdriver.Ie(ie_driver)
            create_log.create_log("Internet Explorer opened successfully")
        elif use_browser == 'chrome':
            create_log.create_log("Execution started in Chrome...")
            # chrome_driver = "web_drivers/chromedriver.exe"
            # self.driver = webdriver.Chrome(chrome_driver)
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            create_log.create_log("Chrome opened successfully")
            # Confirm once the driver works correctly
        elif use_browser == 'firefox':
            create_log.create_log("Execution started in Firefox...")
            firefox_driver = "web_drivers/chromedriver.exe"
            self.driver = webdriver.Firefox(firefox_driver)
            create_log.create_log("Firefox opened successfully")

        else:
            create_log.create_log(
                "Execution started in chrome since valid browser was not selected in the config file...")
            chrome_driver = "web_drivers/chromedriver.exe"
            self.driver = webdriver.Chrome(chrome_driver)

        self.driver.maximize_window()
        base_url = "https://www.google.com/"
        self.driver.get(base_url)
        create_log.create_log("Home Page Loading...")
        self.driver.implicitly_wait(10)

    def tally(self):
        return len(self._reslutForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    @classmethod
    def tearDownClass(self):
        if self.driver != None:
            self.driver.close()
            self.driver.quit()
            pass
