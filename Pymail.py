import smtplib
import configparser
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

def send_email():
    config = read_config('config_email.txt')

    sender_email = config['Email']['sender_email']
    sender_password = config['Email']['sender_password']
    recipient_emails = config['Email']['recipient_emails'].split(', ')
    cc_emails = config['Email'].get('cc_emails', '').split(', ')
    bcc_emails = config['Email'].get('bcc_emails', '').split(', ')

    subject = config['Message']['subject']
    with open(config['Message']['body_file'], 'r') as file:
        body = file.read()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_emails)
    msg['Cc'] = ', '.join(cc_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    attachment_paths = config['Attachments']['attachment_paths'].split(', ')
    for attachment_path in attachment_paths:
        with open(attachment_path, 'rb') as f:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(f.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(attachment)

    all_recipients = recipient_emails + cc_emails + bcc_emails

    server.sendmail(sender_email, all_recipients, msg.as_string())

    server.quit()

if __name__ == "__main__":
    send_email()
