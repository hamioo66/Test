# -*- coding: UTF-8 -*-
from email.mime.text import MIMEText
import smtplib
#发邮件的库

#smit的服务器
SMTPServer = "smtp.163.com"
#发邮件的地址
Sender = "你的163邮件的地址"
#发送者的密码
passwd = "163邮件的授权密码"

#设置发送的内容
message = "sunck is a man"
#转化为邮件的文本
msg = MIMEText(message)

#主体
msg["Subject"] = "来自猩猩的呵呵"
#发送者
msg["From"] = Sender

#一般邮件的端口号是25
#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25)

#登录邮箱
mailServer.login(Sender,passwd)

#发送邮件
mailServer.sendmail(Sender,["想发的邮件地址"],msg.as_string())

#退出邮箱
mailServer.quit()
