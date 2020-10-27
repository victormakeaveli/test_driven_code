import unittest
from django.test import Client
from django.urls import reverse


class testing(unittest.TestCase):

    def test_index(self):    
    
        #assume
        client = Client()
        response = client.get(reverse('index'))

        #action
        response_code = response.status_code

        #assert
        self.assertEquals(response_code, 200, "urls doesn't exist")

        self.assertEquals(response.content, f'Hello, {user}', "message doesn't exists")

    def test_user_input(self):

        #assume
        client = Client()
        response = client.get(reverse('form'))

        #action
        response_code = response.status_code

        #assert
        #the page is ok
        self.assertEquals(response_code, 200, "urls doesn't exist")
        #the content is ok
        # self.assertEqual(response.content) #todo
