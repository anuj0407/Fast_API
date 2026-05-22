from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pincode: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city':'Mathura','state':'Uttar Pradesh','pincode':'281021'}
address1 = Address(**address_dict)

patient_dict = {'name':'John','gender':'male','age':35,'address':address1}
patient1 = Patient(**patient_dict)

print(patient1)
print("\nPatient Name:",patient1.name)
print("Patient City:",patient1.address.city)
print("Patient Pincode:",patient1.address.pincode)