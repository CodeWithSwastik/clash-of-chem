import os 
import json
import random

reactions_filepath = os.path.join(os.path.dirname(__file__), "..",  "..", "reactions.json")
smiles_filepath = os.path.join(os.path.dirname(__file__), "smiles.json")

with open(reactions_filepath, "r") as f:
    REACTIONS = json.load(f)

with open(smiles_filepath, "r") as f:
    SMILES = json.load(f)

class Challenge:
    def __init__(self) -> None:
        self.from_compound = random.choice(list(REACTIONS))
        self.correct_reagent = random.choice(list(REACTIONS[self.from_compound]))
        self.to_compound = REACTIONS[self.from_compound][self.correct_reagent]
        self.reagents = random.choices(list(REACTIONS[self.from_compound]), k=3) + [self.correct_reagent]
        random.shuffle(self.reagents)
        self.time = 5
        self.difficulty = 1
        self.type = "conversion" # "naming", "predict product" etc
    
    @property
    def challenge_data(self):
        return {
            "from": SMILES[self.from_compound],
            "to": SMILES[self.to_compound],
            "reagents": self.reagents,
            "time": self.time
        }

class Game:
    def __init__(self) -> None:
        self.challenges = [Challenge(), Challenge(), Challenge()]
        self.counter = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.challenges):
            raise StopIteration
        else:
            challenge = self.challenges[self.counter]
            self.counter += 1
            data = challenge.challenge_data
            data["number"] = self.counter
            return data
