from Team import Team
from Alliance import Alliance
import States



class Match():


        def __init__(self, red1: Team, red2: Team, red3: Team, blue1: Team, blue2: Team, blue3: Team, winner: States.gameStates, redScore: int, blueScore: int):
                self.redAlliance = Alliance(red1, red2, red3)
                self.blueAlliance = Alliance(blue1, blue2, blue3)
                self.winner = winner
                print(f"{self.guessWinner()},{winner}")
                self.updateMatchElo(redScore, blueScore)

        def guessWinner(self) -> States.gameStates:
                '''Returns 0 for Blue, 1 for Red, 2 for Tie'''

                redAlliance = self.redAlliance
                blueAlliance = self.blueAlliance


                # Calculates total team rating
                redRating = redAlliance.rating
                blueRating = blueAlliance.rating

                # Finds predicted outcome based on total team rating
                if(redRating >= blueRating):

                        # Sets prediction to tie if ratings are equal
                        if(redRating == blueRating):
                                redAlliance.predicted = 0
                                blueAlliance.predicted = 0
                                return States.gameStates.Tie

                        # Sets red alliance prediction to win
                        redAlliance.predicted = 1
                        blueAlliance.predicted = -1
                        return States.gameStates.RedVictory

                # Sets blue alliance prediction to win
                blueAlliance.predicted = 1
                redAlliance.predicted = -1
                return States.gameStates.BlueVictory

        def updateMatchElo(self, redScore: int, blueScore: int):
                winner = self.winner
                redAlliance = self.redAlliance
                blueAlliance = self.blueAlliance

                if(winner == States.gameStates.BlueVictory):
                        blueAlliance.actual = 1
                        redAlliance.actual = -1

                elif(winner == States.gameStates.RedVictory):
                        redAlliance.actual = 1
                        blueAlliance.actual = -1
                else:
                        redAlliance.actual = blueAlliance.actual = 0

                blueAlliance.adjustElo(blueScore, redScore)
                redAlliance.adjustElo(redScore, blueScore)   
        
        