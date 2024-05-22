import os

class Playernick:
    playersArray = []
    statDirectory = 'stats'
    playersPath = 'players.txt'
    workingDirectory = os.getcwd()
    Nickname = ''

    @staticmethod
    def GetNickname():
        return Playernick.Nickname

    @staticmethod
    def SetNickname(nick):
        Playernick.Nickname = nick
        Playernick.CreatePlayersFileIfNotExists()
        if not Playernick.NickExists(nick):
            Playernick.AppendToFile()
        playersArray = Playernick.GetAllPLayers()
        Playernick.CreateFileForPlayer()

    @staticmethod
    def CreatePlayersFileIfNotExists():
        Playernick.CreateStatDir()
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, Playernick.playersPath)
        if not os.path.exists(path):
            open(path, 'a')
    @staticmethod
    def NickExists(nick):
        list = Playernick.GetAllPLayers()
        if list.__contains__(nick + '\n'):
            return True
        return False

    @staticmethod
    def GetAllPLayers():
        Playernick.CreatePlayersFileIfNotExists()
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, Playernick.playersPath)
        f = open(path, 'r')
        return f.readlines()

    @staticmethod
    def AppendToFile():
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, Playernick.playersPath)
        f = open(path, 'a')
        f.write(Playernick.Nickname + '\n')

    @staticmethod
    def CreateStatDir():
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory)
        if not os.path.exists(path):
            os.mkdir(path)

    @staticmethod
    def SaveScore(score):
        filename = Playernick.Nickname + '.txt'
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, filename)
        f = open(path, 'a')
        f.write(str(score) + '\n')

    @staticmethod
    def CreateFileForPlayer():
        Playernick.CreateStatDir()
        filename = Playernick.Nickname + '.txt'
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, filename)
        if not os.path.exists(path):
            open(path, 'a')

    @staticmethod
    def GetBestScore():
        filename = Playernick.Nickname + '.txt'
        path = os.path.join(Playernick.workingDirectory, Playernick.statDirectory, filename)
        if not os.path.exists(path):
            return -1

        f = open(path, 'r')
        lines = f.readlines()
        if len(lines) == 0:
            return -1
        ints = [int(numeric_string) for numeric_string in lines]
        return max(ints)


