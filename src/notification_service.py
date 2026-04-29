from abc import ABC, abstractmethod


class INotificationSender(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass


class NotificationService:
    def __init__(self, email_sender: INotificationSender, sms_sender: INotificationSender):
        self.email_sender = email_sender
        self.sms_sender = sms_sender

    def sendWelcomeNotification(self, recipient: str) -> None:
        self.email_sender.send(recipient, "Welcome!")

    def sendAlertNotification(self, message: str) -> None:
        self.sms_sender.send("broadcast", message)

    def sendPromotion(self, recipient: str, message: str) -> None:
        try:
            self.email_sender.send(recipient, message)
        except Exception:
            pass
