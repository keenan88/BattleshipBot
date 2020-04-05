from time import sleep
from BrowserNavigator import BrowserNavigator
browserNav = BrowserNavigator()

gameId = 98765787
browserNav.openGame(gameId)

browserNav.selectGameModeFriend()
browserNav.startGame()


sleep(2000)
browserNav.closeGame()
