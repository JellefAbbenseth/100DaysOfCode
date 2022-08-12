import smtplib


class Mail:
    def __init__(self, receiver: str, sender: str, password: str):
        self.smtp_host = "imap.gmx.net"
        self.receiver = receiver
        self.sender = sender
        self.password = password
        self.text_header = "text_header"
        self.text_body = "text_body"

    def sent_mail(self, text_header: str, text_body: str):
        try:
            with smtplib.SMTP(self.smtp_host) as connection:
                connection.starttls()
                connection.login(user=self.sender, password=self.password)
                connection.sendmail(
                    from_addr=self.sender,
                    to_addrs=self.reciever,
                    msg=f"{text_header}\n\n{text_body}"
                )
        except ConnectionRefusedError:
            print(f"\n{text_body}")


