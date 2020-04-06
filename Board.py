from random import randint
from enum import Enum

class ShipDirection(Enum):
    NORTH = [0, 1]
    EAST = [1, 0]
    SOUTH = [0, -1]
    WEST = [-1, 0]

class FriendlySquareState(Enum):
    SHIP = "#"
    EMPTY = " "
    UNPLACEABLE = ", "

class Square():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = FriendlySquareState.EMPTY


class Board():

    def __init__(self):
        self.board = self.populateEmptyBoard()
        self.placeShips()
        self.eraseUnplaceableSquares()
        self.prettyPrint()

    def populateEmptyBoard(self):
        board = []
        for row in range(10):
            board.append([None]*10)
            for column in range(10):
                board[row][column] = Square(column, row)
        return board

    def placeShips(self):
        unplacedShips = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        for ship in unplacedShips:
            shipSquares = self.findPlacementSquares(ship)
            self.placeShip(shipSquares)
            self.BlockAdjacentSqaures(shipSquares)

    def findPlacementSquares(self, shipLength):
        startingPoint = self.getFirstShipSquare()
        direction = self.getRandDirection()

        selectedSquares = [startingPoint]
        selectedSquaresValid = True
        currentSquare = startingPoint
        while len(selectedSquares) < shipLength and selectedSquaresValid:
            try:
                nextSquare = self.getNextSquare(currentSquare, direction.value)

                selectedSquaresValid = selectedSquaresValid and nextSquare.state == FriendlySquareState.EMPTY
                selectedSquares.append(nextSquare)
                currentSquare = nextSquare
            except Exception as e:
                selectedSquares = self.findPlacementSquares(shipLength)

        return selectedSquares

    def getFirstShipSquare(self):
        startingPoint = self.getSquare(randint(0,9), randint(0, 9))

        while startingPoint.state != FriendlySquareState.EMPTY:
            startingPoint = self.getSquare(randint(0,9), randint(0, 9))

        return startingPoint

    def getNextSquare(self, startingSquare, direction):
        nextX = startingSquare.x + direction[0]
        nextY = startingSquare.y + direction[1]

        if nextX < 0 or nextX > 9:
            raise ValueError('x coordinate was off the board')
        if nextY < 0 or nextY > 9:
            raise ValueError('y coordinate was off the board')

        nextSquare = self.getSquare(nextX, nextY)

        if nextSquare.state != FriendlySquareState.EMPTY:
            raise ValueError('SQUARE ALREADY TAKEN')

        return nextSquare

    def getSquare(self, x, y):
        if x < 0 or x > 9:
            raise ValueError('x coordinate was off the board')
        if y < 0 or y > 9:
            raise ValueError('y coordinate was off the board')

        return self.board[y][x]

    def getRandDirection(self):
        randDirection = randint(0, 3)
        if randDirection == 0:
            return ShipDirection.NORTH
        elif randDirection == 1:
            return ShipDirection.EAST
        elif randDirection == 2:
            return ShipDirection.SOUTH
        elif randDirection == 3:
            return ShipDirection.WEST

    def placeShip(self, shipSquares):
        for square in shipSquares:
            square.state = FriendlySquareState.SHIP

    def BlockAdjacentSqaures(self, shipSquares):
        for shipSquare in shipSquares:
            for x in range(3):
                for y in range(3):
                    try:
                        adjacentSqaure = self.getSquare(shipSquare.x + (x-1), shipSquare.y + (y-1))
                        if adjacentSqaure.state == FriendlySquareState.EMPTY:
                            adjacentSqaure.state = FriendlySquareState.UNPLACEABLE
                    except:
                        pass

    def eraseUnplaceableSquares(self):
        for row in self.board:
            for square in row:
                square.state = FriendlySquareState.EMPTY if square.state == FriendlySquareState.UNPLACEABLE else square.state


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
