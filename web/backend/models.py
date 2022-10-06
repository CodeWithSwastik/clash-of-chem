from dataclasses import dataclass
import random
from typing import List

PFP_COLORS = [
    'rosewater', 'pink', 'maroon', 'peach', 'yellow', 'teal', 'sky', 'lavender'
]


@dataclass
class User:
    sid: str
    username: str
    room_id: str
    pfp_color: str = "red"

    def __post_init__(self):
        self.pfp_color = random.choice(PFP_COLORS)
    


@dataclass
class Room:
    id: str
    players: List[User]
    owner: User
    settings: "ClashSettings"

    @staticmethod
    def create(owner: User):
        return Room(
            id=owner.room_id, players=[owner], owner=owner, settings=ClashSettings()
        )

    def add_player(self, player: User):
        self.players.append(player)

    def remove_player(self, player: User):
        self.players.remove(player)

    @property
    def players_info(self):
        return [
            {
                "username":x.username, 
                "color":x.pfp_color
            } for x in self.players
        ]

    def create_clash(self):
        return Clash(id=self.id, settings=self.settings)


@dataclass
class Clash:
    id: str
    players: List[User]
    settings: "ClashSettings"


@dataclass
class ClashSettings:
    public: bool = False
