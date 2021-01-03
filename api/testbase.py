import unittest
class TestBase(unittest.TestCase):
    case_module = ""
    def setUp(self):
        self.case_module=""

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print(self.case_module+"执行完毕...")