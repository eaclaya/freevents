from fastapi import APIRouter, Depends
from sqlmodel import Session
from .models import EventModel, EventListSchema, EventCreateSchema, EventUpdateSchema
from api.db.session import get_session

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return EventListSchema(data=[EventModel(id=1, name="Event 1", description="Event 1 description", date="2025-01-01"), EventModel(id=2, name="Event 2", description="Event 2 description", date="2025-01-02"), EventModel(id=3, name="Event 3", description="Event 3 description", date="2025-01-03")])


@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    return EventModel(id=event_id, name="Event 1", description="Event 1 description", date="2025-01-01")

@router.post("/", response_model=EventModel)
def create_event(payload: EventCreateSchema, session: Session = Depends(get_session)):
    data = payload.model_dump()
    print(data)
    return EventModel(id=1, name="Event 1", description="Event 1 description", date="2025-01-01")

@router.put("/{event_id}")
def update_event(event_id: int, event: EventUpdateSchema) -> EventModel:
    return EventModel(id=event_id, name="Event 1", description="Event 1 description", date="2025-01-01")

@router.delete("/{event_id}")
def delete_event(event_id: int) -> EventModel:
    return EventModel(id=event_id, name="Event 1", description="Event 1 description", date="2025-01-01")