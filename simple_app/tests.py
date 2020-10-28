import unittest

from django.test import Client
from django.urls import reverse


class testing(unittest.TestCase):

    #assume
    def setUp(self):
        self.client = Client()
        self.validator = Validator()
        self.username = 'Normal'
        self.user_age = 15
    
    def tearDown(self):
        pass

    def test_index_and_greeting(self):    
    
        response = self.client.get(reverse('index'))
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'Hello')

    def test_form_and_validation(self):

        self.response = self.client.get(reverse('form'))
        response_code = self.response.status_code

        #**validator will be a function inside the app**
        name_validation = validator.username_is_valid(self.username)
        age_validation = validator.user_age_is_valid(self.user_age)
        
        #assert
        #the url is ok
        self.assertEquals(response_code, 200)

        #it validates
        with self.assertTrue:
            name_validation
            age_validation

        with self.assertRaises(ValueError):
             name_validation, int 
             age_validation, str 


    def test_bartender(self):

        #assume
        user_age_less < self.user_age
        user_age_equal = self.user_age
        user_age_more > self.user_age
         
        #action
        #**calculous will be a function inside the app**
        what_drink_less = calculous.drinks(user_age_less)
        what_drink_equal = calculous.drinks(user_age_equal)
        what_drink_more = calculous.drinks(user_age_more)

        #assert
        self.assertEqual(what_drink_less, 'milk')
        self.assertEqual(what_drink_equal, 'coca-cola')
        self.assertEqual(what_drink_more, 'vodka')

