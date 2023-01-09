import time
import getLines
from instagrapi import Client

client = Client()
client.login('username', 'password')

getLinesFromFile = getLines.GetLinesFromFile()
listOfAccounts = getLinesFromFile.GetLinesToList()

for account in range(len(listOfAccounts)):
    print('starting liking pics of account: ', listOfAccounts[account])
    userId = client.user_id_from_username(listOfAccounts[account])
    userMediasList = client.user_medias(userId, 10, 1)
    
    for item in range(len(userMediasList)):
        client.media_like(userMediasList[item].id)
        print('liked image with caption:', userMediasList[item].caption_text)
        time.sleep(1)
    