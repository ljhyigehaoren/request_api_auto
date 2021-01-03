from api.api_post import ApiPost
from tools.operation_json import OperationJson
from config.configdata import GlobalVar

def get_parameter_data(json_file_name):
    data = OperationJson(GlobalVar.API_DATAPATH).read_json_data(json_file_name)
    arr = []
    for key,value in data.items():
        arr.append((
            key,
            value.get("url"),
            value.get("headers"),
            value.get("data"),
            value.get("expect_result"),
            value.get("status_code"),
        ))
    return arr


def login(cls,caseID,url,headers,data,expect_result,status_code,is_return=False):
    """
    用户登录
    :param cls:
    :param caseID:
    :param url:
    :param headers:
    :param data:
    :param expect_result:
    :param status_code:
    :param is_return:
    :return:
    """
    response = ApiPost().api_post(
        url=url,
        data=data,
        headers=headers,
        caseID=caseID,
    )

    print("预期结果：", expect_result)
    if str(type(response))=="<class 'int'>":
        if is_return == False:
            cls.assertEqual(1,0)
        else:
            return response
    else:
        if is_return == False:
            cls.assertEqual(status_code, response.status_code)
            if caseID == "readbook_login015":
                cls.assertIn(expect_result, response.json().get("msg"))
            else:
                cls.assertDictEqual(expect_result, response.json())
        else:
            return response

def register(cls,caseID,url,headers,data,expect_result,status_code,is_return=False):
    """
    用户注册
    :param cls:
    :param caseID:
    :param url:
    :param headers:
    :param data:
    :param expect_result:
    :param status_code:
    :param is_return:
    :return:
    """
    response = ApiPost().api_post(
        url=url,
        data=data,
        headers=headers,
        caseID=caseID
    )
    print("预期结果：", expect_result)
    if str(type(response))=="<class 'int'>":
        print(response)
        if is_return == False:
            cls.assertEqual(1,0)
        else:
            return response
    else:
        if is_return == False:
            cls.assertEqual(status_code, response.status_code)
            cls.assertDictEqual(expect_result, response.json())
            # self.assertIn("This field is required.",response.json()["birthday"][0])
            # self.assertIn("This field may not be blank.", response.json()["account"][0])
            # self.assertIn("This field may not be blank.", response.json()["password"][0])
        else:
            return response

