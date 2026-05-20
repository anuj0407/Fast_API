from pydantic import BaseModel
from typing import List, Dict, Optional
class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]

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
    
patient_info = {"name":"John","age":40,"weight":80.8,"contact_details":{"email":"john_example@gmail.com","phone_no":"9282984213"}}
patient1 = Patient(**patient_info)

print("Before Updation:\n")
insert_patient_data(patient1)

patient_info["married"] = True
patient_info["allergies"] = ["Pollen","Dust"]

patient1 = Patient(**patient_info)
print("\nAfter Updation:\n")
update_patient_data(patient1)


