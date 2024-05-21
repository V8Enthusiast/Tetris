import os

class Playernick:
    playersArray = []
    statDirectory = 'stats'
    playersPath = 'players.txt'
    workingDirectory = os.getcwd()

    @staticmethod
    def CreatePlayersFileIfNotExists():
        Playernick.CreateStatDir()
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, Playernick.playersPath)
        if not os.path.exists(path):
            open(path, 'a')
    @staticmethod
    def NickExists(nick):
        if Playernick.GetAllPLayers().__contains__(nick):
            return True
        return False

    @staticmethod
    def GetAllPLayers():
        Playernick.CreatePlayersFileIfNotExists()
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, Playernick.playersPath)
        f = open(path, 'r')
        return f.readlines()

    def __init__(self, nickname):
        self.nick = nickname
        self.CreatePlayersFileIfNotExists()
        if not Playernick.NickExists(nickname):
            self.AppendToFile()
        self.playersArray = Playernick.GetAllPLayers()
        self.CreateFileForPlayer()

    def AppendToFile(self):
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, Playernick.playersPath)
        f = open(path, 'a')
        f.write(self.nick + '\n')

    @staticmethod
    def CreateStatDir():
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory)
        if not os.path.exists(path):
            os.mkdir(path)


    def SaveScore(self, score):
        filename = self.nick + '.txt'
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, filename)
        f = open(path, 'a')
        f.write(score + '\n')

    def CreateFileForPlayer(self):
        Playernick.CreateStatDir()
        filename = self.nick + '.txt'
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, filename)
        if not os.path.exists(path):
            open(path, 'a')