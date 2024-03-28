import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("neeluyanna@gmail.com","wfaz qfzy qygb qvjm")
    msg=EmailMessage()
    msg["from"]="neeluyanna@gmail.com"
    msg["subject"]=subject
    msg["To"]=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()