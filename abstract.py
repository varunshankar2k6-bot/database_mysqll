from abc import ABC, abstractmethod
class Notification(ABC):
    def __init__(self, sender):
        self.sender = sender
    @abstractmethod
    def send(self, message):
        pass
class EmailNotification(Notification):
    def send(self, message):
        print(f"Email from {self.sender}: {message}")
class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS from {self.sender}: {message}")
class WhatsAppNotification(Notification):
    def send(self, message):
        print(f"WhatsApp from {self.sender}: {message}")
notifications = [EmailNotification("Admin"),SMSNotification("HR"),WhatsAppNotification("Boss")]
for n in notifications:
    n.send("Meeting at 10 AM")