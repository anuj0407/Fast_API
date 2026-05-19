from fastapi import FastAPI, Path , HTTPException
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description='Id of the patient in the DB', example='P001')):
    data = load()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")