from app.api.routes import get_channel_router
from app.services.channel import Channel
from app.services.channel_router import ChannelRouter
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app

client = TestClient(app)


def test_forwards_request_to_correct_channel():
    channel_a = MagicMock(spec=Channel)
    channel_b = MagicMock(spec=Channel)

    app.dependency_overrides[get_channel_router] = lambda: ChannelRouter(
        {"topic_a": channel_a, "topic_b": channel_b}
    )

    response = client.post(
        "/assistance-request/",
        json={"topic": "topic_a", "description": "Request for topic A"},
    )

    channel_a.send.assert_called_once_with("Request for topic A")
    channel_b.send.assert_not_called()
    assert response.status_code == 200
    assert response.json() == {"status": "sent"}


def test_channel_not_invoked_when_invalid_topic():
    channel = MagicMock(spec=Channel)

    app.dependency_overrides[ChannelRouter] = lambda: ChannelRouter(
        {
            "some_topic": channel,
        }
    )

    response = client.post(
        "/assistance-request/",
        json={"topic": "invalid", "description": "Invalid topic"},
    )

    channel.send.assert_not_called()
    assert response.status_code == 400
