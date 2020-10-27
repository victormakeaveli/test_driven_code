import unittest

class testing_app(unittest.TestCase):

    def test_simple(self):    
    
        #assume
        x = True
    
        #action
        result = x
    
        #assert
        self.assertFalse(result)