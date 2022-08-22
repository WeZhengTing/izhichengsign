import smtplib
from email.mime.text import MIMEText
from email.header import Header
from  Izhichen import izhichen

class Mail:
    def __init__(self):
        # 第三方 SMTP 服务

        self.mail_host="smtp.qq.com"       #设置服务器:这个是qq邮箱服务器，直接复制就可以
        self.mail_pass="spuhpmjvmikjdgij"           #刚才我们获取的授权码
        self.sender = '2946073318@qq.com'      #你的邮箱地址
        self.receivers = ['3014829930@qq.com']  # 收件人的邮箱地址

    def send(self):

        content = '签到成功啦'
        message = MIMEText(content, 'plain', 'utf-8')

        message['From'] = Header("健康日报", 'utf-8')
        message['To'] = Header("自己", 'utf-8')

        subject = '日报通知'  # 发送的主题，可自由填写
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()
            izhichen('212104127','苏睿宁')
            print("OK滚去睡觉吧")
        except smtplib.SMTPException as e:
            print("快自己起床签到")


    def sendfalse(self):

        content = '签到失败啦'
        message = MIMEText(content, 'plain', 'utf-8')

        message['From'] = Header("自己哦", 'utf-8')
        message['To'] = Header("自己", 'utf-8')

        subject = '日报通知'  # 发送的主题，可自由填写
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()
            print("OK滚去睡觉吧")
        except smtplib.SMTPException as e:
            print("快自己起床签到")



if __name__ == '__main__':
    try:
        mail = Mail()
        mail.send()
    except:
        mail.sendfalse()
        #打包pyinstaller -F -w signIzhichen.py
