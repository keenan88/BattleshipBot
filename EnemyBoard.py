from enum import Enum

class EnemySquareState(Enum):
    UNKNOWN = " "
    MISS = "."
    HIT = "x"

class EnemySquare():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = EnemySquareState.UNKNOWN

class EmptyBoard():
    def __init__(self):
        self.board = []
        for row in range(10):
            self.board.append([None]*10)
            for column in range(10):
                self.board[row][column] = EnemySquare(column, row)

    def prettyPrint(self):
        self.printHorizontalBorder()
        print("")
        for row in self.board:
            self.printBoardRow(row)
        self.printHorizontalBorder()
        print("")

    def printHorizontalBorder(self):
        for _ in range(12):
            print("- ", end="")

    def printBoardRow(self, row):
        print("- ", end="")
        for square in row:
            print(square.state.value + " ", end="")
        print("- ", end="")
        print("")

class EnemyBoard():

    def __init__(self, board):
        self.enemyBoard = board
        self.knownEnemyBoard = EmptyBoard()
        print("enemy board:")
        self.knownEnemyBoard.prettyPrint()
