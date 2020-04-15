from Match import Match
from Team import Team
import States

team7174 = Team(7174, 12)
team1114 = Team(1114, 12)
team6878 = Team(6878, 12)
team5032 = Team(5032, 12)
team3683 = Team(3683, 12)
team6977 = Team(6977, 12)
team4343 = Team(4343, 12)
team2198 = Team(2198, 12)
team5031 = Team(5031, 12)
team6978 = Team(6978, 12)
team746 = Team(746, 12)
team5834 = Team(5834, 12)
team2405 = Team(2405, 12)
team4519 = Team(4519, 12)






match1 = Match(team7174, team1114, team6878, team5032, team3683, team6977, States.gameStates.BlueVictory)
match6 = Match(team746, team5834, team2405, team2198, team6977, team4519,  States.gameStates.RedVictory)
print(match1.guessWinner())
print(team6977.rating)
match1.updateMatchElo()
print(team6977.rating)
print(match6.guessWinner())
match6.updateMatchElo()
print(team6977.getRating())
