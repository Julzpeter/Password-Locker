#!/usr/bin/env python3.7
from user import User,Credentials
def create_user(uname,password):
    """
    Function to create a bew user
    """
    new_user = User(uname,password)
    return new_user

def save_users(user):
    """
    Fuction to save user
    """
    user.save_user()

def find_user(user_name):
    """
    Function that finds a user by username and returns the user
    """
    return User.find_by_user_name(user_name)

def check_existing_users(user_name,password):
    
    """
    Function that check if a user exists with that username and return a boolean
    """


    new_user = User(user_name,password)

    return new_user


def create_credentials(site_name, site_username, site_password):
    '''
    Function to create a new credential account
    '''
    new_credentials = Credentials(site_name, site_username, site_password)
    return new_credentials


def save_credentials(credential):
    '''
    Function to save credentials
    '''
    credential.save_credential()


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def find_credentials(site_name):
    '''
    Function that finds a creddential account by sitename and returns the credential account.
    '''
    return Credentials.find_by_site_name(site_name)


def check_existing_credentials(site_name):
    '''
    Function that check if a credential account exists with that sitename and return a Boolean
    '''
    return Credentials.credential_exist(site_name)


def del_contact(credential):
    '''
    Function to delete a credential account
    '''
    credential.delete_credential()

def log_in(user_name,password):
    """Function that enables the user to login into his account
    """
    log_in == User.log_in(user_name,password)
    if log_in != False:
        return User.log_in(user_name,password)


def main():
    print("Hello Welcome to Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}.")
    print('\n')

    while True:
        print('\n')
        print("Use these short codes : cc - create a new user, li -to login ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-"*10)

            print("User name ....")
            user_name = input()

            print("Password ...")
            password = input()

            # create and save new user.
            save_users(create_user(user_name, password))
            print('\n')
            print(f"New User {user_name} created")
            print('\n')
            print('\n')

        if short_code == 'li':
            print("Login in")
            print('\n')
            print("Enter your username")
            user_name = input()
            print("Enter your password")
            password = input()
            #user_exist = check_existing_users(user_name, password)
            print('\n')
            print('\n')

        elif short_code =='li':
            """Users login to their accounts
            """
            print('\n')
            print ("Login to your account")
            print("Enter your username")
            user_name = input()

            print("Enter the password")
            password = input()

            if log_in(user_name,password) == None:
                print('\n')
                print("PLease try again or create password")
                print('\n')

            else:
                log_in(user_name,password)
                print('\n')
                print(f"{user_name} WELCOME TO YOUR CREDENTIALS\n Use these short codes")

                while True:
                    print("Short codes: ca:Credential Account,dc:Display Credential accounts")
        
        if short_code == 'ca':
            print("New Credential Account")
            print("-"*10)

            print("Site name ....")
            site_name = input()

            print("Site user name ....")
            site_username = input()

            print("Site Password ...")
            site_password = input()

            # create and save new credential account.
            save_credentials(create_credentials(site_name, site_username, site_password))
            print('\n')
            print(f"New Credential {site_name} {site_username} {site_password}  created")
            print('\n')

        elif short_code == 'dc':
            if display_credentials():
                print("Here is a list of all your crenditial accounts")
                print('\n')
                for credential in display_credentials():
                    print(f"{credential.site_name} {credential.site_username} .....{credential.site_password}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'd':
                print("Enter the credential account you want to delete")
                search_site_name = input()
                if check_existing_credentials(search_site_name):
                    search_site_name = find_credentials(
                    search_site_name)
                    print(f"{search_site_name.site_name} ")
                    print('-' * 20)

                    Credentials.credentials_list.remove(search_site_name)

                else:
                    print("That credential account does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
            print("I really didn't get that. Please use the short codes")

                    

if __name__ == '__main__':
    main()
