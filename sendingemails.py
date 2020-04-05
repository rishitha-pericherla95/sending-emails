import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('./index.html').read_text())
email = EmailMessage()
email['from'] = 'Rishitha'
email['to'] = 'rishitha.pericherla@gmail.com'
email['subject'] = 'This is a demo mail'
email.set_content(html.substitute(name="Rishitha"),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    #hello
    smtp.ehlo()
    #securtity encryption
    smtp.starttls()
    smtp.login('rishithadata@gmail.com','Mclaren@2010')
    smtp.send_message(email)
    print("email sent")