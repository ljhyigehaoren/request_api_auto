"""
    在这里添加全局的变量
"""

class GlobalVar(object):
    # 数据库配置
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT= 6379
    MYSQL_USER="root"
    MYSQL_PASSWPRD="12345678"
    MYSQL_DATABASE="readbook"
    MYSQL_CHARSET="utf8"

    # 数据驱动文件目录
    API_DATAPATH = "./data/"
    # 测试用例存储路径
    API_CASE_PATH = "./case/readbookcases.xlsx"

    # 发送邮件配置
    EMAIL_SEND_USER = "2295808193@qq.com"
    EMAIL_SEND_USERNAME = "小青年"
    EMAIL_PASSWORD = "klnrulxakulmebdi"
    EMAIL_HOST = "smtp.qq.com"
    EMAIL_USERLIST = ["2295808193@qq.com", "ljhyigehaoren@sina.com"]
    EMAIL_SUB = "readbook_api_auto_report"

