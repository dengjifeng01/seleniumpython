#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Test_eamil(object):
    def __init__(self):
        self.mail_houst = "smtp.qq.com"
        self.mail_user = "1535268384@qq.com"
        self.mail_passwrod = "nbjpsqffjqepbadi"

        self.sender = "1535268384@qq.com"
        self.receivers = "dengzyy@foxmail.com"

    #编辑发送内容
    def send_eamil(self):
        message = MIMEMultipart()
        message["From"] = Header("TEST111","utf-8")
        message["To"] = Header("TEST",'utf-8')
        message["Subject"] = Header("Python SMTP 测试！！！")
        message.attach(MIMEText("ceshiwenjian"))
        att1 = MIMEText(open("start.py","rb").read(),"base64","utf-8")
        att1["Content-Type"] = "application/octet-stream"
        att1["Content-Disposition"] = "attachment;filename='text.py'"
        message.attach(att1)
        return message

    #发送邮件
    def main(self):
        message = self.send_eamil()
        smtp = smtplib.SMTP()
        smtp.connect(self.mail_houst)
        smtp.login(self.mail_user,self.mail_passwrod)
        smtp.sendmail(self.sender,self.receivers,message.as_string())

if __name__ == "__main__":
    t = Test_eamil()
    t.main()
