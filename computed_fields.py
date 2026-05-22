from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2))
        return bmi

def display(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

def insert_patient_data(patient: Patient):
    display(patient)
    print("Inserted")

def update_patient_data(patient: Patient):
    display(patient)
    print("BMI :",patient.bmi)
    print("Updated")
    
patient_info = {"name":"John","email":"johnDoe@icici.com","age":65,"weight":80.8,'height':'1.75',"married":True,"allergies":["Pollen","Dust"],"contact_details":{"phone_no":"9282984213",'emergency':'2049934992'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)