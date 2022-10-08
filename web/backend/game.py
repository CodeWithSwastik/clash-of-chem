import os
import json
import random
from datetime import datetime

reactions_filepath = os.path.join(
    os.path.dirname(__file__), "..", "..", "reactions.json"
)
smiles_filepath = os.path.join(os.path.dirname(__file__), "smiles.json")

with open(reactions_filepath, "r") as f:
    REACTIONS = json.load(f)

with open(smiles_filepath, "r") as f:
    SMILES = json.load(f)

REAGENTS = set()
for substrate in REACTIONS:
    for reagent, product in REACTIONS[substrate].items():
        REAGENTS.add(reagent)

class Challenge:
    def __init__(self) -> None:
        self.time = 25
        self.difficulty = 1
        self.type = "conversion"  # "naming", "predict product" etc
        self.started_at = None
        self.running = False
        self.players_cleared = {}  # {name: time_taken_to_clear}

        # conversion
        self.from_compound = random.choice(list(REACTIONS))
        self.correct_reagent = random.choice(list(REACTIONS[self.from_compound]))
        self.to_compound = REACTIONS[self.from_compound][self.correct_reagent]

        self.reagents = [self.correct_reagent]

        for _ in range(3):
            r = random.choice(list(REAGENTS))

            if r in self.reagents or (r in REACTIONS[self.from_compound] and REACTIONS[self.from_compound][r] == self.to_compound): 
                continue
            self.reagents.append(r)

        random.shuffle(self.reagents)

    @property
    def challenge_data(self):
        return {
            "from": SMILES[self.from_compound],
            "to": SMILES[self.to_compound],
            "reagents": self.reagents,
            "time": self.time,
        }

    def start(self):
        self.started_at = datetime.now()
        self.running = True

    def player_cleared(self, player_name):

        if not self.running or player_name in self.players_cleared:
            return 0

        time_taken = (datetime.now() - self.started_at).total_seconds()
        points = int(((self.time - time_taken) / self.time) * 30)
        self.players_cleared[player_name] = time_taken
        return points


class Game:
    def __init__(self) -> None:
        self.challenges = [Challenge(), Challenge(), Challenge(), Challenge(), Challenge()]
        self.current_challenge = None
        self.counter = 0
        self.points_table = {}

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.challenges):
            raise StopIteration
        else:
            self.current_challenge = self.challenges[self.counter]
            self.current_challenge.start()
            self.counter += 1
            data = self.current_challenge.challenge_data
            data["number"] = self.counter
            return data

    def clear_challenge(self, player_name):
        points = self.current_challenge.player_cleared(player_name)
        self.points_table[player_name] += points
