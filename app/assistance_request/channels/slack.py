import requests
from .base_channel import BaseChannel
from app.core.logger import logger
from app.core.settings import settings


class SlackChannel(BaseChannel):
    def send(self, message: str):
        payload = {"text": message}
        logger.info(f"Sending message to Slack: {payload}")
        response = requests.post(settings.slack_webhook_url, json=payload)
        logger.info("Message sent to Slack")
        response.raise_for_status()
