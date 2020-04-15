from Match import Match
from Team import Team
from getTeams import getTeams
import getData
import States
from Alliance import Alliance

teams = getTeams()
matchTeams = getData.getRow(0)

victorDict = {
    "RED": States.gameStates.RedVictory,
    "BLUE": States.gameStates.BlueVictory,
    "TIE": States.gameStates.Tie

}

for match in range(getData.getSize()):
    matchTeams = getData.getRow(match)
    Match(
        teams[matchTeams.Red_1], teams[matchTeams.Red_2], teams[matchTeams.Red_3], 
        teams[matchTeams.Blue_1], teams[matchTeams.Blue_2], teams[matchTeams.Blue_3], 
        victorDict[matchTeams.Winner], matchTeams.Red_Score, matchTeams.Blue_Score
        )

for team in teams:
    print(f"{team},{teams[team].getRating()}")

print(Alliance.correct / 2)





