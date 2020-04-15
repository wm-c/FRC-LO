from Team import Team

class Match():


        def __init__(self, red1: Team, red2: Team, red3: Team, blue1: Team, blue2: Team, blue3: Team):
                self.red1 = red1
                self.red2 = red2
                self.red3 = red3
                self.blue1 = blue1
                self.blue2 = blue2
                self.blue3 = blue3

        def guessWinner(self) -> int:
                '''Returns 0 for Blue, 1 for Red, 2 for Tie'''
                redRating = self.red1.rating + self.red2.rating + self.red3.rating
                blueRating = self.blue1.rating + self.blue2.rating + self.blue3.rating
                if(redRating >= blueRating):
                        if(redRating == blueRating):
                                self.red1.predicted,  self.red2.predicted, self.red3.predicted = 2
                                self.blue1.predicted,  self.blue2.predicted, self.blue3.predicted = 2
                                return "2"
                        self.red1.predicted,  self.red2.predicted, self.red3.predicted = 1
                        self.blue1.predicted,  self.blue2.predicted, self.blue3.predicted = 0
                        return "1"
                self.red1.predicted,  self.red2.predicted, self.red3.predicted = 0
                self.blue1.predicted,  self.blue2.predicted, self.blue3.predicted = 1
                return "tie"



                