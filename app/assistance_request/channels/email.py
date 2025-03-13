from .base_channel import BaseChannel
from app.core.logger import logger


class EmailChannel(BaseChannel):
    def send(self, message: str):
        # mock implementation
        logger.debug(f"[MOCK] Sending email: {message}")
