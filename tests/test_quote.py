import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of quote
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote("There are only two kinds of programming languages: those people always bitch about and those nobody uses.", "Bjarne Stroustrup")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))
