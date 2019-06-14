import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours
    """
    """
    unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run efore each test cases
        """
        self.new_user = User("JulietKoech","12338")
        self.new_credentials = Credentials("Twitter", "Julz", "12338")

    def test_init(self):
        """test_init test case to test if the object is initialized properly
        """


