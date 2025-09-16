from sqlmodel import create_engine
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL

if DATABASE_URL == '':
    raise NotImplementedError('DATABASE_URL not set')

engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session