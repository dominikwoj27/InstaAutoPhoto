from instagrapi import Client
import getLines
import time

class InstagrApiClient:
    
    username = ''
    password = ''
    client = 0
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client()
        self.client.login(self.username, self.password)
        
    def LikeProfilesFromFile(self, numberOfPics, timeDelay):
        
        getLinesFromFile = getLines.GetLinesFromFile()
        listOfAccounts = getLinesFromFile.GetLinesToList()

        for account in range(len(listOfAccounts)):
            print('starting liking pics of account: ', listOfAccounts[account])
            userId = self.client.user_id_from_username(listOfAccounts[account])
            userMediasList = self.client.user_medias(userId, numberOfPics, timeDelay)
            
            for item in range(len(userMediasList)):
                self.client.media_like(userMediasList[item].id)
                print('liked image with caption:', userMediasList[item].caption_text)
                time.sleep(timeDelay)
    