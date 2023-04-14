#Imports
from email.message import EmailMessage
from emailpassword import email, password
import ssl
import smtplib

email_sender = email
email_password = password

email_receiver = str(input("Who do you want to send this e-mail to?\n"))


#Creating E-mail
subject = str(input('Write the subject of the email:\n'))
body = str(input('Write your e-mail:\n'))

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#Sending e-mail:
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())