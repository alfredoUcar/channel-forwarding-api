import pytest
from unittest.mock import MagicMock
from app.services.channel_router import ChannelRouter
from app.services.channel import Channel

def test_returns_correct_channel():
    # Create mock channels
    channel_a = MagicMock(spec=Channel)
    channel_b = MagicMock(spec=Channel)
    
    router = ChannelRouter({
        "topic_a": channel_a,
        "topic_b": channel_b
    })

    # Should return the correct channel based on the topic
    assert router.get("topic_a") == channel_a
    assert router.get("topic_b") == channel_b

def test_raises_error_for_unknown_topic():
    channel_a = MagicMock(spec=Channel)
    router = ChannelRouter({"topic_a": channel_a})
    
    # Should raise ValueError for unsupported topic
    with pytest.raises(ValueError, match="Unsupported topic: unknown_topic"):
        router.get("unknown_topic")

