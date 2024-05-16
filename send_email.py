import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "nguyen.ppa740@gmail.com"
password = "ugierddfzpdjckbf"

receiver = "nguyen.ppa740@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Test Email
Umie
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)