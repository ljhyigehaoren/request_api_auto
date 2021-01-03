"""
    目标：
        1.搜索组装测试套件
        2.运行测试套件并且生成测试报告
"""

import unittest,time
from tools.send_email import SendEmail
# from HtmlTestRunner import HTMLTestRunner
# from tools.html_testreport_cn import HTMLTestRunner
from tools.beauty_testreport import HTMLTestReport
class Runner(object):

    def __init__(self):
        self.email = SendEmail()

    def run_case(self):
        # 第一步：组装测试套件
        suite = unittest.defaultTestLoader.discover("./case",pattern="test*.py")

        # suite.addTests()
        # 第二步：指定测试报告的生成路径和文件名称
        report_path = "./report/readbook_%s.html" % (time.strftime("%Y%m%d%H%M%S"))

        # 第三步：运行测试套件并生成测试报告
        with open(report_path,"wb") as file:
            # test_runner = HTMLTestRunner(stream=file,description="测试用例报告",title="readbook_api_auto_report")
            test_runner = HTMLTestReport(
                stream=file,
                description="测试用例报告",
                title="readbook_api_auto_report",
                tester="李居豪",
            )
            result = test_runner.run(suite)

        # 获取执行成功、失败的测试用例
        success_count = result.success_count
        failure_count = result.failure_count
        error_count = result.error_count
        total = result.success_count + result.failure_count + result.error_count
        print(
            "共:",total,"条;",
            "成功:",success_count,"条;",
            "失败:",failure_count,"条;",
            "错误:",error_count,"条;",
        )

        #将测试结果发送给指定用户
        self.email.send_case_result_email(
            report_path,
            success_count,
            failure_count+error_count,
        )

if __name__ == '__main__':
    runner = Runner()
    runner.run_case()
