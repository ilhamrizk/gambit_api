# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import os

app = FastAPI()

SUPABASE_URL = "https://oktqikjeapcxoffhdeyk.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9rdHFpa2plYXBjeG9mZmhkZXlrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA1NjA2MDAsImV4cCI6MjA2NjEzNjYwMH0.RfY62PjWoc2vnEH0FffSsX92YzZrfvISPriG027-LWs"

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