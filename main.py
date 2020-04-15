from Match import Match
from Team import Team
import States

team7174 = Team(7174, 12)
team1114 = Team(1114, 12)
team6878 = Team(6878, 12)
team5032 = Team(5032, 12)
team3683 = Team(3683, 12)
team6977 = Team(6977, 12)

match1 = Match(team7174, team1114, team6878, team5032, team3683, team6977, States.gameStates.RedVictory)

print(match1.guessWinner())
print(team6977.rating)
match1.updateMatchElo()
print(team6977.rating)
