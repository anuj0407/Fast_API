from fastapi import FastAPI
import json

app = FastAPI()

def load():
    with open("patients.json","r") as f:
        data = json.load(f)

    return data

@app.get("/")
def first():
    return {"Message":"Patient Management System API"}

@app.get("/about")
def about():
    return {"Message":"A fully functional API to manage Patients"}

@app.get("/view")
def view():
    return load()