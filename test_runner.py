import time
import unittest
from HtmlTestRunner import HTMLTestRunner

from page_objects.pages.database_pages.report_to_database import ReportTODatabase
from test_scripts import t001_home_page
from test_utility import create_log
from multiprocessing import Process
import sys
import os
from shutil import copyfile
from page_objects.pages.excel_reports_write import excel_write

use_browser = os.environ.get("BROWSER")
print("Launching BROWSER: ", use_browser)

os.makedirs("logs/", exist_ok=True)
copyfile("input_files/execution_logs.html", "logs/execution_logs.html")
copyfile("input_files/execution_report.log", "logs/execution_logs.html")

os.makedirs("screen_shots/", exist_ok=True)
os.makedirs("reports/", exist_ok=True)


class MyTestSuite(unittest.TestCase):
    if use_browser == "chrome":
        def test_suite(self):
            start_time = time.time()
            design_status_page_script = unittest.TestLoader().loadTestsFromTestCase(t001_home_page.TestHomePage)

            suite = unittest.TestSuite(design_status_page_script)

            runner = HTMLTestRunner(output='reports', report_title='Test Case Execution Report',
                                    report_name='TestExecutionReport', verbosity=0, add_timestamp=True,
                                    combine_reports=False)
            runner.run(unittest.TestSuite(suite))

            # excel_obj = excel_write.ExcelWrite()
            # excel_obj.excel_write()
            # self.report_obj = ReportTODatabase()
            # self.report_obj.insert_report_to_database(float(time.time() - start_time))


if __name__ == '__main__':
    if use_browser == 'chrome':
        obj = MyTestSuite()
        p1 = Process(target=obj.test_suite())
