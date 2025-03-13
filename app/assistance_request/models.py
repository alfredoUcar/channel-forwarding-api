from pydantic import BaseModel


class AssistanceRequest(BaseModel):
    topic: str
    description: str
