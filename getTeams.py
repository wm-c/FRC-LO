from getData import data
from Team import Team

teams = {}


for rows in range(data.index.stop):
    row = data.iloc[rows]
    teamNumbers = [row.Red_1, row.Red_2, row.Red_3, row.Blue_1, row.Blue_2, row.Blue_3]
    
    for teamCol in teamNumbers:
        if(not teamCol in teams):
            teams[teamCol] = Team(teamCol, 1)
        else:
            teams[teamCol].incrementMatches()


def getTeams():
    return teams

