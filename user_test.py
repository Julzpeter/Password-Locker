import unittest
from user import User
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