import unittest
from HtmlTestRunner import HTMLTestRunner
from test_scripts import t001_home_page,t002_profile_page
import os
from shutil import copyfile

use_browser = os.environ.get("BROWSER")
print("Launching BROWSER: ", use_browser)

os.makedirs("logs/", exist_ok=True)
copyfile("input_files/execution_logs.html", "logs/execution_logs.html")
copyfile("input_files/execution_report.log", "logs/execution_logs.html")

os.makedirs("screen_shots/", exist_ok=True)
os.makedirs("reports/", exist_ok=True)


class MyTestSuite(unittest.TestCase):

    def test_suite(self):
        nakuri_profile_script = unittest.TestLoader().loadTestsFromTestCase(t002_profile_page.TestHotelPage)

        suite = unittest.TestSuite(nakuri_profile_script)

        runner = HTMLTestRunner(output='reports', report_title='Test Case Execution Report',
                                report_name='TestExecutionReport', verbosity=0, add_timestamp=True,
                                combine_reports=False)
        runner.run(unittest.TestSuite(suite))


if __name__ == '__main__':
    obj = MyTestSuite()
    obj.test_suite()
