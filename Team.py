

class Team():

    def __init__(self, teamNumber: int, totalMatches: int):
        self.teamNumber = teamNumber
        self.totalMatches = totalMatches
        self.rating = 1000
        self.gamesPlayed = 0
        self.predicted = None

    def __repr__(self) -> str:
        return str(self.totalMatches)

    def __str__(self) -> str:
        return str(self.teamNumber)

    def getRating(self) -> int:
        return self.rating

    def setRating(self, newRating: int):
        self.rating = newRating

    def updateRating(self, matchNumber: int, expectedWin = 0, unexpectedWin = 0, expectedLoss = 0, unexpectedLoss = 0):
        multiplier = (matchNumber / self.totalMatches) + 1
        self.rating += (30 * expectedWin + 60 * unexpectedWin - 30 * expectedLoss - 60 * unexpectedLoss) * multiplier

    def incrementMatches(self):
        self.totalMatches += 1


    


        