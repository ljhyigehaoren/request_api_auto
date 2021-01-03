"""
    读取json数据
"""
import json
class OperationJson(object):

    def __init__(self,filepath):
        self.filepath = filepath

    def read_json_data(self,filename=None):
        with open(self.filepath+filename,"r",encoding="utf-8") as file:
            data = file.read()
        return json.loads(data)


if __name__ == '__main__':
    data = OperationJson("../data/").read_json_data("register.json")
    print(json.loads(data))
    print(type(json.loads(data)))





