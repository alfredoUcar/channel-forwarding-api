from app.services.channel import Channel
from app.logger import logger


class EmailChannel(Channel):
    def send(self, message: str):
        # mock implementation
        logger.debug(f"[MOCK] Sending email: {message}")
