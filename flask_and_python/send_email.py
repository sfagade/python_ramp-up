from email.mime.text import MIMEText
import smtplib


def send_email(email_address, height, average_height, count):
    from_email = "saintwan@yahoo.com"
    from_password = "my_password"
    to_email = email_address

    subject = "Height Data"
    message = "Hey there, your height is <b>%s</b>. Average Height of all is %s and that is calculated out of %s " \
              " people." % (height, average_height, count)

    msg = MIMEText(message, "html")
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
