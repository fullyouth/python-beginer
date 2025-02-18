import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email(sender_email, sender_password, receiver_emails, 
               subject, message, message_type='plain', 
               attachments=None, smtp_server='smtp.gmail.com', 
               smtp_port=587):
    """
    发送电子邮件
    
    参数：
    sender_email -- 发件人邮箱
    sender_password -- 发件人邮箱密码/授权码
    receiver_emails -- 收件人邮箱列表
    subject -- 邮件主题
    message -- 邮件正文内容
    message_type -- 内容类型：'plain'（默认）或 'html'
    attachments -- 附件文件路径列表（可选）
    smtp_server -- SMTP服务器地址（默认Gmail）163 smtp.163.com
    smtp_port -- SMTP服务器端口（默认587）
    """
    
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_emails)
    msg['Subject'] = subject

    # 添加邮件正文
    body = MIMEText(message, message_type)
    msg.attach(body)

    # 添加附件
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(attachment))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
            msg.attach(part)

    try:
        # 连接SMTP服务器并发送邮件
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # 启用安全传输模式
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_emails, msg.as_string())
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")

# 使用示例
if __name__ == "__main__":
    # 配置信息（需要修改以下信息）
    """
        1. 前置条件准备
        登录 网易163邮箱网页版
        进入「设置」→「POP3/SMTP/IMAP」
        开启以下两个选项：
        POP3/SMTP服务
        IMAP/SMTP服务
        点击「客户端授权密码」→「开启」→ 通过手机验证获取 16位授权码（示例：ABCDabcd1234efgh）
    """
    config = {
        'sender_email': 'fullyouth@163.com',  # 发件人邮箱
        'sender_password': '你自己的邮箱专用码',      # 邮箱密码或应用专用密码
        'receiver_emails': ['1075955128@qq.com'],
        'subject': '自动发送测试邮件',
        'message': '<h1>这是一封通过Python自动发送的测试邮件。</h1>',
        'message_type': 'html',  # 可选 'html'
        'attachments': [],  # 附件路径列表
        'smtp_server': 'smtp.163.com',
        'smtp_port': 25         # 或 465
    }

    # 发送邮件
    send_email(**config)