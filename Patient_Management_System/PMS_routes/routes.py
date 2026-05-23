from fastapi import APIRouter, Path, Query
from fastapi.responses import JSONResponse
from schemas import Patient, UpdatedPatient
import crud 
import os
from database import file_path
router = APIRouter()

@router.get("/")
def home():
    return {'message': 'Patient Management System API'}

@router.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@router.get('/view')
def view():
    return crud.get_all_patients()

@router.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient', example='P001')):
    return crud.get_patient_by_id(patient_id)

@router.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), 
    order: str = Query('asc', description='sort in asc or desc order')
):
    return crud.get_sorted_patients(sort_by, order)

@router.post('/create')
def create_patient(patient: Patient):
    crud.add_patient(patient)
    return JSONResponse(status_code=201, content={'message': 'patient created successfully'})

@router.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: UpdatedPatient):
    crud.edit_patient(patient_id, patient_update)
    return JSONResponse(status_code=200, content={'message': 'Patient Updated'})
    
@router.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    crud.remove_patient(patient_id)
    return JSONResponse(status_code=200, content={'message': 'Patient deleted'})
