from math import prod
import os
import json
import random
from datetime import datetime
from itertools import cycle

reactions_filepath = os.path.join(
    os.path.dirname(__file__), "..", "..", "reactions.json"
)
smiles_filepath = os.path.join(os.path.dirname(__file__), "smiles.json")

with open(reactions_filepath, "r") as f:
    REACTIONS = json.load(f)

with open(smiles_filepath, "r") as f:
    SMILES = json.load(f)

REAGENTS = set()
PRODUCTS = set()

for substrate in REACTIONS:
    for reagent, product in REACTIONS[substrate].items():
        REAGENTS.add(reagent)
        PRODUCTS.add(product)

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
            "type": self.type,
            "time": self.time,
            "from": SMILES[self.from_compound],
            "to": SMILES[self.to_compound],
            "reagents": self.reagents,
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

class StrategyChallenge:
    def __init__(self, players: list) -> None:
        self.time = 300
        self.type = "strategy"

        self.starting = random.choice(list(REACTIONS))
        self.finals = []

        while len(REACTIONS[self.starting]) < 5 and self.get_reagents(self.starting):
            self.starting = random.choice(list(REACTIONS))

        self.current = self.starting


        while len(self.finals) < len(players):
            p = random.choice(list(PRODUCTS))
            if p in REACTIONS[self.current].values():
                continue
            self.finals.append(p)
        self.players = players

        self.targets = dict(zip(self.players, self.finals))

        self.playerCycle = cycle(self.players)
        self.turn = next(self.playerCycle)
        self.winner = None

    def get_reagents(self, comp = None):
        comp = comp or self.current
        l = []
        for r in list(REACTIONS[comp]):
            prod = REACTIONS[comp][r]
            if prod in self.finals:
                l.append(r)

        random.shuffle(l)
        return l[:6]

    def update(self, reagent):
        self.current = REACTIONS[self.current][reagent]
        if self.targets[self.turn] == self.current:
            print(self.turn, "wins")
            self.winner = self.turn
            return
        
        self.turn = next(self.playerCycle)

    @property
    def challenge_data(self):
        d = {
            "type": self.type,
            "time": self.time,
            "current": SMILES[self.current],
            "reagents": self.get_reagents(),
            "turn": self.turn,
            "targets": self.targets,
            "winner": self.winner
        }
        return d

    

class Game:
    def __init__(self) -> None:
        self.challenges = [Challenge(), Challenge()]
        self.current_challenge = None
        self.counter = 1
        self.points_table = {}

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.challenges):
            raise StopIteration
        elif self.counter == 1:
            self.current_challenge = StrategyChallenge(list(self.points_table))
        else:
            self.current_challenge = self.challenges[self.counter]
            self.current_challenge.start()

        data = self.current_challenge.challenge_data
        data["number"] = self.counter
        self.counter += 1
        return data

    def clear_challenge(self, player_name):
        points = self.current_challenge.player_cleared(player_name)
        self.points_table[player_name] += points

    def strategy_update(self, reagent):
        self.current_challenge.update(reagent)

        if self.current_challenge.winner:
            self.points_table[self.current_challenge.winner] += 100