from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API Simples")

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

todos=[]

@app.post("/v1/todos", response_model=TodoResponse, status_code=201)
async def create_todo(todo: TodoCreate):
    todo_id= len(todos)+1
    new_todo = {
        "id": todo_id,
        "title": todo.title,
        "completed": todo.completed
    }
    todos.append(new_todo)
    return new_todo

@app.get("/v1/todos", response_model=List[TodoResponse])
async def get_todos():
    return todos

        
