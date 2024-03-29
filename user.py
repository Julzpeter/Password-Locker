class User:

    """
    Class that generates new instances of users
    """

    user_list = []

    def save_user(self):
        """
        save_user method saves users objects into user_list
        """
        User.user_list.append(self)



    def __init__(self,user_name,password):
        """
        _init_method that helps us define properties for our objects
        """
        self.user_name = user_name
        self.password = password
    
@classmethod
def find_by_user_name(cls,user_name):
    """
    Method that takes in a user_name and returns a user that matches that number.

    Args:
    user_name: User_name to search for 
    Returns: 
    User of person that matches the user_name.
    """
    for user in cls.user_list:
        if user.user_name == user_name:
            return user

@classmethod
def user_exist(cls,user_name,password):
    """
    Method that checks if  a user exists from the user list.
    Args:
    user_name: User_name to search if it exists
    Return:
    Boolean: True or falsedepending if the user exists
    """

    user = ""
    for user in cls.user_list:
        if user.user_name == user_name and password == password:
            user =  user.user_name
            return user


@classmethod 
def log_in(cls,user_name,password):
    """method that enables users to access their credentials
    """
    for user in cls.user_list:
        if user_name == user_name and password == password:
            return Credentials.credentials_list
    return False





## Credentials Class
class Credentials:
    """
    Class that generates new instances of contacts
    """
    credentials_list = []



    def __init__(self, site_name, site_username, site_password):
        """
        _init_method that helps us define properties for our objects
        """
        self.site_name = site_name
        self.site_username = site_username
        self.site_password = site_password

    def save_credentials(self):
        """
        save_credentials method saves credentials objects into credentials_list
        """
        Credentials.credentials_list.append(self)

@classmethod
def display_credentials(cls):
    """
    method that returns the credentials list
    """
    return cls.credentials_list

def delete_credential(self):
    """
    delete_credential method deletes a credential account from the credential list
    """
    Credentials.credentials_list.remove(self)

@classmethod
def find_by_site_name(cls,site_name):
    """
    method that takes in a site_name and returns a credential that matches that site name
    Args:
    site_name: Site_name to search for
    Returns: 
    Site_name of credential that matches the site_name
    """
    for credential in cls.credentials_list:
        if credential.site_name == site_name:
            return credential


@classmethod
def credential_exist(cls,site_name):
    """
    method that checks if a credential account exists from the credential list
    Args:
    site_name: Site_name to search if it exists
    Returns:
    Boolean: True or false depending if the credential exists
    """
    for credential in cls.credentials_list:
        if credential.site_name == site_name:
            return True
    return False







        


