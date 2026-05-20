from pydantic import BaseModel
# schema
class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")
    
patient_info = {"name":"John","age":40}

patient1 = Patient(**patient_info)

update_patient_data(patient1)


# Pydantic used for many features it provides like type validation in above code , 
# it also gives data validation, and auto type conversion, clear error message.
