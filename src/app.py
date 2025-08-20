from fastapi import FastAPI
from manager import Manager
from src.soldier import Soldier

app = FastAPI()

manager = Manager()

@app.get("/soldiersdb/current_soldier/{id}")
def update_soldier(id: int):
    manager.update_current_soldier_by_id(id)

@app.get("/soldiersdb/get_all")
def get_data():
    return manager.get_all_data()

@app.put("/soldiersdb/update/{field}/{value}")
def update_soldier(field: str, value):
    manager.update_soldier(field, value)

@app.post("/soldiersdb/insert")
def insert_soldier(soldier):
    manager.insert_soldier(soldier)

@app.get("/soldiersdb/delete")
def delete_soldier():
    manager.delete_soldier()