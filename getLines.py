import os
cwd = os.getcwd()

class GetLinesFromFile:
    def GetLinesToList(self):
        with open(cwd + "\\accountsList.txt") as file:
            lines = [line.rstrip() for line in file]
        return lines