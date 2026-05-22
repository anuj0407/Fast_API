from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict
class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains= ['hdfc.com','icici.com']
        domain_name= value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a Valid domain")
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if 0< value <100:
            return value
        else:
            raise ValueError("Age should be in between 0 to 100")
    
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
    
patient_info = {"name":"John","email":"johnDoe@icici.com","age":40,"weight":80.8,"married":True,"allergies":["Pollen","Dust"],"contact_details":{"phone_no":"9282984213"}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)