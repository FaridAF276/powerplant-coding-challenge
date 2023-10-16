from typing import List
from input_models import PowerPlantDataPoint
from output_models import PowerPlant
import logging
# def main():
#     pp, load = extract_data()
#     sorted_pp = sorted(pp, key=lambda x:x["cost_per_mwh"])
#     return make_power_mix(sorted_pp, load)

logger = logging.getLogger(__name__)
def make_power_mix(pps, load):
    if load == 0:
        return {}
    elif load > sum(pp["pmax"] for pp in pps):
        raise ValueError("The load exceeds the max power of all the powerplants provided.")
    accepted_pp = []
    current_load = 0
    
    for pp in pps:
        if current_load == load:
            return accepted_pp
        if current_load + pp["pmin"] <= load:
            needed_power = min(pp['pmax'], load - current_load)
            current_load += needed_power
            accepted_pp.append({"name" :pp["name"], "p":  needed_power})
    if sum(pp["p"] for pp in accepted_pp) != load:
        raise ValueError(f"Couldn't find a combination of powerplants that exactly match the load.")
    
    return accepted_pp

async def get_powerplants(powerplants:List[PowerPlantDataPoint], load:int)-> PowerPlant:
    if load ==0:
        return {}
    elif load > sum(pp.pmax for pp in powerplants):
        raise ValueError("The load exceeds the max power of all the powerplants provided.")
    accepted_pp:List[PowerPlant] = []
    covered_load = 0
    print([pp for pp in powerplants])
    for pp in powerplants:
        if covered_load == load:
            return accepted_pp
        if covered_load + pp.pmin <= load:
            needed_power = min(pp.pmax, load-covered_load)
            covered_load += needed_power
            accepted_pp.append(PowerPlant(name=pp.name, p=needed_power))
    if sum(pp.p for pp in accepted_pp) != load:
        raise ValueError(f"Couldn't find a combination of powerplants that exactly match the load. {sum(pp.p for pp in accepted_pp)} out of {load} MW were covered.")
    return accepted_pp
if __name__ == "__main__":
    pass
