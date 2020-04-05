from random import randint
from enum import Enum

class ShipDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class SquareState(Enum):
    UNKNOWN = "?"
    MISS = "."
    HIT = "x"

class Square():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = SquareState.UNKNOWN




class Board():

    def __init__(self):
        self.board = []

        for x in range(10):
            self.board.append([])
            for y in range(10):
                self.board[x].append(Square(x, y))

        self.prettyPrint()

        unplacedShips = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        while(len(unplacedShips) > 0):
            self.placeShip(unplacedShips.pop(0))


    def placeShip(self, shipLength):
        shipPlaced = False

        while not shipPlaced:
            startingPoint = [randint(0,9), randint(0, 9)]
            direction = ShipDirection(randint(0, 3))
            print(shipLength)
            print(startingPoint)
            print(direction)

            for distance in range(shipLength):
                shipPlaced = shipPlaced and self.isSquareOpen(startingPoint, direction, distance)


    def isSquareOpen(self, startingPoint, direction, distance):
        if direction == ShipDirection.NORTH:
            pass


    def prettyPrint(self):
        for row in self.board:
            for square in row:
                print(square.state.value + " ", end="")
            print("")
