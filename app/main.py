from fastapi import FastAPI
from app.assistance_request.api_routes import router

app = FastAPI()

app.include_router(router)
