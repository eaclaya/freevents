from sqlmodel import Field, SQLModel
from typing import List

class EventModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    date: str

class EventListSchema(SQLModel):
    data: List[EventModel]

class EventCreateSchema(SQLModel):
    name: str
    description: str
    date: str

class EventUpdateSchema(SQLModel):
    name: str
    description: str
    date: str

class EventDeleteSchema(SQLModel):
    id: int