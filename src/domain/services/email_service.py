from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from config.env import getEnvParams


class EmailService:
    def __init__(self):
        self.__config__ = getEnvParams()
        self.server = smtplib.SMTP(
            self.__config__["smtp"]["server"], self.__config__["smtp"]["port"]
        )
        self.server.starttls()
        self.server.login(
            self.__config__["smtp"]["username"], self.__config__["smtp"]["password"]
        )

    def sendEmail(
        self,
        to: str,
        body: str,
        subject: str,
    ):
        msg = MIMEMultipart()
        msg["From"] = self.__config__["smtp"]["username"]
        msg["To"] = to
        msg["Subject"] = subject

        msg.attach(MIMEText(body))

        self.server.sendmail(self.__config__["smtp"]["username"], to, msg.as_string())
