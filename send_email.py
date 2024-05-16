import smtplib, ssl


def send_email(message):
    port = 465
    smtp_server = "smtp.gmail.com"

    password = "ugierddfzpdjckbf"
    sender_email = "nguyen.ppa740@gmail.com"

    recipient_email = "nguyen.ppa740@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message)





