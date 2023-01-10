class EnterCredentials:
    @staticmethod
    def GetCredentialsToList():
        #enter credentials
        username = input('please enter username: \n')
        password = input('please enter password: \n')
        credentials = [username, password]
        return credentials