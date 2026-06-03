from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from typing import Sequence

from utils.get_cv_files import File

def _create_message_as_text(
    send_from_address: str,
    send_to_address: str | Sequence[str],
    subject: str,
    body: str,
    files_bytes: Sequence[File] 
) -> str:
    msg = MIMEMultipart()
    msg['From'] = send_from_address
    msg['To'] = send_to_address
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    for file in files_bytes:
        msg.attach(
            MIMEApplication(
                file.bytes,
                Name=file.basename
            )
        )
    
    return msg.as_string()

def send_email_from_mail_ru(
    send_from_address: str,
    send_to_address: str | Sequence[str],
    password: str,
    subject: str,
    body: str,
    files_bytes: Sequence[File]
) -> str:
    log = ''
    server = smtplib.SMTP('smtp.mail.ru', 25)
    log += server.starttls().__str__() + '\n'
    log += server.login(send_from_address, password).__str__() + '\n'
    text = _create_message_as_text(
        send_from_address,
        send_to_address,
        subject,
        body,
        files_bytes 
    )
    log += server.sendmail(send_from_address, send_to_address, text).__str__() + '\n'
    server.quit()
    return log

def send_email_from_gmail(
    send_from_address: str,
    send_to_address: str | Sequence[str],
    password: str,
    subject: str,
    body: str,
    files_bytes: Sequence[File]
) -> str:
    log = ''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    log += server.starttls().__str__() + '\n'
    log += server.login(send_from_address, password).__str__() + '\n'
    text = _create_message_as_text(
        send_from_address,
        send_to_address,
        subject,
        body,
        files_bytes 
    )
    log += server.sendmail(send_from_address, send_to_address, text).__str__() + '\n'
    server.quit()
    return log