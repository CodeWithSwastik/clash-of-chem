from dataclasses import dataclass, field
import random
from typing import Dict, List
from datetime import datetime
from game import Game

PFP_COLORS = [
    "rosewater",
    "pink",
    "maroon",
    "peach",
    "yellow",
    "teal",
    "sky",
    "lavender",
]


@dataclass
class User:
    sid: str
    username: str
    room_id: str
    pfp_color: str = "red"

    def __post_init__(self):
        self.pfp_color = random.choice(PFP_COLORS)

    @property
    def user_info(self):
        return {"username": self.username, "color": self.pfp_color}


@dataclass
class Room:
    id: str
    players: List[User]
    owner: User
    settings: "ClashSettings"
    created_at: datetime

    def __del__(self):
        print(f"Room {self.id} deleted.")

    @staticmethod
    def create(owner: User):
        return Room(
            id=owner.room_id,
            players=[owner],
            owner=owner,
            settings=ClashSettings(),
            created_at=datetime.now(),
        )

    def add_player(self, player: User):
        self.players.append(player)

    def remove_player(self, player: User):
        self.players.remove(player)
        if player == self.owner and self.players:
            self.owner = self.players[0]

    @property
    def players_info(self):
        return [x.user_info for x in self.players]

    @property
    def countdown(self):
        minutes = 5
        return (self.created_at - datetime.now()).total_seconds() + 60 * minutes

    @property
    def room_info(self):
        return {
            "id": self.id,
            "players": self.players_info,
            "countdown": self.countdown,
            "owner": self.owner.username,
        }

    def create_clash(self):
        return Clash(id=self.id, settings=self.settings, players=self.players)


@dataclass
class Clash:
    id: str
    settings: "ClashSettings"
    players: List[User] = field(default_factory=list)
    started_at: datetime = field(default_factory=datetime.now)
    game: Game = field(default_factory=Game)

    def __post_init__(self):
        self.game.points_table = {player.username: 0 for player in self.players}

    @property
    def leaderboard(self):
        return dict(sorted(self.game.points_table.items(), key=lambda item: item[1]))

    @property
    def clash_info(self):
        return {
            "id": self.id,
            "leaderboard": self.leaderboard,
            "players": self.players_info,
        }

    @property
    def players_info(self):
        return {x.username: x.user_info for x in self.players}


@dataclass
class ClashSettings:
    public: bool = False
