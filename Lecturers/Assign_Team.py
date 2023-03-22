



class Team:

    def __init__(self, team, Nationality, PremierLeague, points,played,wins,goals):
        self.__team = team
        self.__Nationality = Nationality
        self.__points = points
        self.__played = played
        self.__wins = wins
        self.__goals = goals
        self.__PremierLeague = PremierLeague

    def resetAll(self):
        self.__points = 0
        self.__played = 0
        self.__wins = 0
        self.__goals = 0

    def addGoals(self, goals):
        self.__goals += goals

    def getGoals(self):
        return self.__goals

    def getName(self):
        return self.__team

    def getNationality(self):
        return self.__Nationality

    def getPoints(self):
        return self.__points

    def getPlayed(self):
        return self.__played

    def getWins(self):
        return self.__wins

    def getPremierLeague(self):
        return self.__PremierLeague

    def getPercentWins(self):
        if (self.__played)==0:
            return 0
        else:
            return int(100 * (self.__wins / (self.__played)))

    def markWin(self):
        self.__points+= 3
        self.__played += 1
        self.__wins += 1

    def markDraw(self):
        self.__points += 1
        self.__played+= 1

    def markLoss(self):
        self.__played += 1