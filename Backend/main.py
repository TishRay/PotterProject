from fastapi import FastAPI 
from base import Base
from database import engine, SessionLocal
from models import Reading_log, ReadingRecord

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return "Test"

@app.get("/readall")
def all_logs():
    db = SessionLocal()
    logs = db.query(Reading_log).all()
    return logs

@app.post("/addlog")
def new_entry(chapter:int,chapter_notes:str):
    db = SessionLocal()
    record = Reading_log(
        user_id = 1,
        book_id = 1,
        chapter = chapter,
        chapter_notes = chapter_notes
    )
    db.add(record)
    db.commit()
    return record
