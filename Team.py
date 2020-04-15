

class Team():

    def __init__(self, teamNumber: int, totalMatches: int):
        self.teamNumber = teamNumber
        self.totalMatches = totalMatches
        self.rating = 1000
        self.gamesPlayed = 0
        self.matchesPlayed = 1

    def __repr__(self) -> str:
        return str(self.totalMatches)

    def __str__(self) -> str:
        return str(self.teamNumber)

    def getRating(self) -> int:
        return self.rating

    def setRating(self, newRating: int):
        self.rating = newRating

    def updateRating(self, matchNumber: int, expected = 0, unexpected = 0):
        
        multiplier = (matchNumber / self.totalMatches) + 1
        self.rating += (30 * expected + 60 * unexpected) * multiplier
        print(f"Team # {self.teamNumber}, multiplier {multiplier}, expected {expected}, unexpected {unexpected}")
        self.gamesPlayed += 1

    def incrementMatches(self):
        self.totalMatches += 1


    


        