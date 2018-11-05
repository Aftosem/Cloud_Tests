class Parametrs:
    pathP = ""
    cycleP = int

    def setPath(self):
        Parametrs.pathP = input("Enter CC ip https://192.168.0.")

    def setCycle(self):
        Parametrs.cycleP = input("Enter how many times repeat = ")

    def getPath(self):
        path = Parametrs.pathP
        return path

    def getCycle(self):
        cycle = Parametrs.cycleP
        return cycle
