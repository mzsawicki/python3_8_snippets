from typing import TypedDict


class Player(TypedDict):
    name: str
    points: int
    eliminated: bool


player1: Player = {'name': 'Bob', 'points': 0, 'eliminated': False}
player2: Player = {'name': 'Alice', 'points': 0, 'alive': True}
