from typing import List
from pydantic import BaseModel, Field

class Fuels(BaseModel):
    gas:float = Field(alias="gas(euro/MWh)")
    kerosine:float =Field(alias="kerosine(euro/MWh)")
    co2:float = Field(alias="co2(euro/ton)")
    wind:float =Field(alias="wind(%)")

class PowerPlant(BaseModel):
    name:str
    type: str
    efficiency: float
    pmin: float
    pmax: float
class PowerPlantPayload(BaseModel):
    load: int
    fuels : Fuels
    powerplants : List[PowerPlant]

class PowerPlantDataPoint(BaseModel):
    name:str
    cost_per_mwh: float
    pmin:float
    pmax:float