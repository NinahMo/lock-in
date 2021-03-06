#!/usr/bin/env python3.6
from user import User
from password import Password

def create_user(fname,lname,email,passcode):
    '''
    this creates a user portion which allows creation of account
    '''
    new_user = User(fname,lname,email,passcode)
    return new_user

def save_user(User):
    '''
    this saves your user infomation and also authenticates it
    '''
    User.save_user()
def create_password(app_name,user_name,password_number):
    '''
    this creates a path for you to build your information
    '''
    new_password = Password(app_name,user_name,password_number)
    return new_password
def save_password(password):
    '''
    this saves your password credentials in the main
    '''
    password.save_password()
    
def del_password(password):
    '''
    this function allows you to delete information
    '''
    password.delete_password()
def find_by_appname(app_name):
    '''
    this allows you to find the specific account
    '''
    return Password.find_account_byappname(app_name)   
def display_password():
    '''
    this displays all your available contacts
    '''
    return Password.display_passwords()

def authenticate_user(loginname,passcode):
    '''
    this prooves one is the user then gives them access to the app
    '''
    return User.user_authenticate(loginname,passcode)

def valid_user(full_name,login_name,email,passcode):
    '''
    this validates your information and allows you to run
    '''
    if full_name=="" or login_name=="" or email=="" or passcode=="" :
        return False
    else:
        return True
    
def main():
    print("Welcome to Lock-in.")
    print("This is a python built app that allows you to easily store and delete your password information.")
    print('\n')
    
    print("PLease enter your full name:")    
    full_name = input()
    print("Write down a login user name please:")
    login_name = input()
    print("Now,write your email address:")
    email = input()    
    print("Inorder for you to proceed you need a password.")
    passcode = input()
    
    validAccount = valid_user(full_name,login_name,email,passcode)
    if validAccount:
        save_user(create_user(full_name,login_name,email,passcode))
        print('\n')
        print(f"{full_name} you have successfully created an account...")
        print('\n')
        
        print("login  below with your user account information")
        print('\n')
        
        print("please enter your user name")
        loginUser = input()
        
        print("enter passcode")
        loginPasscode = input()
        
        if authenticate_user(loginUser,loginPasscode):
            print(f"{loginUser} Welcome to LOCK-IN")
            print('\n')
    
    
            while True:
                print("Okay to begin using the app you need to first choose your option : ca - create new information for account, da - display existing accounts,del - delete an account, ex - exit LOCK-IN")        
                print('\n')
                short_code = input().lower()
                
                if short_code == 'ca':
                    print("Enter the name of the application:")
                    a_name = input()
                    
                    print("Enter your username for the application:")
                    u_name = input()
                    
                    print("Do you want a custom password for your account? yes/no ")
                    custom_code = input().lower()
                    
                    if custom_code == 'yes':
                        p_value = u_name[:5] + "4211"                
                        print(f"your password will be {p_value} ")
                        print('\n')
                    else:
                        print("Please enter custom password:")
                        p_value = input()
                        save_password(create_password(a_name,u_name,p_value))
                    print('\n')    
                    print(f"You have successfully created your account credentials {full_name} and they have been saved in the system.")
                    print('\n')
                elif short_code == 'da':
                    if display_password():
                        print("Below are the various account informations you have created:")
                        print('\n')
                        for password in display_password():
                            print(f"This is your account:...app:{password.app_name},name:{password.user_name},passcode:{password.password_number}")
                    
                    else:
                        print('\n')
                        print("You have no existing account information.")
                        print('\n')
                
                elif short_code == 'del':
                    print("To delete an account please write the name of the app.")
                    del_info = input()
                    del_acc = find_by_appname(del_info)
                    if del_acc.app_name == del_info:
                        del_acc.delete_password()
                        print('\n')
                        print("you have deleted your information.")
                    else:
                        print('\n')
                        print("The above file does not exist.")
                        print('\n')        
                elif short_code == 'ex':
                    print("Thank you for using our services.Bye!!")
                    break
                
                else:
                    print('\n')
                    print("Sorry fo the inconvinience but we are unable to read what you have written please try again using the correct short codes.")               
                    print('\n')    

        else:
            print("Invalid User name please try again.")
            print('\n')
    else:
        print("Enter your correct details")
                
    
if __name__ == '__main__':
    main()