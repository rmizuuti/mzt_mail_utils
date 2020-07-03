import smtplib
from email.mime.text import MIMEText


class Mailer:

    def __init__(self, smtp_server, smtp_port, login, senha):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.login = login
        self.senha = senha
        self.smtp = None

    def send_email(self, recipients, subject, text):
        try:
            self.__connect()
            msg = MIMEText(text)
            msg['Subject'] = subject
            msg['From'] = self.login
            msg['To'] = recipients
            self.smtp.sendmail(self.login, recipients, msg.as_string())
            self.smtp.close()
        except Exception as e:
            print('Failed to send e-mail. {}'.format(str(e)))

    def __connect(self):
        try:
            self.smtp = smtplib.SMTP_SSL(host=self.smtp_server, port=self.smtp_port)
            self.smtp.login(self.login, self.senha)
        except Exception as e:
            print('Failed to connect to SMTP server. {}'.format(str(e)))
