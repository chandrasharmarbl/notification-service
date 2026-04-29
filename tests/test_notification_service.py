import pytest                                                                                                                                                                                                      
from notification_service import NotificationService, INotificationSender                                                                                                                                          
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
class TestNotificationService:                                                                                                                                                                                     
                
    def test_send_welcome_notification_calls_email_sender_with_correct_recipient(self, mocker):
        email_sender = mocker.MagicMock(spec=INotificationSender)
        sms_sender = mocker.MagicMock(spec=INotificationSender)                                                                                                                                                    
        service = NotificationService(email_sender, sms_sender)
                                                                                                                                                                                                                    
        service.sendWelcomeNotification("alice@example.com")
                                                                                                                                                                                                                    
        email_sender.send.assert_called_once_with("alice@example.com", "Welcome!")

