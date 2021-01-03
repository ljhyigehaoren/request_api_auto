import pytest
# from unittest import mock
import mock
class TestCase(object):

    def hello(self):
        print("hello word")
        return 123

    def test_01(self):
        data={
            "status":200,
            "data":[
                {"name":"lisi"},
                {"name":"wangwu"}
            ]
        }
        self.hello = mock.Mock(return_value=data)
        result = self.hello()
        print(result)

        assert result["status"]==2000

    def test_02(self):
        data={
            "status":200,
            "data":[
                {"name":"lisi"},
                {"name":"wangwu"}
            ]
        }
        self.hello = mock.Mock(return_value=data)
        result = self.hello()
        print(result)

        assert result["status"]==200

    @pytest.mark.parametrize("num1,num2,result",
                             [[1, 2, .4], [2, 3, 5]])
    def test_03add(self, num1, num2, result):
        num3 = num1 + num2
        assert num3 == result





if __name__ == '__main__':
    # hello()
    a=1
    print(str(type(a))=="<class 'int'>")