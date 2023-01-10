import EnterCredentials 
import InstagrApiClient

#enter credentials
credentials = EnterCredentials.EnterCredentials.GetCredentialsToList()

#create client for instagrApi, like posts
instagrApiClient = InstagrApiClient.InstagrApiClient(credentials[0], credentials[1])
instagrApiClient.LikeProfilesFromFile(10, 1)
