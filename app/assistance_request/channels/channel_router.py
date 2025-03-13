from typing import Dict
from .base_channel import BaseChannel


class ChannelRouter:
    def __init__(self, channels: Dict[str, BaseChannel]):
        self.channels = channels

    def get(self, topic: str) -> BaseChannel:
        if topic not in self.channels:
            raise ValueError(f"Unsupported topic: {topic}")
        return self.channels.get(topic)
