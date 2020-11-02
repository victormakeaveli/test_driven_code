import unittest

from django.test import Client, TestCase
from django.urls import reverse
from .models import *
 
#gabriel help
#import json
# 

class Testing(TestCase):

    #assume
    def setUp(self):

        self.client = Client()

        self.user = Users()
        self.user.name = 'victor'
        self.user.age = 22
        # self.calculous = calculous()
    

    def test_index_and_greeting(self):    
    
        response = self.client.get(reverse('index'))
        
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "hello")

        #gabriel help
        # print(dir(response))
        # self.AssertEquals(json.loads(response.content), "hello")
        #
class Testing_1(unittest.TestCase):

    #assume
    def setUp(self):

        self.client = Client()

        self.user = Users()
        self.user.name = 'victor'
        self.user.age = 22
        # self.calculous = calculous()
    
    def test_name_validation(self):
        self.assertIsInstance(self.user.name, str)

    def test_age_validation(self):
        self.assertIsInstance(self.user.age, int)

    #     print(type(self.user.name))
    #     with self.assertRaises(ValueError):
    #         self.user.name != str


    # def test_form(self):


    #     response = self.client.get(reverse('form'))
    #     response_code = self.response.status_code

    #     #**validator will be a function inside the app**
    #     name_validation = self.validator.user_is_valid(self.username)
        
    #     #assert
    #     #the url is ok
    #     self.assertEquals(response_code, 200)
    #     it validates 


    # def test_bartender(self):

    #     #assume
    #     user_age_less = self.user.age
    #     user_age_equal = self.user.age
    #     user_age_more > self.user.age

    #     #action
    #     #**calculous will be a function inside the app**
    #     which_drink_less = self.calculous(user_age_less)
    #     which_drink_equal = self.calculous(user_age_equal)
    #     which_drink_more = self.calculous(user_age_more)
                
    #     #assert
    #     self.assertEqual(which_drink_less, 'milk')
    #     self.assertEqual(which_drink_equal, 'coca-cola')
    #     self.assertEqual(which_drink_more, 'vodka')

# if __name__ == '__main__':
#     unittest.main()