import getLines
    
getLinesFromFile = getLines.GetLinesFromFile()
listOfAccounts = getLinesFromFile.GetLinesToList()

for i in range(len(listOfAccounts)):
    print (listOfAccounts[i])
    