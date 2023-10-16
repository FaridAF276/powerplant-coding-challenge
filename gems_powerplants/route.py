from fastapi import FastAPI, HTTPException
from utils import parse_body, get_powerplants
from typing import List
from output_models import PowerPlant
from input_models import PowerPlantPayload
app = FastAPI()
@app.get("/")
def root():
    return {"body": "Welcome to GEMS App."}
@app.post("/productionplan")
async def production(payload: PowerPlantPayload) -> List[PowerPlant]:
    power_plants_datas = parse_body(input=payload)
    try: 
        await get_powerplants(powerplants=sorted(power_plants_datas, key=lambda x:x.cost_per_mwh), load=payload.load)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=e.args)