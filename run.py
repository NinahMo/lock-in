from user import User
from password import Password

def create_user(fname,lname,email,password):
    new_user = User(fname,lname,email,password)
    return new_user

def  create_password(aname,uname,pnumber):
    new_password = Password(aname,uname,pnumber)
    return new_password
def save_password(password):
    password.save_password()
    
def del_password(password):
    password.delete_password()
    
def display_contacts():
    return Password.display_passwords()

def main():
    print("Welcome to Lock-in.This is a python built app that allows you to easily store and delete your password information.")
    print("PLease enter your full name:")    
    full_name = input()
    print("Write down a login user name please:")
    login_name = input()
    print("Now,write your email address:")
    email = input()    
    print("Inorder for you to proceed you need a password.")
    password = input()
    
    print("Welcome {full_name} to LOCK-IN the best password locker around.What is your command? ")
    print('\n')
    while True:
        print("Okay to begin using the app you need to first choose your option : ca - create new information for account, da - display existing accounts, ex - exit LOCK-IN")        
        short_code == input().lower()
        
        
    
    


if __name__ == '__main__':
    main()