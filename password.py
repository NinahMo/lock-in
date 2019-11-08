class Password:
    password_list = []
    def __init__(self,full_name,user_name,email,password_number,password_confirm):
        self.full_name = full_name
        self.user_name = user_name 
        self.email = email
        self.password_number = password_number
        self.password_confirm = password_confirm
    
    def save_password(self):
        Password.password_list.append(self)
        
# pass       