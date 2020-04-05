from selenium import webdriver

class BrowserNavigator():

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=options)

    def openGame(self, gameId):
        gameURL = "http://en.battleship-game.org/id" + str(gameId)
        self.driver.get(gameURL)

    def closeGame(self):
        self.driver.close()

    def selectGameModeFriend(self):
        friendBtn = self.driver.find_element_by_link_text("friend")
        friendBtn.click()

    def selectGameModeRussian(self):
        russianBtn = self.driver.find_element_by_css_selector(".battlefield-start-ships_type__default > .battlefield-start-ships_type-link")
        russianBtn.click()

    def startGame(self):
        startBtn = self.driver.find_element_by_css_selector(".battlefield-start-button")

    def selectCell(self, row, column):
        cellCSS = ".battlefield:nth-child(2) .battlefield-row:nth-child(" + str(row) + ") > .battlefield-cell:nth-child(" + str(column) + ") > .battlefield-cell-content"
        cell = self.driver.find_element_by_css_selector(cellCSS)
        cell.click()
