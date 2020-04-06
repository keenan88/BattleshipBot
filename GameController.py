from FriendlyBoard import FriendlyBoard
from EnemyBoard import EnemyBoard
from Player import Player

p1Board = FriendlyBoard()
p2Board = FriendlyBoard()

p1 = Player(p1Board, p2Board)
p2 = Player(p2Board, p1Board)

players = [p1, p2]

while not (p1.victorious or p2.victorious):
    for player in players:
        player.shoot()
