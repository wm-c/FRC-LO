from Team import Team
import States


class Alliance():

    def __init__(self, team1: Team, team2: Team, team3: Team):
        self.teamList = [team1, team2, team3]
        self.rating = team1.rating + team2.rating + team3.rating
        self.predicted = None
        self.actual = None
    
    def __str__(self):
        return f"{self.team1}, {self.team2}, {self.team3}"

    def adjustElo(self):
        teamList = self.teamList
        
        if(self.actual == self.predicted):
            [team.updateRating(team.matchesPlayed, expected = self.actual) for team in teamList]
            
        else:
            [team.updateRating(team.matchesPlayed, unexpected = self.actual) for team in teamList]
        

        