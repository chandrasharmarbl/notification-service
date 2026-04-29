# Notification Service

A lightweight Python service for sending notifications via email and SMS, built around a dependency-injected sender interface.

## Overview

`NotificationService` orchestrates notification delivery by delegating to pluggable sender implementations. Senders conform to the `INotificationSender` interface, making it straightforward to swap in real providers (SendGrid, Twilio, etc.) or test doubles.

## Notification Types

| Method | Channel | Description |
|---|---|---|
| `sendWelcomeNotification(recipient)` | Email | Sends a "Welcome!" message to a new user |
| `sendAlertNotification(message)` | SMS | Broadcasts an alert message to all recipients |
| `sendPromotion(recipient, message)` | Email | Sends a promotional message; failures are logged and swallowed |

## Project Structure

```
notification-service/
├── src/
│   └── notification_service.py   # NotificationService + INotificationSender
└── tests/
    └── test_notification_service.py
```

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (package manager)

## Setup

```bash
uv sync --group dev
```

## Running Tests

```bash
uv run pytest
```

## Usage

```python
from src.notification_service import NotificationService, INotificationSender

class MyEmailSender(INotificationSender):
    def send(self, recipient: str, message: str) -> None:
        # integrate with your email provider
        ...

class MySmsSender(INotificationSender):
    def send(self, recipient: str, message: str) -> None:
        # integrate with your SMS provider
        ...

service = NotificationService(
    email_sender=MyEmailSender(),
    sms_sender=MySmsSender(),
)

service.sendWelcomeNotification("alice@example.com")
service.sendAlertNotification("Deployment complete.")
service.sendPromotion("bob@example.com", "50% off this weekend!")
```
