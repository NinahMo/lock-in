class User:
    user_list = []
    def __init__(self,full_name,login_name,email,password_value):
        '''
        Here we call ana array which has the login information and what is needed for the login.
        '''
        self.full_name = full_name
        self.login_name = login_name
        self.email = email
        self.password_value = password_value
    
    def save_user(self):
        '''
        this allows you to save your login information
        '''
        User.user_list.append(self)   
    
    @classmethod
    def user_authenticate(cls,loginname,passcode):
        '''
        this allows authentication of the the users information before allowing access.
        '''
        for user in cls.user_list:
            if user.login_name == loginname and user.password_value == passcode:
                return True
        
        return False        
        
#pass