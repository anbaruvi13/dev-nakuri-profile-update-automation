from datetime import datetime
import webbrowser


def create_log(test_name):
    test_name = str(test_name)
    now = datetime.now()
    current_time = now.strftime("%m-%d-%Y %H:%M:%S")
    file_name = "logs/" + "execution_report" + ".log"
    # line_prepender(file_name, current_time + ' ' + str(test_name) + '\n')


def line_prepender(file_name, line):
    with open(file_name, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rsplit('\r\n') + '\n' + str(content))
        f.close()


def initialize_log():
    file_name = "logs/" + "execution_report" + ".log"
    f = open(file_name, 'r+')
    f.truncate(0)
    f.close()
    # url = r'https://search.ipindia.gov.in/DesignApplicationStatus'
    # webbrowser.open(url, new=2)


def logic_for_pass_fail_error(result):
    if result == True:
        return "Passed. "
    elif result == False:
        return "Failed. "
    else:
        return "Error. "
