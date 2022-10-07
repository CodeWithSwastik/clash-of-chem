from dataclasses import dataclass, field
import random
from typing import Dict, List
from datetime import datetime


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
            created_at=datetime.now()
        )

    def add_player(self, player: User):
        self.players.append(player)

    def remove_player(self, player: User):
        self.players.remove(player)
        if player == self.owner and self.players:
            self.owner = self.players[1]



    @property
    def players_info(self):
        return [
            {
                "username":x.username, 
                "color":x.pfp_color
            } for x in self.players
        ]
    @property
    def countdown(self):
        minutes = 5
        return (self.created_at - datetime.now()).total_seconds() + 60*minutes

    @property
    def room_info(self):
        return {
            "id": self.id,
            "players": self.players_info,
            "countdown": self.countdown,
            "owner": self.owner.username
        }

    def create_clash(self):
        return Clash(
            id=self.id, 
            settings=self.settings, 
            players=self.players
        )


@dataclass
class Clash:
    id: str
    settings: "ClashSettings"
    players: List[User] = field(default_factory=list)
    started_at: datetime = field(default_factory=datetime.now)
    points: Dict[str, int] = field(default_factory=dict)
    
    def __post_init__(self):
        self.points = {
            player.username: 0 for player in self.players
        }

    @property
    def leaderboard(self):
        return dict(sorted(self.points.items(), key=lambda item: item[1]))

    @property
    def clash_info(self):
        return {
            "id": self.id,
            "leaderboard": self.leaderboard
        }

@dataclass
class ClashSettings:
    public: bool = False
