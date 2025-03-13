from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

router = APIRouter()

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
