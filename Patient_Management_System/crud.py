from fastapi import HTTPException
from database import load_data, save_data
from schemas import Patient, UpdatedPatient

def get_all_patients() -> dict:
    return load_data()

def get_patient_by_id(patient_id: str) -> dict:
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    return data[patient_id]

def get_sorted_patients(sort_by: str, order: str) -> list:
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()
    sort_order = True if order == 'desc' else False
    return sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

def add_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient Already exists')
    
    data[patient.id] = patient.model_dump(exclude={'id'})
    save_data(data)

def edit_patient(patient_id: str, patient_update: UpdatedPatient):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
    
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)
    
    data[patient_id] = patient_pydantic_obj.model_dump(exclude={'id'})
    save_data(data)

def remove_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]
    save_data(data)
