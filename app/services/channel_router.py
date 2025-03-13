from app.services.channel import Channel
from app.services.slack import SlackChannel
from app.services.email import EmailChannel

class ChannelRouter:
    def __init__(self):
        # Default mapping of topics to channels
        self.channels = {
            "sales": SlackChannel(),
            "pricing": EmailChannel(),
        }

    def get(self, topic: str) -> Channel:
        if topic not in self.channels:
            raise ValueError(f"Unsupported topic: {topic}")
        return self.channels.get(topic)
