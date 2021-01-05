import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.configdata import GlobalVar

class SendEmail:
    def __init__(self):
        self.send_user = None
        self.send_user_name = None
        self.email_host = None
        self.password = None

    def send_mail(self,htmlrunner_path,user_list,sub,content,send_case_excel=False):
        user = self.send_user_name + "<" + self.send_user + ">"

        msg = MIMEMultipart()
        # 发送邮件的对象
        sub_message1 = MIMEText(content,_subtype="plain",_charset="utf-8")
        msg.attach(sub_message1)

        # 根据send_case_excel参数判断是否需要发送测试用例,默认为False：不发送
        if send_case_excel:
            # 发送测试用例
            sub_message2 = MIMEText(open(GlobalVar.API_CASE_PATH, 'rb').read(), 'base64', 'utf-8')
            sub_message2["Content-Type"] = 'application/octet-stream'
            sub_message2.add_header('content-disposition', 'attachment', filename=('utf-8', '', 'case.xlsx'))
            msg.attach(sub_message2)

        # 发送测试用例执行结果HTML文件
        sub_message3 = MIMEText(open(htmlrunner_path, 'rb').read(), 'html', 'utf-8')
        sub_message3["Content-Type"] = 'application/octet-stream'
        sub_message3.add_header('content-disposition', 'attachment',filename=('utf-8', '','report.html'))
        msg.attach(sub_message3)

        # 邮件的主题
        msg["Subject"] = Header(sub,'utf-8')
        # 邮件的发送者
        msg["From"] = Header(user,'utf-8')
        # 邮件的接收者
        msg["To"] = Header(";".join(user_list),'utf-8')
        # 发送方邮件服务器对象
        server = smtplib.SMTP()
        try:
            # 连接发送方邮件服务器
            server.connect(self.email_host)
            # 登录邮箱
            server.login(self.send_user,self.password)
            # 执行发送邮件的动作
            server.sendmail(user,user_list,msg.as_string())
            print("发送邮件成功")
        except Exception as e:
            print("发送邮件失败,错误原因:{}".format(repr(e)))
        finally:
            # 关闭连接
            server.close()

    def send_case_result_email(self,htmlrunner_path,pass_count,fail_count,sub=None,send_case_excel=False):
        print("正在发送测试用例结果...")
        self.send_user = GlobalVar.EMAIL_SEND_USER
        self.send_user_name = GlobalVar.EMAIL_SEND_USERNAME
        self.password = GlobalVar.EMAIL_PASSWORD
        self.email_host = GlobalVar.EMAIL_HOST
        user_list = GlobalVar.EMAIL_USERLIST
        if sub == None:
            sub = GlobalVar.EMAIL_SUB
        total_count = pass_count+fail_count
        content = """
        本次共执行测试用例%s条，其中失败条数%s，成功条数%s，
        通过率%.2f%%,失败率%.2f%%。
        详情请下载html附件，在浏览器中查看。
        """ % (
            total_count,
            fail_count,
            pass_count,
            (float(pass_count) / total_count * 100),
            (float(fail_count) / total_count * 100),
        )
        self.send_mail(htmlrunner_path,user_list, sub, content,send_case_excel=send_case_excel)


if __name__ == '__main__':
    pass

