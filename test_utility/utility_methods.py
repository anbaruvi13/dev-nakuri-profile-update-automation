from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UtilMethods(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(self.driver, 30)

    def dropdown_visible_text(self, locator, text):
        # common method to select a value from the dropdown menu
        # Explicit waits the execution until 30 sec or till the dropdown is visible
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

        except Exception as e:
            print(e)

        select = Select(self.driver.find_element(By.XPATH, locator))
        sleep(0.5)
        select.select_by_visible_text(text)

    def click_on_element(self, locator):
        # Normal Click action Performed
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

        except Exception as e:
            print(e)
        self.driver.find_element(By.XPATH, locator).click()

    def click_on_element_using_js(self, locator):
        # Click action using JavaScript method
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

        except Exception as e:
            print(e)
        sleep(0.5)
        self.driver.execute_script("argument[0].click();", self.driver.find_element(By.XPATH, locator))

    def send_keys(self, locator, value):

        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

        except Exception as e:
            print(e)
        sleep(0.5)
        self.driver.find_element(By.XPATH,locator).send_keys(value)

    def clear_text_box(self, locator):

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

        except Exception as e:
            print(e)
        sleep(0.5)
        self.driver.find_element(By.XPATH, locator).clear()

    def send_keys_with_clear_text(self, locator, value):

        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

        except Exception as e:
            print(e)
        sleep(0.5)
        self.driver.find_element(By.XPATH, locator).clear()
        self.driver.find_element(By.XPATH, locator).send_keys(value)

    def get_text(self, locator):
        text = ""
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            text = self.driver.find_element(By.XPATH,locator).text
        except Exception as e:
            print(e)
            pass
        return text

    def is_displayed(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

        except Exception as e:
            print(e)
        sleep(0.5)
        element = self.driver.find_element(By.XPATH,locator)
        return element.is_displayed

    def execution_time(self, end_time):
        # Method to find the time taken for an TestCase to Execute
        # If end time is converted into minus from seconds
        if end_time > 60:
            mins = int(end_time / 60)
            secs = end_time % 60
            return "Execution Time: " + str(mins) + "mins %.2f" % secs + "s"
        else:
            return "Execution Time: %.2f" % end_time + "s"
