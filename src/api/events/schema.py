from pydantic import BaseModel
from typing import List

class EventSchema(BaseModel):
    id: int
    name: str
    description: str
    date: str

class EventListSchema(BaseModel):
    data: List[EventSchema]

class EventCreateSchema(BaseModel):
    name: str
    description: str
    date: str

class EventUpdateSchema(BaseModel):
    name: str
    description: str
    date: str

class EventDeleteSchema(BaseModel):
    id: int