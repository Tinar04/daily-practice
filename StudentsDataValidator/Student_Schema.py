import csv
from pydantic import ValidationError
from pydantic import BaseModel,Field,field_validator,computed_field,model_validator
import csv
from pydantic import ValidationError
import json
from pydantic_settings import BaseSettings
import os
print("subscript started")

class Settings(BaseSettings):
    model_config = {"env_file": ".env"}
    OUTPUT_DIR: str
    STRICT_MODE: bool


class Adresss(BaseModel):
    model_config = {"extra":"forbid"}
    city:str
    pincode:str = Field(max_length=6)
    @field_validator('pincode')
    @classmethod
    def validate_pincode(cls,value):
        if len(value)!=6:
            raise ValueError("pincode should be of 6 digits only")
        return value


class Students(BaseModel):
    model_config = {"extra":"forbid"}
    name:str
    age :int = Field(gt=0,le=100)
    grade : int = Field(gt=0,le=12)
    is_pass : bool
    marks:float = Field(ge=0,le=100)
    scholarship:float = Field(description="yearly",gt=0)
    fees:float = Field(description="yearly",gt=0)
    address:Adresss

    @field_validator('name')
    @classmethod
    def StudentName_validation(cls,value):
        name = [char for char in value if char.isalpha()]

        if len(name)==0:
            raise ValueError("Name should contain at least one string")

        return value
    
    @model_validator(mode="after")
    def final_fees(self):
        if self.fees<self.scholarship:
            raise ValueError("discount cant be greater than the fees")              

        return self

    
    @computed_field
    @property
    def check_fees(self)->float:
        finalfee = self.fees-self.scholarship
        return finalfee 



valid_students = []
failed_rows = []

with open('students_final.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['address'] = {
            "city": row.pop('city'),
            "pincode": row.pop('pincode')
        }
        try:
            s = Students(**row)
            valid_students.append(s)
        except ValidationError as e:
            failed_rows.append({"row": row, "errors": e.errors()})

print(f"Valid: {len(valid_students)}, Failed: {len(failed_rows)}")

for f in failed_rows:
    print(f["row"]["name"], "->")
    for err in f["errors"]:
        print("   ", err['loc'], err['msg'])
    

  

settings = Settings()
print(settings)
 
os.makedirs(settings.OUTPUT_DIR, exist_ok=True)
output_data = [s.model_dump() for s in valid_students]
 
with open(f'{settings.OUTPUT_DIR}/clean_students.json', 'w') as f:
    json.dump(output_data, f, indent=2, default=str)
    print("data inserted successfully")

    


