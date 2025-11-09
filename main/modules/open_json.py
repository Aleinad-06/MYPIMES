import json
def open_json(json_rut):
    with open(json_rut, "r") as sd:
        openn = json.load(sd)
    
    return openn