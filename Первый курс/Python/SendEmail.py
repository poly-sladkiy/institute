import smtplib
from email.mime.text import MIMEText
from email.header    import Header

smtp_host = 'smtp.gmail.com'  # yahoo
login = "" # login, who will send e-mail
password =  "" # pswd
recipients_emails = "" # who will receive the message

msg = MIMEText('Тест', 'plain', 'utf-8')
msg['Subject'] = Header('Прога', 'utf-8')
msg['From'] = login
msg['To'] = recipients_emails

s = smtplib.SMTP(smtp_host, 587, timeout=10)
# s.set_debuglevel(1) # for debug
s.starttls()
s.login(login, password)

s.sendmail(msg['From'], recipients_emails, msg.as_string())

s.quit()