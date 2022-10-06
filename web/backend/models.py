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
    
    @staticmethod
    def create(owner: User):
        return Room(id=owner.room_id, players=[owner], owner=owner)

    def add_player(self, player: User):
        self.players.append(player)

    def remove_player(self, player: User):
        self.players.remove(player)

    @property
    def player_names(self):
        return [x.username for x in self.players]