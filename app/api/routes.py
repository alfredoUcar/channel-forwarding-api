from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from app.models import AssistanceRequest
from app.services.channel_router import ChannelRouter
from app.logger import logger

router = APIRouter()

# Initialize the router
channel_router = ChannelRouter()

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
def assistance_request(request: AssistanceRequest):
    try:
        channel = channel_router.get(request.topic)
    except ValueError as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Unsupported topic")

    channel.send(request.description)
    return {"status": "sent"}
