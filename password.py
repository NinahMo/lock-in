class Password:
    password_list = []
    def __init__(self,app_name,user_name,password_number):
        self.app_name = app_name
        self.user_name = user_name 
        self.password_number = password_number
      
    
    def save_password(self):
        Password.password_list.append(self)
     
    def delete_password(self):
        Password.password_list.remove(self)
    
    @classmethod
    def display_passwords(cls):
        return cls.password_list    
            
# pass       