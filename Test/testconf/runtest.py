import os
from uitlsfunction import readdate, readcounter

reportFolderName = f"{readdate()}_{readcounter()}"

# For running testCases
command = f"pytest -s --alluredir=ReportAllure/{reportFolderName} --html=ReportHtml/report_{reportFolderName}.html --self-contained-html testcase"
# command = f"pytest -s testcase/skype"
# command = f"pytest -s testcase/whatsapp/test_whatsapp_00_whatsapp_number_checker.py"
# command = f"pytest -s --reruns 5 --reruns-delay 5 testcase/whatsapp/test_whatsapp_00_whatsapp_number_checker_for_escaped_number.py"
# command = f"pytest -s --reruns 500 --reruns-delay 5 testcase/whatsapp/test_whatsapp_00_whatsapp_number_checker_for_escaped_number.py"
# command = f"pytest -s testcase/gchat"
os.system(command)

#  Send email
# sender = ''
# password = ''
# receivers = ''
# sendemail(sender, password, receivers)

# number of allure & html reports to keep
# number = 2
# keepreports(number)

# For generating report
# command = f"allure serve ReportAllure/{reportFolderName}"
# os.system(command)
