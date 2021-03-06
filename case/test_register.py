"""
    目标：完成注册业务逻辑层实现
"""
from parameterized import parameterized
from case.request_base import *
from api.testbase import TestBase
# import unittest

class TestRegister(TestBase):
    """
        使用参数化时一定要注意：
        1.格式：列表套元组，
        2.元组内的元素顺序必须和方法中的参数顺序保持一致
    """

    @parameterized.expand(get_parameter_data("register_more.json"))
    def test_register(self,caseID,url,headers,data,expect_result,status_code):
        print(caseID+"正在执行...")
        self.case_module=caseID
        register(self,caseID,url,headers,data,expect_result,status_code)


if __name__ == '__main__':

    # unittest.main()
    pass
