#!/usr/bin/env/python3.7
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
    





