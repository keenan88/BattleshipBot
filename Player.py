from random import randint
from FriendlyBoard import Square

class Player():

    def __init__(self, friendlyBoard, enemyBoard):
        self.friendlyBoard = friendlyBoard
        self.enemyBoard = enemyBoard
        self.victorious = False

    def shoot(self):
        selectedSquare = self.selectSquare()
        while self.enemyBoard.getSquare(selectSquare.x, selectedSquare.y).state != EnemySquareState.UNKNOWN:
            print("f")

    def selectSquare(self):
        randX = randint(0, 9)
        randY = randint(0, 9)

        return Square(randX, randY)
