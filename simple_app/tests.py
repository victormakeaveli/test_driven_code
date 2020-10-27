import unittest
from django.test import Client
from django.urls import reverse


class testing(unittest.TestCase):

    def test_index_and_greeting(self):    
    
        #assume
        client = Client()
        response = client.get(reverse('index'))

        #action
        response_code = response.status_code

        #assert
        self.assertEquals(response_code, 200)

        self.assertEquals(response.content, f'Hello, {user}')

    def test_form_and_validation(self):

        #assume
        client = Client()
        validator = Validator()

        response = client.get(reverse('form'))
        
        username = 'Normal'
        user_age = 15

        #action
        response_code = response.status_code

        name_validation = validator.username_is_valid(username)
        age_validation = validator.user_age_is_valid(user_age)
        
        #assert
        #the url is ok
        self.assertEquals(response_code, 200)

        #it validates
        self.assertTrue(name_validation)
        self.assertTrue(age_validation)
    
    def test_bartender(self):

        #assume
        user_age_1 =< 10
        user_age_2 =< 20
        user_age_3 =< 30
         
        #action
        what_drink1 = calculous.drinks(user_age_1)
        what_drink2 = calculous.drinks(user_age_2)
        what_drink3 = calculous.drinks(user_age_3)

        #assert
        self.assertEqual(what_drink1, 'milk')
        self.assertEqual(what_drink2, 'coca-cola')
        self.assertEqual(what_drink3, 'vodka')

