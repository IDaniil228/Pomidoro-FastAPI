from email.mime.multipart import MIMEMultipart
import ssl
import smtplib
from email.mime.text import MIMEText

from celery import Celery

from setting import Setting

setting = Setting()

celery = Celery(__name__)
# celery.conf.broker_url = setting.CELERY_BROKER_URL
# celery.conf.result_backend = "rpc://"

celery.conf.update(
    broker_url=setting.BROKER_URL,
    result_backend='rpc://',
    worker_pool='solo',
    task_always_eager=False,
)


@celery.task(name="send_welcome_mail")
def send_welcome_mail(subject: str, text: str, to_mail: str):
    msg = _build_message(subject=subject, text=text, to_mail=to_mail, from_mail=setting.FROM_MAIL)
    _send_mail(msg=msg)

def _build_message(subject: str, text: str, to_mail: str, from_mail: str) -> MIMEMultipart:
    msg = MIMEMultipart()

    msg["From"] = from_mail
    msg["To"] = to_mail
    msg["Subject"] = subject
    msg.attach(MIMEText(text, _subtype="plain"))
    return msg

def _send_mail(msg: MIMEMultipart) -> None:
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(host=setting.SMTP_HOST, port=setting.SMTP_PORT, context=context)
    server.login(setting.FROM_MAIL, password=setting.SMTP_PASSWORD)
    server.send_message(msg)
    server.quit()