import unittest

from django.test import Client
from django.urls import reverse

import models

class Testing(unittest.TestCase):

    #assume
    def setUp(self):
        self.client = Client()
        self.validator = Validator()
        self.calculous = self.Calculous()
        self.user = User('Simple', 'Name', 15)
    

    def test_index_and_greeting(self):    
    
        response = self.client.get(reverse('index'))
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'Hello')
    

    def test_form_and_validation(self):

        self.response = self.client.get(reverse('form'))
        response_code = self.response.status_code

        #**validator will be a function inside the app**
        name_validation = self.validator.user_is_valid(self.username)
        
        #assert
        #the url is ok
        self.assertEquals(response_code, 200)

        #it validates 
        with self.assertTrue:
            self.

        with self.assertRaises(ValueError):
            self.user.name, int
            self.user.age, str


    def test_bartender(self):

        #assume
        user_age_less < self.user.age
        user_age_equal = self.user.age
        user_age_more > self.user.age

        #action
        #**calculous will be a function inside the app**
        which_drink_less = self.calculous.drinks(user_age_less)
        which_drink_equal = self.calculous.drinks(user_age_equal)
        which_drink_more = self.calculous.drinks(user_age_more)

        #assert
        self.assertEqual(which_drink_less, 'milk')
        self.assertEqual(which_drink_equal, 'coca-cola')
        self.assertEqual(which_drink_more, 'vodka')

