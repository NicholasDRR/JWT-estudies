import re
from pydantic import BaseModel, validator

class User(BaseModel):
    username: str
    password: str
    
    @validator('username')
    def validator_username(cls, username):
        
        if not re.match("^([a-z]|[0-9]|@)+$", username):
            raise ValueError("Username format invalid!")
        
        return username