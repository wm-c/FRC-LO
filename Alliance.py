from Team import Team
import States


class Alliance():

    correct = 0

    def __init__(self, team1: Team, team2: Team, team3: Team):
        self.teamList = [team1, team2, team3]
        self.rating = team1.rating + team2.rating + team3.rating
        self.predicted = None
        self.actual = None
    
    def __str__(self):
        return f"{self.team1}, {self.team2}, {self.team3}"

    def adjustElo(self, allianceScore: int, opponentScore: int):
        teamList = self.teamList
        
        if(self.actual == self.predicted):
            [team.updateRating(self.actual, 0, allianceScore, opponentScore) for team in teamList]
            Alliance.correct += 1
        else:
            [team.updateRating(0, self.actual, allianceScore, opponentScore) for team in teamList]
    
        

        