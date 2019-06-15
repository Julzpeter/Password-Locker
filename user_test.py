import unittest 
from user import User,Credentials


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours
    """
    """
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run efore each test cases
        """
        self.new_user = User("JulietKoech","12338")
        self.new_credentials = Credentials("Twitter", "Julz", "12338")

    def test__init__(self):
        """test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.user_name,"JulietKoech")
        self.assertEqual(self.new_user.password,"12338")

        self.assertEqual(self.new_credentials.site_name,"Twitter")
        self.assertEqual(self.new_credentials.site_username,"Julz")
        self.assertEqual(self.new_credentials.site_password,"12338")

    def test_save_user(self):
        """
        test_save_contact test case to test if the contact object is saved into the contact_list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        User.user_list = []
        Credentials.credentials_list = []

def test_save_multiple_user(self):
        """
        test_save_multiple _user to check if we can save multiple user object to our user_list
        """
        self.new_user.save_user()
        test_user = User("Test","12338")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

def test_find_user_by_user_name(self):
        """
        test to check if we can find a user by user_name and display information
        """
        self.new_user.save_user()
        test_user = User("Test","12338")
        test_user.save_user()
        found_user = User.find_by_user_name("Test")
        
        self.assertEqual(found_user.user_name,test_user.user_name)

def 










if __name__ =='__main__':
        unittest.main()









