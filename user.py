class User:

    """
    Class that generates new instances of users
    """

    user_list = []
    def save_user(self):
        """
        save_contact method saves contact objects into contact_list
        """

    def __init__(self,user_name,password):
        """
        _init_method that helps us define properties for our objects
        """
        self.user_name = user_name
        self.password = password


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

       








        


