import json
def open_json(json_rut):
    with open(json_rut, "r", encoding = "utf-8") as sd:
        openn = json.load(sd)
    
    return openn