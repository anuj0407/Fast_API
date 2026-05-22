from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict
class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contacts(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Updated")
    
patient_info = {"name":"John","email":"johnDoe@icici.com","age":65,"weight":80.8,"married":True,"allergies":["Pollen","Dust"],"contact_details":{"phone_no":"9282984213",'emergency':'2049934992'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)