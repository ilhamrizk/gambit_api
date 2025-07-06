# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# ✅ Aktifkan CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # atau ["http://localhost:5173"] untuk lebih ketat
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

class Todo(BaseModel):
    task: str

@app.get("/todos")
def get_todos():
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/todos?select=*",
        headers=headers
    )
    return response.json()

@app.post("/todos")
def create_todo(todo: Todo):
    payload = {"task": todo.task}
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/todos",
        headers={**headers, "Prefer": "return=minimal"},
        json=payload
    )
    return response.json()

@app.get("/online_gambler")
def get_todos():
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/online_gambler?select=*",
        headers=headers
    )
    return response.json()

@app.get("/online_gambler_eq")
def check_id_exists(id_value: str):
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/online_gambler",
        headers=headers,
        params={
            "id_value": f"eq.{id_value}",
            "select": "id_value"
        }
    )
    return {"exists": len(r.json()) > 0}