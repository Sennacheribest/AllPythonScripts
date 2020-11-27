""" Python function to send a basic email notification. """

import smtplib

sender_email = "sennacheribest@gmail.com"
sender_passwd = "Your password"

def send_mail(receiver, subject, body):
    message = "Subject: {}\n\n{}".format(subject, body)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_passwd)
        server.sendmail(sender_email, receiver, message)
