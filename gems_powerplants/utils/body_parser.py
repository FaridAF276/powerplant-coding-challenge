import json
from typing import List
from input_models import PowerPlantPayload, PowerPlantDataPoint
def extract_data():
    with open("data\payload1.json", "r") as f:
        payload = json.load(f)
        # pprint(payload)
        load = payload["load"]
        fuels = payload["fuels"]
        powerplants = payload["powerplants"]
        pp_name_cost = []
        for pp in powerplants:
            if pp["type"] == "gasfired":
                pp_name_cost.append({"name": pp["name"], "cost_per_mwh" : fuels["gas(euro/MWh)"]/pp["efficiency"], "pmin": pp["pmin"], "pmax": pp["pmax"]})
            if pp["type"] == "turbojet":
                pp_name_cost.append({"name": pp["name"], "cost_per_mwh" : fuels["kerosine(euro/MWh)"]/pp["efficiency"], "pmin": pp["pmin"], "pmax": pp["pmax"]})
            if pp["type"] == "windturbine":
                pp_name_cost.append({"name": pp["name"], "cost_per_mwh" : 0, "pmin": pp["pmin"]*0.01*fuels["wind(%)"], "pmax":pp["pmax"]*0.01*fuels["wind(%)"]})
        return pp_name_cost, load
def parse_body(input: PowerPlantPayload) -> List[PowerPlantDataPoint]:
    fuels = input.fuels
    powerplants = input.powerplants
    pp_dp = []
    for pp in powerplants:
        if pp.type == "gasfired":
            pp_dp.append(PowerPlantDataPoint(name=pp.name, cost_per_mwh=fuels.gas/pp.efficiency, pmin=pp.pmin, pmax=pp.pmax))
        if pp.type == "turbojet":
            pp_dp.append(PowerPlantDataPoint(name=pp.name, cost_per_mwh=fuels.kerosine/pp.efficiency, pmin=pp.pmin, pmax=pp.pmax))
        if pp.type == "windturbine":
            pp_dp.append(PowerPlantDataPoint(name=pp.name, cost_per_mwh=0.0, pmin=pp.pmin*0.01*fuels.wind, pmax=pp.pmax*0.01*fuels.wind))
    return pp_dp
def main():
    extract_data()           
if __name__ == "__main__":
    main()