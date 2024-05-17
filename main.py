from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

app = FastAPI()


# cONFIGURACIÓN DE LA BASE DE DATOS SQL

DATABASE_URL = "task.db"


def get_db():
    db = sqlite3.connect(DATABASE_URL, check_same_thread=False)
    try:
        yield db
        db.commit()
    finally:
        db.close()


get_db()


# MODELOS
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False


# Ruta para crear una nueva tarea
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
        (task.title, task.description, task.completed),
    )
    task.id = cursor.lastrowid
    return task


