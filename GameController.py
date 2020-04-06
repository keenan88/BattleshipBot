from Board import Board
from EnemyBoard import EnemyBoard
from Player import Player

print("p1 board:")
p1Board = Board()
print("p2 board:")
p2Board = Board()

p1 = Player(p1Board, EnemyBoard(p2Board))
p2 = Player(p2Board, EnemyBoard(p1Board))

players = [p1, p2]

while not (p1.victorious or p2.victorious):
    for player in players:
        p1.victorious = True
        #player.shoot()
