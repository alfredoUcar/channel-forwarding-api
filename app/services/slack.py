import requests
from app.config import settings
from app.services.channel import Channel


class SlackChannel(Channel):
    def send(self, message: str):
        payload = {"text": message}
        response = requests.post(settings.slack_webhook_url, json=payload)
        response.raise_for_status()
