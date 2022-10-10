import os
import json
import requests

reactions_filepath = os.path.join(
    os.path.dirname(__file__), "..", "..", "reactions.json"
)
smiles_filepath = os.path.join(os.path.dirname(__file__), "smiles.json")

with open(reactions_filepath, "r") as f:
    REACTIONS = json.load(f)

with open(smiles_filepath, "r") as f:
    SMILES = json.load(f)


def add_smile(compound):
    try:
        res = requests.get("https://opsin.ch.cam.ac.uk/opsin/" + compound)
        SMILES[compound] = res.json()["smiles"]
        print(compound, "added!")
    except Exception as e:
        with open(smiles_filepath, "w") as f:
            json.dump(SMILES, f)
        print("Failed:", compound)
        print("Reason:", res.json()["message"])
        print(e)


for substrate in REACTIONS:
    if substrate not in SMILES:
        add_smile(substrate)

    for reagent, product in REACTIONS[substrate].items():
        if product not in SMILES:
            add_smile(product)


with open(smiles_filepath, "w") as f:
    json.dump(SMILES, f, indent=4)
