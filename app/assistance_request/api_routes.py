from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from app.assistance_request.models import AssistanceRequest
from app.assistance_request.channels.channel_router import ChannelRouter
from app.assistance_request.channels.slack import SlackChannel
from app.assistance_request.channels.email import EmailChannel
from app.core.logger import logger

router = APIRouter()


def get_channel_router():
    return ChannelRouter({"sales": SlackChannel(), "pricing": EmailChannel()})


@router.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Backend challenge</title>
        </head>
        <body>
            <p>Check API documentation at <a href="http://localhost:8000/docs">/docs</a></p>
        </body>
    </html>
    """


@router.post("/assistance-request/")
def assistance_request(
    request: AssistanceRequest,
    channel_router: ChannelRouter = Depends(get_channel_router),
):
    try:
        channel = channel_router.get(request.topic)
    except ValueError as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Unsupported topic")

    channel.send(request.description)
    return {"status": "sent"}
