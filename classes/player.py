import os

class Player:
    playersArray = []
    statDirectory = 'stats'
    playersPath = 'players.txt'
    workingDirectory = os.getcwd()

    def __init__(self, nickname):
        self.nick = nickname
        self.CreatePlayersFileIfNotExists()
        if not Player.NickExists(nickname):
            self.AppendPlayerToFile()
        self.playersArray = Player.GetAllPLayers()
        self.CreateFileForPlayerIfNotExists()

    def SaveScore(self, score):
        filename = self.nick + '.txt'
        path = os.path.join(Player.workingDirectory, Player.statDirectory, filename)
        f = open(path, 'a')
        f.write(score + '\n')

    def AppendPlayerToFile(self):
        path = os.path.join(Player.workingDirectory, Player.statDirectory, Player.playersPath)
        f = open(path, 'a')
        f.write(self.nick + '\n')

    def CreateFileForPlayerIfNotExists(self):
        Player.CreateStatDirIfNotExists()
        filename = self.nick + '.txt'
        path = os.path.join(Player.workingDirectory, Player.statDirectory, filename)
        if not os.path.exists(path):
            open(path, 'a')

    @staticmethod
    def NickExists(nick):
        if Player.GetAllPLayers().__contains__(nick):
            return True
        return False

    @staticmethod
    def GetAllPLayers():
        Player.CreatePlayersFileIfNotExists()
        path = os.path.join(Player.workingDirectory, Player.statDirectory, Player.playersPath)
        f = open(path, 'r')
        return f.readlines()

    @staticmethod
    def CreateStatDirIfNotExists():
        path = os.path.join(Player.workingDirectory, Player.statDirectory)
        if not os.path.exists(path):
            os.mkdir(path)

    @staticmethod
    def CreatePlayersFileIfNotExists():
        Player.CreateStatDirIfNotExists()
        path = os.path.join(Player.workingDirectory, Player.statDirectory, Player.playersPath)
        if not os.path.exists(path):
            open(path, 'a')


