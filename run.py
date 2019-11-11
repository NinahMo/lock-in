#!/usr/bin/env python3.6
from user import User
from password import Password

def create_user(fname,lname,email,passcode):
    new_user = User(fname,lname,email,passcode)
    return new_user

def create_password(aname,uname,pvalue):
    new_password = Password(aname,uname,pvalue)
    return new_password
def save_password(password):
    password.save_password()
    
def del_password(password):
    password.delete_password()
    
def display_contacts():
    return Password.display_passwords()

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
    
    print(f"Welcome {full_name} to LOCK-IN the best password locker around.What is your command? ")
    print('\n')
    while True:
        print("Okay to begin using the app you need to first choose your option : ca - create new information for account, da - display existing accounts, ex - exit LOCK-IN")        
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
                print("your password will be {p_value} ")
            else:
                print("Please enter custom password:")
                p_value = input()
                save_password(create_password(a_name,u_name,p_value))
            print('\n')    
            print(f"You have successfully created your account credentials {full_name} and they have been saved in the system.")
            
        elif short_code == 'dc':
            if display_passwords():
                print("Below are the various account informations you have created:")
                
                for password in display_passwords():
                    print(f"{password.app_name} {password.user_name} {password.password_number}")
            
            else:
                print('\n')
                print("You have no existing account information.")
                print('\n')
        
        elif short_code == "ex":
            print("Thank you for using our services.Bye!!")
            break
        
        else:
            print("Sorry fo the inconvinience but we are unable to read what you have written please try again using the correct short codes.")               
                

if __name__ == '__main__':
    main()