from fastapi import APIRouter
from .schema import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return EventListSchema(data=[EventSchema(id=1, name="Event 1", description="Event 1 description", date="2025-01-01"), EventSchema(id=2, name="Event 2", description="Event 2 description", date="2025-01-02"), EventSchema(id=3, name="Event 3", description="Event 3 description", date="2025-01-03")])


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return EventSchema(id=event_id, name="Event 1", description="Event 1 description", date="2025-01-01")

@router.post("/")
def create_event(event: EventCreateSchema) -> EventSchema:
    return EventSchema(id=1, name="Event 1", description="Event 1 description", date="2025-01-01")

@router.put("/{event_id}")
def update_event(event_id: int, event: EventUpdateSchema) -> EventSchema:
    return EventSchema(id=event_id, name="Event 1", description="Event 1 description", date="2025-01-01")

@router.delete("/{event_id}")
def delete_event(event_id: int) -> EventSchema:
    return EventSchema(id=event_id, name="Event 1", description="Event 1 description", date="2025-01-01")