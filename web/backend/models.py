from dataclasses import dataclass
from typing import List


@dataclass
class User:
    sid: str
    username: str
    room_id: str


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
    def player_names(self):
        return [x.username for x in self.players]

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
