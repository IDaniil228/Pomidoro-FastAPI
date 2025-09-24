from Schema import EmailMessage
from setting import Setting
from worker.celery import send_welcome_mail

from faststream.rabbit import RabbitBroker

class MailClient:

    def __init__(self):
        self.setting = Setting()


    async def send_welcome_message(self, to_mail : str) -> None:
        broker = RabbitBroker(self.setting.BROKER_URL)
        msg = EmailMessage(
            text = "Спасибо за регистрацию",
            subject = "Welcome",
            to_mail = to_mail,
        )
        await broker.connect()

        response = await broker.publish(
            message=msg,
            queue="email-queue"
        )
        print(f"Message sent: {response}")

        await broker.stop()



        #send_welcome_mail.delay("Welcome", "Thanks for registering", to_mail)


