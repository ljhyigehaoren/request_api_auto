"""
    用户注册接口封装
"""
import requests
from tools.log import log_message
class ApiPost(object):

    def api_post(self,url,data,caseID,headers=None,timeout=(3,2)):
        if headers == None:
            headers = {"Content-Type":"application/json"}
        try:
            res = requests.post(url,json=data,headers=headers,timeout=timeout)
            print("实际结果：",res.text)
            return res
        except Exception as e:
            log_message.instance(caseID).error_log(message=e)
            print("实际结果：", e)
            return 0
