import requests
from app.config import settings
from app.services.channel import Channel
from app.logger import logger


class SlackChannel(Channel):
    def send(self, message: str):
        payload = {"text": message}
        logger.info(f"Sending message to Slack: {payload}")
        response = requests.post(settings.slack_webhook_url, json=payload)
        logger.info("Message sent to Slack")
        response.raise_for_status()
