import pytest                                                                                                                                                                                                      
from src.notification_service import NotificationService, INotificationSender                                                                                                                                          
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
class TestNotificationService:                                                                                                                                                                                     
                
    def test_send_welcome_notification_calls_email_sender_with_correct_recipient(self, mocker):
        email_sender = mocker.MagicMock(spec=INotificationSender)
        sms_sender = mocker.MagicMock(spec=INotificationSender)                                                                                                                                                    
        service = NotificationService(email_sender, sms_sender)
                                                                                                                                                                                                                    
        service.sendWelcomeNotification("alice@example.com")
                                                                                                                                                                                                                    
        email_sender.send.assert_called_once_with("alice@example.com", "Welcome!")

    def test_send_alert_notification_calls_sms_sender_with_correct_message(self, mocker):
        email_sender = mocker.MagicMock(spec=INotificationSender)
        sms_sender = mocker.MagicMock(spec=INotificationSender)
        service = NotificationService(email_sender, sms_sender)

        service.sendAlertNotification("System is down!")

        sms_sender.send.assert_called_once_with("broadcast", "System is down!")

    def test_send_promotion_handles_email_sender_exception_gracefully(self, mocker):
        email_sender = mocker.MagicMock(spec=INotificationSender)
        sms_sender = mocker.MagicMock(spec=INotificationSender)
        email_sender.send.side_effect = Exception("SMTP failure")
        service = NotificationService(email_sender, sms_sender)

        service.sendPromotion("bob@example.com", "50% off!")
