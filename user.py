class User:

    """
    Class that generates new instances of users
    """

    user_list = []
    
    def _init_(self,user_name,password):
        """
        _init_method that helps us define properties for our objects
        """
        self.user_name = user_name
        self.password = password
        


