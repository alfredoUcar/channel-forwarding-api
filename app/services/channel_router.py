from typing import Dict
from app.services.channel import Channel
class ChannelRouter:
    def __init__(self, channels: Dict[str, Channel]):
        self.channels = channels

    def get(self, topic: str) -> Channel:
        if topic not in self.channels:
            raise ValueError(f"Unsupported topic: {topic}")
        return self.channels.get(topic)
