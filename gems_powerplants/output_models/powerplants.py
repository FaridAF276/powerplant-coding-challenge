from typing import List
from pydantic import BaseModel

class PowerPlant(BaseModel):
    name:str
    p: float