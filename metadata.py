from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title = "Name of the patient", description="Give the name of the patient in less than 50 characters", examples = ['Anuj','Rahul'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt = 0,lt =120)
    weight: Annotated[float, Field(gt=0, strict= True)]
    married: Annotated[bool, Field(default= None,description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]], Field(default= None,max_length=5)]
    contact_details: Dict[str,str]

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
    print("Updated")
    
patient_info = {"name":"John","email":"johnDoe@gmail.com","linkedin_url":"http://linkedin.com/1320","age":40,"weight":80.8,"contact_details":{"phone_no":"9282984213"}}
patient1 = Patient(**patient_info)

print("Before Updation:\n")
insert_patient_data(patient1)

patient_info["married"] = True
patient_info["allergies"] = ["Pollen","Dust"]

patient1 = Patient(**patient_info)
print("\nAfter Updation:\n")
update_patient_data(patient1)


